# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CustomCRMTimesheet(models.Model):
    _name = 'custom.crm.timesheet'
    _description = 'Custom CRM Timesheet'

    name = fields.Char(string="Description", required=True)
    lead_id = fields.Many2one('crm.lead', string="Related Opportunity", required=True, ondelete='cascade')
    user_id = fields.Many2one('res.users', string="Related User",
                              default=lambda self: self.env.user, required=True)

    def _get_default_employee(self):
        return self.env.user.employee_id.id

    employee_id = fields.Many2one('hr.employee', string="Employee", default=_get_default_employee)
    date = fields.Date(string="Date", default=fields.Date.context_today)
    duration = fields.Float(string="Duration (Hours)", required=True)

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        """ کاربران عادی فقط تایم‌شیت خودشان را ببینند، ادمین‌ها همه را ببینند """
        if not self.env.user.has_group('base.group_system'):
            args.append(('user_id', '=', self.env.user.id))
        return super().search(args, offset, limit, order, count)


class CRMLead(models.Model):
    _inherit = 'crm.lead'

    timesheet_ids = fields.One2many('custom.crm.timesheet', 'lead_id', string="Timesheets")
