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

    def action_put_in_queue_line(self):
        pass

    def action_send_now_line(self):
        pass

    def action_test(self):
        if self.mailing_type == 'line':
            ctx = dict(self.env.context, default_mailing_id=self.id)
            return {
                'name': _('Test LINE marketing'),
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'mailing.line.test',
                'target': 'new',
                'context': ctx,
            }
        return super(Mailing, self).action_test()    

    def action_send_mail(self, res_ids=None):
        mass_line = self.filtered(lambda m: m.mailing_type == 'line')
        if mass_line:
            mass_line.action_send_line(res_ids=res_ids)
        return super(Mailing, self - mass_line).action_send_mail(res_ids=res_ids)

    def _parse_mailing_domain(self):
        self.ensure_one()
        try:
            mailing_domain = literal_eval(self.mailing_domain)
        except Exception:
            mailing_domain = [('id', 'in', [])]
        return mailing_domain

    def _get_recipients(self):
        mailing_domain = self._parse_mailing_domain()
        res_ids = self.env[self.mailing_model_real].search(mailing_domain).ids

        # randomly choose a fragment
        if self.contact_ab_pc < 100:
            contact_nbr = self.env[self.mailing_model_real].search_count(mailing_domain)
            topick = int(contact_nbr / 100.0 * self.contact_ab_pc)
            if self.campaign_id and self.unique_ab_testing:
                already_mailed = self.campaign_id._get_mailing_recipients()[self.campaign_id.id]
            else:
                already_mailed = set([])
            remaining = set(res_ids).difference(already_mailed)
            if topick > len(remaining):
                topick = len(remaining)
            res_ids = random.sample(remaining, topick)
        return res_ids

    def _get_remaining_recipients(self):
        res_ids = self._get_recipients()
        already_mailed = self.env['mailing.trace'].search_read([
            ('model', '=', self.mailing_model_real),
            ('res_id', 'in', res_ids),
            ('mass_mailing_id', '=', self.id)], ['res_id'])
        done_res_ids = {record['res_id'] for record in already_mailed}
        return [rid for rid in res_ids if rid not in done_res_ids]

    def action_send_line(self, res_ids=None):
        for mailing in self:
            if not res_ids:
                res_ids = mailing._get_remaining_recipients()
            if not res_ids:
                raise UserError(_('There are no recipients selected.'))

            #composer = self.env['sms.composer'].with_context(active_id=False).create(mailing._send_sms_get_composer_values(res_ids))
            #composer._action_send_sms()
            mailing.write({'state': 'done', 'sent_date': fields.Datetime.now()})
        return True
