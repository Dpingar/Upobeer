# -*- coding: utf-8 -*-
from odoo import http

# class Upobeer(http.Controller):
#     @http.route('/upobeer/upobeer/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/upobeer/upobeer/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('upobeer.listing', {
#             'root': '/upobeer/upobeer',
#             'objects': http.request.env['upobeer.upobeer'].search([]),
#         })

#     @http.route('/upobeer/upobeer/objects/<model("upobeer.upobeer"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('upobeer.object', {
#             'object': obj
#         })