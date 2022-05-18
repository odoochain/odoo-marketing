from odoo import models, fields, api
import requests
import tweepy



class fw_odoo_twitter_post(models.Model):
    _name = 'fw_odoo_twitter_post'
    _description = 'fw_odoo_twitter_post'
   
    tt_page_id = fields.Many2many("twitter.page_id")
    msg = fields.Char()
    image = fields.Char()

    CK = fields.Char(required=True)
    CS = fields.Char(required=True)
    AT = fields.Char(required=True)
    AS = fields.Char(required=True)
    name = fields.Char(string="Reference", required=True, copy=False, readonly=True, default=lambda self: ('New'))  


    @api.model
    def create(self, vals):
        if vals.get('name', ('New')) == ('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('fw_odoo_twitter_post') or ('New')
        record = super(fw_odoo_twitter_post, self).create(vals)
        return record

    def send_post(self):
        # Authenticate to Twitter
        auth = tweepy.OAuthHandler(self.CK, self.CS)
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

  
        




