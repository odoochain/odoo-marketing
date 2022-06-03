# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests




class fw_odoo_facebook_post(models.Model):
    _name = 'fw_odoo_facebook_post'
    _description = 'fw_odoo_facebook_post'
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name= fields.Char(required=True)
    fb_page_id = fields.Many2many("facebook.page_id")
    msg = fields.Char()
    image = fields.Char()
    
    ref = fields.Char(string="Reference", required=True, copy=False, readonly=True, default=lambda self: ('New'))  

    state = fields.Selection([                                          
        ('A-draft', 'Draft'),
        ('B-schedule', 'Scheduling'),
        ('C-done', 'Done'),
        ('D-cancel', 'Cancelled'),
        ], string='Status',  default='A-draft', tracking=True)

    

    schedule_date = fields.Datetime(string='Scheduled for', tracking=True)

    @api.model
    def create(self, vals):
        if vals.get('ref', ('New')) == ('New'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('fw_odoo_facebook_post') or ('New')
        record = super(fw_odoo_facebook_post, self).create(vals)
        return record

    def send_post(self):
        self.state= 'C-done'
        self.schedule_date= fields.Datetime.now()
        for i in range(len(self.fb_page_id)):
            if not self.image:
                payload = {
                'message' : self.msg,
                'access_token' : self.fb_page_id[i].facebook_access_token
                }
                post_url = 'https://graph.facebook.com/{}/feed'.format(self.fb_page_id[i].page_id) 
                r = requests.post(post_url, data=payload)
                print(r.text)
                return r
            elif not self.msg:
                image_url = 'https://graph.facebook.com/{}/photos'.format(self.fb_page_id[i].page_id)
                image_location = self.image
                img_payload = {
                'url' : image_location,
                'access_token': self.fb_page_id[i].facebook_access_token
                }
                r = requests.post(image_url, data=img_payload)
                print(r.text)
                return r
            else : 
                image_url = 'https://graph.facebook.com/{}/photos'.format(self.fb_page_id[i].page_id)
                image_location = self.image
                img_payload = {
                'message' : self.msg,
                'url' : image_location,
                'access_token': self.fb_page_id[i].facebook_access_token
                }
                r = requests.post(image_url, data=img_payload)
                print(r.text)
                return r
        
        
    

    def action_cancel(self):
        self.state='D-cancel'
        self.schedule_date=""

    def action_retry(self):
        self.state='A-draft'

    def action_schedule(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("fw_odoo_facebook_post.facebook_schedule_date_action")
        action['context'] = dict(self.env.context, default_fb_page_id=self.id)
        self.state='B-schedule'
        return action
    
    @api.model
    def action_send_schedule_facebook(self):
        mass_mailings = self.search([('state', '=', 'B-schedule'), '|', ('schedule_date', '<', fields.Datetime.now()), ('schedule_date', '=', False)])
        for mass_mailing in mass_mailings:
            mass_mailing.send_post()


class page_id(models.Model):
    _name="facebook.page_id"
    _description="Page Id"

    page_name = fields.Char()
    page_id = fields.Char(required=True)
    facebook_access_token = fields.Text(required=True) 

