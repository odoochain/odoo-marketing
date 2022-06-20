from odoo import models, fields, api

class facebook_help(models.Model):
    _name="facebook.help"
    _description="facebook help"

    name=fields.Char()