# -*- coding: utf-8 -*-
# from odoo import http


# class Minimarketku(http.Controller):
#     @http.route('/minimarketku/minimarketku/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/minimarketku/minimarketku/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('minimarketku.listing', {
#             'root': '/minimarketku/minimarketku',
#             'objects': http.request.env['minimarketku.minimarketku'].search([]),
#         })

#     @http.route('/minimarketku/minimarketku/objects/<model("minimarketku.minimarketku"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('minimarketku.object', {
#             'object': obj
#         })
