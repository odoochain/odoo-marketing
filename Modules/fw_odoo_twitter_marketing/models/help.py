from odoo import models, fields, api

class telegram_help(models.Model):
    _name="telegram.help"
    _description="Telegram help"

    name=fields.Char()