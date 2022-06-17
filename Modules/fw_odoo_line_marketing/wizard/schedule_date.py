# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class FWOdooLineScheduleDate(models.TransientModel):
    _name = 'fw_odoo_line_marketing.schedule.date'
    _description = 'LINE Scheduling' 

    schedule_date = fields.Datetime(string='Scheduled for')
    line_id = fields.Many2one('mailing.mailing', required=True, ondelete='cascade')

    @api.constrains('schedule_date')
    def _check_schedule_date(self):
        for scheduler in self:
            if scheduler.schedule_date < fields.Datetime.now():
                raise ValidationError(_('Please select a date equal/or greater than the current date.'))

    def set_schedule_date(self):
        self.line_id.write({'schedule_date': self.schedule_date, 'state': 'in_queue'})
        