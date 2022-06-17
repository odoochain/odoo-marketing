# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime
import logging

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.osv import expression

_logger = logging.getLogger(__name__)


class Mailing(models.Model):
    _inherit = 'mailing.mailing'

    @api.model
    def default_get(self, fields):
        res = super(Mailing, self).default_get(fields)
        if fields is not None and 'keep_archives' in fields and res.get('mailing_type') == 'line':
            res['keep_archives'] = True
        if fields is not None and 'mailing_model_name' in fields and res.get('mailing_type') == 'line':
            res['mailing_model_name'] = 'line.list'

        if res.get('mailing_type') == 'line':
           res['name'] = 'line marketing %s' % datetime.now().strftime('%d/%m/%Y')
           res['subject'] = res['name']
        return res

    # mailing options
    mailing_type = fields.Selection(selection_add=[
        ('line', 'LINE')
    ], ondelete={'line': 'set default'})

    line_group_ids = fields.Many2many('fw_bot_group', 'fw_bot_group_mailing', string='Groups')
    line_message = fields.Text(string='Message',help='limit 5000')

    def action_send_now_line(self):
        self.state= 'done'
        self.sent_date= fields.Datetime.now()

    @api.model
    def action_send_schedule_line(self):
        mass_mailings = self.search([('state', 'in', ('in_queue', 'sending')), ('mailing_type', '=', 'line'), '|', ('schedule_date', '<', fields.Datetime.now()), ('schedule_date', '=', False)])
        for mass_mailing in mass_mailings:
            mass_mailing.action_send_now_line()         

    def action_schedule_line(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("fw_odoo_line_marketing.line_schedule_date_action")
        action['context'] = dict(self.env.context, default_line_id=self.id)
        return action
        
    @api.depends('mailing_type')
    def _compute_medium_id(self):
        super(Mailing, self)._compute_medium_id()
        
        lineref = self.env.ref('fw_odoo_line_marketing.fw_odoo_utm_medium_line')
        for mailing in self:
            if mailing.mailing_type == 'line' and (not mailing.medium_id or mailing.medium_id == lineref):
                mailing.medium_id = lineref.id

