# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

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
        return res

    # mailing options
    mailing_type = fields.Selection(selection_add=[
        ('line', 'LINE')
    ], ondelete={'line': 'set default'})


    def action_put_in_queue_line(self):
        pass

    def action_send_now_line(self):
        pass