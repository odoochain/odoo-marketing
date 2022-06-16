# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.osv import expression

_logger = logging.getLogger(__name__)

class channel(models.Model):
    _name="channel_group.telegram"
    _description="channel telegram"

    channel=fields.Char()
    Api_key = fields.Char()