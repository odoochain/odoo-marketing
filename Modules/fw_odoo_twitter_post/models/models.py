from odoo import models, fields, api
import requests
import tweepy



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
        return True
    

        


class page_id(models.Model):
    _name="twitter.page_id"
    _description="Page Id"

    page_name = fields.Char()
    page_id = fields.Char(required=True)
    twitter_access_token = fields.Text(required=True) 
