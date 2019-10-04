# -*- coding: utf-8 -*-
from odoo import http

# class AsLattiPayroll(http.Controller):
#     @http.route('/as_latti_payroll/as_latti_payroll/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/as_latti_payroll/as_latti_payroll/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('as_latti_payroll.listing', {
#             'root': '/as_latti_payroll/as_latti_payroll',
#             'objects': http.request.env['as_latti_payroll.as_latti_payroll'].search([]),
#         })

#     @http.route('/as_latti_payroll/as_latti_payroll/objects/<model("as_latti_payroll.as_latti_payroll"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('as_latti_payroll.object', {
#             'object': obj
#         })