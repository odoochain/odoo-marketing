# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class TwitterScheduleDate(models.TransientModel):
    _name = 'fw_odoo_telegram_marketing.schedule.date'
    _description = 'Twitter Scheduling'

    

    schedule_date = fields.Datetime(string='Scheduled for')
    telegram_id = fields.Many2one('mailing.mailing', required=True, ondelete='cascade')

    @api.constrains('schedule_date')
    def _check_schedule_date(self):
        for scheduler in self:
            if scheduler.schedule_date < fields.Datetime.now():
                raise ValidationError(_('Please select a date equal/or greater than the current date.'))

    def set_schedule_date(self):
        self.telegram_id.write({'schedule_date': self.schedule_date, 'state': 'in_queue'})
        