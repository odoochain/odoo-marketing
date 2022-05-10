# -*- coding: utf-8 -*-
# from odoo import http


# class FwOdooTelegramMarketing(http.Controller):
#     @http.route('/fw_odoo_telegram_marketing/fw_odoo_telegram_marketing/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fw_odoo_telegram_marketing/fw_odoo_telegram_marketing/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fw_odoo_telegram_marketing.listing', {
#             'root': '/fw_odoo_telegram_marketing/fw_odoo_telegram_marketing',
#             'objects': http.request.env['fw_odoo_telegram_marketing.fw_odoo_telegram_marketing'].search([]),
#         })

#     @http.route('/fw_odoo_telegram_marketing/fw_odoo_telegram_marketing/objects/<model("fw_odoo_telegram_marketing.fw_odoo_telegram_marketing"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fw_odoo_telegram_marketing.object', {
#             'object': obj
#         })
