# -*- coding: utf-8 -*-

from odoo import models, fields, api


class fw_odoo_facebook(models.Model):
    _inherit="fw_odoo_facebook_post"
    

    mailing_type = fields.Selection([
        ('facebook', 'Facebook')
    ], default='facebook')