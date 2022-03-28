# -*- coding: utf-8 -*-
# from odoo import http


# class Handphoneorganizer(http.Controller):
#     @http.route('/handphoneorganizer/handphoneorganizer/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/handphoneorganizer/handphoneorganizer/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('handphoneorganizer.listing', {
#             'root': '/handphoneorganizer/handphoneorganizer',
#             'objects': http.request.env['handphoneorganizer.handphoneorganizer'].search([]),
#         })

#     @http.route('/handphoneorganizer/handphoneorganizer/objects/<model("handphoneorganizer.handphoneorganizer"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('handphoneorganizer.object', {
#             'object': obj
#         })
