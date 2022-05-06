# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.osv import expression
import requests

_logger = logging.getLogger(__name__)


class Mailing(models.Model):
    _inherit = 'mailing.mailing'
    channel_group= fields.Many2many("channel_group.telegram")
    body_plaintext = fields.Text('Telegram Body')
    

    telegram_force_send = fields.Boolean(
        'Send Directly', help='Use at your own risks.')

    # mailing options
    mailing_type = fields.Selection(selection_add=[
        ('telegram', 'Telegram')
    ], ondelete={'telegram': 'set default'})

    @api.model
    def default_get(self, fields):
        res = super(Mailing, self).default_get(fields)
        if fields is not None and 'keep_archives' in fields and res.get('mailing_type') == 'telegram':
            res['keep_archives'] = True
        if fields is not None and 'mailing_model_name' in fields and res.get('mailing_type') == 'telegram':
            res['mailing_model_name'] = 'telegram.list'
        return res

   


    def action_put_in_queue_telegram(self):
        res = self.action_put_in_queue()
        if self.telegram_force_send:
            self.action_send_mail()
        return res

    def action_send_now_telegram(self):
        for i in range(len(self.channel_group)):
            self.send_to_tg(self.channel_group[i].Api_key,self.channel_group[i].channel,self.body_plaintext)
        return self.action_send_mail()

    def send_to_tg(self, sender, recipients, msg):
        """
        send message to tg 
        @recipients text separate by enter
        """

        err = False
        if not recipients:
            err = _('no recipient')
            return err

        send_text = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text='

        
        response = requests.get(send_text % (
                sender, recipients) +
                msg
            )
        j_rp = response.json()
        if not j_rp.get('ok',False):
            err = j_rp.get('description', _('unexpected error'))
            return err

        self._message_log(body=_('send notification to telegram: %s') % msg)                                   
        return err

       

        
class channel(models.Model):
    _name="channel_group.telegram"
    _description="channel telegram"

    channel=fields.Char()
    Api_key = fields.Char()
    
   
    