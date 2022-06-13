from odoo import models, fields, api, _ 
import html2text
import urllib.parse as parse
import logging
_logger = logging.getLogger(__name__)
"""
class SendMultipleContactMessage(models.TransientModel):
    _name = 'whatsapp.wizard.multiple.contact'

    partner_id = fields.Many2one('res.partner', string="Recipient")
    mobile = fields.Char(required=True, string="Contact Number")
    message = fields.Text(string="Message", required=True)

    def send_multiple_contact_message(self):
        if self.message and self.mobile:
            message_string = ''
            message = self.message.split(' ')
            for msg in message:
                message_string = message_string + msg + ' '
            message_string = parse.quote(message_string)
            html2text.html2text(message_string)
            message_string = message_string[:(len(message_string) - 3)]
            number = self.mobile
            link = "https://web.whatsapp.com/send?phone=" + number
            send_msg = {
                'type': 'ir.actions.act_url',
                'url': link + "&text=" + message_string,
                'target': 'new',
                'res_id': self.id,
            }
            return send_msg

class SendContactMessage(models.TransientModel):
    _name = 'whatsapp.wizard.contact'

    user_id = fields.Many2one('res.partner', string="Recipient Name", default=lambda self: self.env[self._context.get('active_model')].browse(self.env.context.get('active_ids')))
    mobile_number = fields.Char(related='user_id.mobile', required=True)
    message = fields.Text(string="Message", required=True)

    def send_custom_contact_message(self):
        if self.message:
            message_string = ''
            message = self.message.split(' ')
            for msg in message:
                message_string = message_string + msg + '%20'
            message_string = message_string[:(len(message_string) - 3)]
            number = self.user_id.mobile
            link = "https://web.whatsapp.com/send?phone=" + number
            send_msg = {
                'type': 'ir.actions.act_url',
                'url': link + "&text=" + message_string,
                'target': 'new',
                'res_id': self.id,
            }
            return send_msg
 
"""


class WhatsappSendMessage(models.TransientModel):
    _name = 'whatsapp.message.wizard'

    user_id = fields.Many2one('res.partner', string="Recipient")
    mobile_number = fields.Char( related='user_id.mobile', required=True)
    message = fields.Text(string="Message")
    model = fields.Char('mail.template.model_id')
    template_id = fields.Many2one('mail.template', 'Use template', index=True,)


    def send_message(self):
        if self.message and self.mobile_number:
            message_string = ''
            message = self.message.split(' ')
            for msg in message:
                message_string = message_string + msg + '%20'
            message_string = message_string[:(len(message_string) - 3)]
            number = self.user_id.mobile
            link = "https://web.whatsapp.com/send?phone=" + number
            send_msg = {
                'type': 'ir.actions.act_url',
                'url': link + "&text=" + message_string,
                'target': 'new',
                'res_id': self.id,
            }
            return send_msg

            