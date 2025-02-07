# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
from datetime import datetime
from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.osv import expression
import requests

_logger = logging.getLogger(__name__)

class Mailing(models.Model):
    _inherit = 'mailing.mailing'

    channel_group= fields.Many2many("channel_group.telegram")
    body_plaintext = fields.Text('Telegram Body')
    image = fields.Char()
    schedule_date = fields.Datetime(string='Scheduled for')
          
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
        if res.get('mailing_type') == 'telegram':
           res['name'] = 'telegram marketing %s' % datetime.now().strftime('%d/%m/%Y')
           res['subject'] = res['name']
        return res

    def action_send_now_telegram(self):
        for i in range(len(self.channel_group)):
            self.send_to_tg(self.channel_group[i].Api_key,self.channel_group[i].channel,self.image,self.body_plaintext)
        return self.action_send_mail()

    @api.model
    def action_send_schedule_telegram(self):
        mass_mailings = self.search([('state', 'in', ('in_queue', 'sending')), ('mailing_type', '=', 'telegram'),'|', ('schedule_date', '<', fields.Datetime.now()), ('schedule_date', '=', False)])
        for mass_mailing in mass_mailings:
            mass_mailing.action_send_now_telegram()
            
    @api.depends('mailing_type')
    def _compute_medium_id(self):
        super(Mailing, self)._compute_medium_id()
        for mailing in self:
            if mailing.mailing_type == 'telegram' and (not mailing.medium_id or mailing.medium_id == self.env.ref('fw_odoo_telegram_marketing.utm_medium_telegram')):
                mailing.medium_id = self.env.ref('fw_odoo_telegram_marketing.utm_medium_telegram').id
            
                 
    def send_to_tg(self, sender, recipients,img, msg):
        """
        send message to tg 
        @recipients text separate by enter
        """

        err = False
        if not recipients:
            err = _('no recipient')
            return err 
        if img==False:
            img="" 
        send_text = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&parse_mode=markdown&text='
        response = requests.get(send_text % (sender, recipients)+"[​​​​​​​​​​​]("+img+")"+msg)
  
    
        j_rp = response.json()
        if not j_rp.get('ok',False):
            err = j_rp.get('description', _('unexpected error'))
            return err
        

        self._message_log(body=_('send notification to telegram: %s') % msg)                                   
        return err

    def action_schedule_telegram(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("fw_odoo_telegram_marketing.telegram_schedule_date_action")
        action['context'] = dict(self.env.context, default_telegram_id=self.id)
        return action