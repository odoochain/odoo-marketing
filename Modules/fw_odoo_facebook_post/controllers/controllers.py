# -*- coding: utf-8 -*-
# from odoo import http


# class FwOdooFacebookPost(http.Controller):
#     @http.route('/fw_odoo_facebook_post/fw_odoo_facebook_post/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fw_odoo_facebook_post/fw_odoo_facebook_post/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fw_odoo_facebook_post.listing', {
#             'root': '/fw_odoo_facebook_post/fw_odoo_facebook_post',
#             'objects': http.request.env['fw_odoo_facebook_post.fw_odoo_facebook_post'].search([]),
#         })

#     @http.route('/fw_odoo_facebook_post/fw_odoo_facebook_post/objects/<model("fw_odoo_facebook_post.fw_odoo_facebook_post"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fw_odoo_facebook_post.object', {
#             'object': obj
#         })
