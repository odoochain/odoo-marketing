# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.osv import expression
import requests
import html2text
import urllib.parse as parse
_logger = logging.getLogger(__name__)


class Mailing(models.Model):
    _inherit = 'mailing.mailing'
    
    mobile_group = fields.Many2many("whatsapp.group")
    message = fields.Text('whatsapp Body')
    

    whatsapp_force_send = fields.Boolean(
        'Send Directly', help='Use at your own risks.')

    # mailing options
    mailing_type = fields.Selection(selection_add=[
        ('whatsapp', 'whatsapp')
    ], ondelete={'whatsapp': 'set default'})

    @api.model
    def default_get(self, fields):
        res = super(Mailing, self).default_get(fields)
        if fields is not None and 'keep_archives' in fields and res.get('mailing_type') == 'whatsapp':
            res['keep_archives'] = True
        if fields is not None and 'mailing_model_name' in fields and res.get('mailing_type') == 'whatsapp':
            res['mailing_model_name'] = 'whatsapp.list'
        return res

   

    def action_put_in_queue_whatsapp(self):
        res = self.action_put_in_queue()
        if self.whatsapp_force_send:
            self.action_send_mail()
        return res

    def action_send_now_whatsapp(self):
        for i in range(len(self.mobile_group)):
            if self.message and self.mobile_group[i].mobile:
                self.action_send_mail()
                message_string = ''
                message = self.message.split(' ')
                for msg in message:
                    message_string = message_string + msg + ' '
                message_string = parse.quote(message_string)
                html2text.html2text(message_string)
                message_string = message_string[:(len(message_string) - 3)]
                number = self.mobile_group[i].mobile
                link = "https://web.whatsapp.com/send?phone=" + number
                send_msg = {
                    'type': 'ir.actions.act_url',
                    'url': link + "&text=" + message_string,
                    'target': 'new',
                    'res_id': self.id,
                }
                return send_msg
"""
    def send_direct_message(self):
        record_phone = self.partner_id.mobile
        if not record_phone:
            view = self.env.ref('odoo_whatsapp_integration.warn_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = "Please add a mobile number!"
            return {
                'name': 'Mobile Number Field Empty',
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'display.error.message',
                'views': [(view.id, 'form')],
                'view_id': view.id,
                'target': 'new',
                'context': context
            }
        if not record_phone[0] == "+":
            view = self.env.ref('odoo_whatsapp_integration.warn_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = "No Country Code! Please add a valid mobile number along with country code!"
            return {
                'name': 'Invalid Mobile Number',
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'display.error.message',
                'views': [(view.id, 'form')],
                'view_id': view.id,
                'target': 'new',
                'context': context
            }
        else:
            prods = ""
            for rec in self:
                for id in rec.invoice_line_ids:
                            prods = prods + "*" +str(id.product_id.name) + " : " + str(id.quantity) + "* \n"

            custom_msg = "Hello *{}*, your Invoice *{}* with amount *{} {}* is ready. \nYour invoice contains following items:\n {}".format(str(self.partner_id.name),str(self.name),str(self.currency_id.symbol),str(self.amount_total),prods)
            ph_no = [number for number in record_phone if number.isnumeric()]
            ph_no = "".join(ph_no)
            ph_no = "+" + ph_no

            link = "https://web.whatsapp.com/send?phone=" + ph_no
            message_string = parse.quote(custom_msg)

            url_id = link + "&text=" + message_string
            return {
                'type': 'ir.actions.act_url',
                'url': url_id,
                'target': 'new',
                'res_id': self.id,
            }
 """       
class group(models.Model):
    _name="whatsapp.group"
    _description ="whatsapp group"
    mobile = fields.Char()
    
        
    
