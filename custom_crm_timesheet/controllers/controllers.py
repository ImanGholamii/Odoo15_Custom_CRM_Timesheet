# -*- coding: utf-8 -*-
# from odoo import http


# class CustomCrmTimesheet(http.Controller):
#     @http.route('/custom_crm_timesheet/custom_crm_timesheet', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_crm_timesheet/custom_crm_timesheet/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_crm_timesheet.listing', {
#             'root': '/custom_crm_timesheet/custom_crm_timesheet',
#             'objects': http.request.env['custom_crm_timesheet.custom_crm_timesheet'].search([]),
#         })

#     @http.route('/custom_crm_timesheet/custom_crm_timesheet/objects/<model("custom_crm_timesheet.custom_crm_timesheet"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_crm_timesheet.object', {
#             'object': obj
#         })
