# -*- coding: utf-8 -*-

from odoo import models, fields, api


class fw_odoo_twitter(models.Model):
    _inherit="fw_odoo_twitter_post"

    mailing_type = fields.Selection([
        ('twitter', 'Twitter')
    ], default='twitter')