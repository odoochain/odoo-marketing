# -*- coding: utf-8 -*-

from odoo import models, fields, api
#import json
#from facebook import GraphAPI
import requests


class fw_odoo_facebook_post(models.Model):
    _name = 'fw_odoo_facebook_post'
    _description = 'fw_odoo_facebook_post'
   
    fb_page_id = fields.Many2many("facebook.page_id")
    facebook_access_token = fields.Text() 
    msg = fields.Char()

    

    def send_post(self):
        payload = {
        'message' : self.msg,
        'access_token' : self.facebook_access_token
        }
        post_url = 'https://graph.facebook.com/{}/feed'.format(self.fb_page_id.page_id) 
        r = requests.post(post_url, data=payload)
        print(r.text) 
        return r

#on ne peut pas mettre deux fois le même post sur la même page

class page_id(models.Model):
    _name="facebook.page_id"
    _description="Page Id"

    page_id = fields.Char()


