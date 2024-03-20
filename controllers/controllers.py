# -*- coding: utf-8 -*-
# from odoo import http


# class CatBreeder(http.Controller):
#     @http.route('/cat_breeder/cat_breeder', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cat_breeder/cat_breeder/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cat_breeder.listing', {
#             'root': '/cat_breeder/cat_breeder',
#             'objects': http.request.env['cat_breeder.cat_breeder'].search([]),
#         })

#     @http.route('/cat_breeder/cat_breeder/objects/<model("cat_breeder.cat_breeder"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cat_breeder.object', {
#             'object': obj
#         })

