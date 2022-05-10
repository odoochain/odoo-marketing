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
    channel_group= fields.Many2many("channel_group.line")
    body_plaintext = fields.Text('Line Body')
    

    line_force_send = fields.Boolean(
        'Send Directly', help='Use at your own risks.')

    # mailing options
    mailing_type = fields.Selection(selection_add=[
        ('line', 'LINE')
    ], ondelete={'line': 'set default'})

    @api.model
    def default_get(self, fields):
        res = super(Mailing, self).default_get(fields)
        if fields is not None and 'keep_archives' in fields and res.get('mailing_type') == 'line':
            res['keep_archives'] = True
        if fields is not None and 'mailing_model_name' in fields and res.get('mailing_type') == 'line':
            res['mailing_model_name'] = 'line.list'
        return res

    


    def action_put_in_queue_line(self):
        res = self.action_put_in_queue()
        if self.line_force_send:
            self.action_send_mail()
        return res

    def action_send_now_line(self):
        for i in range(len(self.channel_group)):
            self.send_to_LINE(self.channel_group[i].Api_key,self.channel_group[i].channel,self.body_plaintext)
        return self.action_send_mail()


    def send_to_LINE(self, sender, recipients, msg):
        """
        send message to LINE
        @recipients text separate by enter
        """
        err = False
        if not recipients:
            err = _('no recipient')
            return err

        
        response = requests.post('https://notify-api.line.me/api/notify',
                                headers={
                                    'content-type': 'application/x-www-form-urlencoded',
                                    'Authorization': 'Bearer ' 
                                }, data={
                                    'message': msg
                                }
                                )
        j_rp = response.json()
        if j_rp.get('message',False) != 'ok':
            err = j_rp.get('message', _('unexpected error'))
            return err
        
        self._message_log(body=_('send notification to LINE: %s') % msg)
        return err
        

        

class channel(models.Model):
    _name="channel_group.line"
    _description="channel line"

    channel=fields.Char()
    Api_key = fields.Char()