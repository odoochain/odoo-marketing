# -*- coding: utf-8 -*-
from odoo import models, fields, api
import tweepy

class fw_odoo_twitter_post(models.Model):
    _name = 'fw_odoo_twitter_post'
    _description = 'fw_odoo_twitter_post'
    _inherit = ["mail.thread", "mail.activity.mixin"]

    schedule_date = fields.Datetime(string='Scheduled for', tracking=True)
    msg = fields.Char()
    image = fields.Char()

    CK = fields.Char(required=True)
    CS = fields.Char(required=True)
    AT = fields.Char(required=True)
    AS = fields.Char(required=True)
    reference = fields.Char(string="Reference", required=True, copy=False, readonly=True, default=lambda self: ('New'))  
    name=fields.Char(required=True)

    state = fields.Selection([                                          
        ('A-draft', 'Draft'),
        ('B-schedule', 'Scheduling'),
        ('C-done', 'Done'),
        ('D-cancel', 'Cancelled'),
        ], string='Status',  default='A-draft', tracking=True)


    @api.model
    def create(self, vals):
        if vals.get('reference', ('New')) == ('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('fw_odoo_twitter_post') or ('New')
        record = super(fw_odoo_twitter_post, self).create(vals)
        return record

    def send_post(self):
        # Authenticate to Twitter
        self.state= 'C-done'
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
        

  
    def action_schedule(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("fw_odoo_twitter_post.twitter_schedule_date_action")
        action['context'] = dict(self.env.context, default_tt_page_id=self.id)
        self.state='B-schedule'
        return action

    def action_cancel(self):
        self.state='D-cancel'
        self.schedule_date=""

    def action_retry(self):
        self.state='A-draft'

    
    @api.model
    def action_send_schedule_twitter(self):
        mass_mailings = self.search([('state', '=', 'B-schedule'), '|', ('schedule_date', '<', fields.Datetime.now()), ('schedule_date', '=', False)])
        for mass_mailing in mass_mailings:
            mass_mailing.send_post()