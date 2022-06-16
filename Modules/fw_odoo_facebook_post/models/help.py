# -*- coding: utf-8 -*-
from odoo import models, fields, api

class facebook_help(models.Model):
    _name="facebook.help"
    _description="Facebook help"

    name=fields.Char()