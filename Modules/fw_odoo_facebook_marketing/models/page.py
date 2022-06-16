# -*- coding: utf-8 -*-
import logging

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.osv import expression

_logger = logging.getLogger(__name__)

class page_id(models.Model):
    _name="facebook.page_id"
    _description="Page Id"

    page_name = fields.Char()
    page_id = fields.Char(required=True)
    facebook_access_token = fields.Text(required=True) 

    