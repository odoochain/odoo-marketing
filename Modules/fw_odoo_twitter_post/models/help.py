from odoo import models, fields, api

class twitter_help(models.Model):
    _name="twitter.help"
    _description="Twitter help"

    name=fields.Char()