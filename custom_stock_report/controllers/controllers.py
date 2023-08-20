# -*- coding: utf-8 -*-
# from odoo import http


# class CustomStockReport(http.Controller):
#     @http.route('/custom_stock_report/custom_stock_report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_stock_report/custom_stock_report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_stock_report.listing', {
#             'root': '/custom_stock_report/custom_stock_report',
#             'objects': http.request.env['custom_stock_report.custom_stock_report'].search([]),
#         })

#     @http.route('/custom_stock_report/custom_stock_report/objects/<model("custom_stock_report.custom_stock_report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_stock_report.object', {
#             'object': obj
#         })
