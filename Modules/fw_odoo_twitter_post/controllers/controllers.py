# -*- coding: utf-8 -*-
# from odoo import http


# class FwOdooTwitterPost(http.Controller):
#     @http.route('/fw_odoo_twitter_post/fw_odoo_twitter_post/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fw_odoo_twitter_post/fw_odoo_twitter_post/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fw_odoo_twitter_post.listing', {
#             'root': '/fw_odoo_twitter_post/fw_odoo_twitter_post',
#             'objects': http.request.env['fw_odoo_twitter_post.fw_odoo_twitter_post'].search([]),
#         })

#     @http.route('/fw_odoo_twitter_post/fw_odoo_twitter_post/objects/<model("fw_odoo_twitter_post.fw_odoo_twitter_post"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fw_odoo_twitter_post.object', {
#             'object': obj
#         })
