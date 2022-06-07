# -*- coding: utf-8 -*-
# from odoo import http


# class FwOdooMarketing(http.Controller):
#     @http.route('/fw_odoo__marketing/fw_odoo__marketing/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fw_odoo__marketing/fw_odoo__marketing/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fw_odoo__marketing.listing', {
#             'root': '/fw_odoo__marketing/fw_odoo__marketing',
#             'objects': http.request.env['fw_odoo__marketing.fw_odoo__marketing'].search([]),
#         })

#     @http.route('/fw_odoo__marketing/fw_odoo__marketing/objects/<model("fw_odoo__marketing.fw_odoo__marketing"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fw_odoo__marketing.object', {
#             'object': obj
#         })
