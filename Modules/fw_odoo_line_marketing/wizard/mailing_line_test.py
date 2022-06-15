# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, exceptions, fields, models, _
from odoo.addons.phone_validation.tools import phone_validation


class MassSMSTest(models.TransientModel):
    _name = 'mailing.line.test'
    _description = 'Test LINE Mailing'

    group_id = fields.Many2one('fw_bot_group', string='Group', required=True)

    def action_send_line(self):
        # self.ensure_one()
        # numbers = [number.strip() for number in self.numbers.split(',')]
        # sanitize_res = phone_validation.phone_sanitize_numbers_w_record(numbers, self.env.user)
        # sanitized_numbers = [info['sanitized'] for info in sanitize_res.values() if info['sanitized']]
        # invalid_numbers = [number for number, info in sanitize_res.items() if info['code']]
        # if invalid_numbers:
        #     raise exceptions.UserError(_('Following numbers are not correctly encoded: %s, example : "+32 495 85 85 77, +33 545 55 55 55"', repr(invalid_numbers)))
        
        # record = self.env[self.mailing_id.mailing_model_real].search([], limit=1)
        # body = self.mailing_id.body_plaintext
        # if record:
        #     # Returns a proper error if there is a syntax error with jinja
        #     body = self.env['mail.render.mixin']._render_template(body, self.mailing_id.mailing_model_real, record.ids)[record.id]

        # self.env['line.api']._send_line_batch([{
        #     'res_id': 0,
        #     'number': number,
        #     'content': body,
        # } for number in sanitized_numbers])
        return True
