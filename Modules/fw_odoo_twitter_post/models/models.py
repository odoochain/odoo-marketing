from odoo import models, fields, api
import requests
import tweepy
from requests_oauthlib import OAuth1Session


class fw_odoo_twitter_post(models.Model):
    _name = 'fw_odoo_twitter_post'
    _description = 'fw_odoo_twitter_post'
   
    tt_page_id = fields.Many2many("twitter.page_id")
    msg = fields.Char()
    image = fields.Char()

    name = fields.Char(string="Reference", required=True, copy=False, readonly=True, default=lambda self: ('New'))  


    @api.model
    def create(self, vals):
        if vals.get('name', ('New')) == ('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('fw_odoo_twitter_post') or ('New')
        record = super(fw_odoo_twitter_post, self).create(vals)
        return record

    def send_post(self):
        url_text= "https://api.twitter.com/1.1/statuses/update.json"
        params= {"status": self.msg}
        twitter = OAuth1Session(self.tt_page_id.CK,self.tt_page_id.CS,self.tt_page_id.AT,self.tt_page_id.AS)
        req = twitter.post(url_text, params=params)
        if req.status_code == 200:
            print("ok")
        else:
            print("Error: %d" % req.status_code)
    
  
        


class page_id(models.Model):
    _name="twitter.page_id"
    _description="Page Id"

    CK = fields.Char()
    CS = fields.Char()
    AT = fields.Char()
    AS = fields.Char()
