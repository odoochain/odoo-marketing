# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.osv import expression
import requests

_logger = logging.getLogger(__name__)

class Mailing(models.Model):
    _inherit = 'mailing.mailing'

    fb_page_id = fields.Many2many("facebook.page_id")
    fmsg = fields.Char()
    fimage = fields.Char()

    facebook_force_send = fields.Boolean(
        'Send Directly', help='Use at your own risks.')

    # mailing options
    mailing_type = fields.Selection(selection_add=[
        ('facebook', 'Facebook')
    ], ondelete={'facebook': 'set default'})

    @api.model
    def default_get(self, fields):
        res = super(Mailing, self).default_get(fields)
        if fields is not None and 'keep_archives' in fields and res.get('mailing_type') == 'facebook':
            res['keep_archives'] = True
        if fields is not None and 'mailing_model_name' in fields and res.get('mailing_type') == 'facebook':
            res['mailing_model_name'] = 'facebook.list'
        return res

   

    def action_put_in_queue_facebook(self):
        res = self.action_put_in_queue()
        if self.facebook_force_send:
            self.action_send_mail()
        return res


    def action_send_now_facebook(self):
        self.state= 'done'
        self.sent_date= fields.Datetime.now()
        for i in range(len(self.fb_page_id)):
            if not self.fimage:
                payload = {
                'message' : self.fmsg,
                'access_token' : self.fb_page_id[i].facebook_access_token
                }
                post_url = 'https://graph.facebook.com/{}/feed'.format(self.fb_page_id[i].page_id) 
                r = requests.post(post_url, data=payload)
                print(r.text)
                return r
            elif not self.fmsg:
                image_url = 'https://graph.facebook.com/{}/photos'.format(self.fb_page_id[i].page_id)
                image_location = self.fimage
                img_payload = {
                'url' : image_location,
                'access_token': self.fb_page_id[i].facebook_access_token
                }
                r = requests.post(image_url, data=img_payload)
                print(r.text)
                return r
            else : 
                image_url = 'https://graph.facebook.com/{}/photos'.format(self.fb_page_id[i].page_id)
                image_location = self.fimage
                img_payload = {
                'message' : self.fmsg,
                'url' : image_location,
                'access_token': self.fb_page_id[i].facebook_access_token
                }
                r = requests.post(image_url, data=img_payload)
                print(r.text)
                return r

            
    @api.model
    def action_send_schedule_facebook(self):
        mass_mailings = self.search([('state', 'in', ('in_queue', 'sending')), ('mailing_type', '=', 'facebook'), '|', ('schedule_date', '<', fields.Datetime.now()), ('schedule_date', '=', False)])
        for mass_mailing in mass_mailings:
            mass_mailing.action_send_now_facebook()         
        


    def action_schedule_facebook(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("fw_odoo_facebook_marketing.facebook_schedule_date_action")
        action['context'] = dict(self.env.context, default_facebook_id=self.id)
        return action
        

    @api.depends('mailing_type')
    def _compute_medium_id(self):
        super(Mailing, self)._compute_medium_id()
        for mailing in self:
            if mailing.mailing_type == 'facebook' and (not mailing.medium_id or mailing.medium_id == self.env.ref('fw_odoo_facebook_marketing.utm_medium_facebook')):
                mailing.medium_id = self.env.ref('fw_odoo_facebook_marketing.utm_medium_facebook').id

