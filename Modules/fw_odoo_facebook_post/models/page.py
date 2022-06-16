# -*- coding: utf-8 -*-
from odoo import models, fields, api

class page_id(models.Model):
    _name="facebook.page_id"
    _description="Page Id"

    page_name = fields.Char()
    page_id = fields.Char(required=True)
    facebook_access_token = fields.Text(required=True) 