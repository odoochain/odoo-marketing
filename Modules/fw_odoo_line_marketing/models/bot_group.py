# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.osv import expression

_logger = logging.getLogger(__name__)

class FWBotGroup(models.Model):
    _name = 'fw_bot_group'

    name = fields.Char('group name')
    date_join = fields.Datetime('Date bot join to group')
    group_id = fields.Char('group id')