# -*- coding: utf-8 -*-

from odoo import models, fields, api


class fw_odoo_marketing(models.Model):
    _inherit="fw_odoo_twitter_post"
    name=fields.Char()