from odoo import models, fields, api


class HrContractFileds(models.Model):
    _inherit = 'hr.employee'

    id_userss = fields.Many2one('hr.employee', string="employeess")
    nature_work_allow = fields.Integer(string='Nature Of Work Allowance')
    cost_living_allow = fields.Integer(string='Cost Of Living Allowance')
    ticket_allow = fields.Integer(string='Ticket Allowance')
    vacation_allow = fields.Integer(string='Vacation Allowance')
    allowance_1 = fields.Integer(string='Allowance 1')
    allowance_2 = fields.Integer(string='Allowance 2')


#class hremployeefields(models.Model):
#     _inherit = 'hr.department'
#
#
# id_departmentss = fields.Many2one('hr.department', string="departmentss")
