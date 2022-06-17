# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class FWOdooLineSettings(models.TransientModel):
    _name = 'fw_odoo_line_marketing_settings'
    _description = 'LINE Marketing settings' 

    access_token = fields.Text('LINE Channel access token')

    @api.model
    def get_access_token(self):
        return self.env['ir.config_parameter'].get_param('line-access-token')

    def save_settings(self):
        self.env['ir.config_parameter'].set_param('line-access-token', self.access_token)
        