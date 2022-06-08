# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.osv import expression
import requests
import re
import tweepy


_logger = logging.getLogger(__name__)


class Mailing(models.Model):
    _inherit = 'mailing.mailing'

    schedule_date = fields.Datetime(string='Scheduled for', tracking=True)
    msg = fields.Char()
    image = fields.Char()

    CK = fields.Char()
    CS = fields.Char()
    AT = fields.Char()
    AS = fields.Char()

    twitter_force_send = fields.Boolean(
        'Send Directly', help='Use at your own risks.')

    # mailing options
    mailing_type = fields.Selection(selection_add=[
        ('twitter', 'Twitter')
    ], ondelete={'twitter': 'set default'})

    @api.model
    def default_get(self, fields):
        res = super(Mailing, self).default_get(fields)
        if fields is not None and 'keep_archives' in fields and res.get('mailing_type') == 'twitter':
            res['keep_archives'] = True
        if fields is not None and 'mailing_model_name' in fields and res.get('mailing_type') == 'twitter':
            res['mailing_model_name'] = 'twitter.list'
        return res

   

    def action_put_in_queue_twitter(self):
        res = self.action_put_in_queue()
        if self.twitter_force_send:
            self.action_send_mail()
        return res


    def action_send_now_twitter(self):
        # Authenticate to Twitter
        self.state= 'done'
        self.schedule_date= fields.Datetime.now()
        auth = tweepy.OAuth1UserHandler(self.CK, self.CS)
        auth.set_access_token(self.AT, self.AS)

        # Create API object
        api = tweepy.API(auth)
        
        # Create a tweet
        tweet_text= self.msg
        if tweet_text==False:
            tweet_text=""
        if self.image==False:
            api.update_status(status=tweet_text)
        else:
            media = api.media_upload(self.image)
            api.update_status(status=tweet_text, media_ids=[media.media_id])

    @api.model
    def action_send_schedule_twitter(self):
        mass_mailings = self.search([('state', 'in', ('in_queue', 'sending')), '|', ('schedule_date', '<', fields.Datetime.now()), ('schedule_date', '=', False)])
        for mass_mailing in mass_mailings:
            mass_mailing.action_send_now_twitter()
            
             
        

    def action_schedule_twitter(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("fw_odoo_twitter_marketing.twitter_schedule_date_action")
        action['context'] = dict(self.env.context, default_twitter_id=self.id)
        return action
        



    

    