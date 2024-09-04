from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class owner(models.Model):
    _name = 'owner1'
    name = fields.Char(default='New')
    phone = fields.Char()
    address = fields.Text()
    living_area = fields.Char(string="Number of seats")
    facades = fields.Boolean()
    states = fields.Selection([
        ('draft', 'Draft'),
        ('ready', 'Ready'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
        ('closed', 'Closed')
    ], default='draft')
    age = fields.Integer()
    prop_ids = fields.One2many('allow1', 'ow_id', string="Owner User")
    actived = fields.Boolean()
    customer_id = fields.Many2one('res.partner', string='Customer', )

    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)', 'The expected name must be UNIQUE.'),
        ('unique_phone', 'UNIQUE(phone)', 'The expected phone must be UNIQUE.')
    ]

    def action_draft(self):
        for rec in self:
            print("inside draft action")
            rec.states = 'draft'

    def action_ready(self):
        for rec in self:
            print("inside ready action")
            rec.states = 'ready'

    def action_done(self):
        for rec in self:
            print("inside done action")
            rec.states = 'done'

    def action_closed(self):
        for rec in self:
            print("inside closed action")
            rec.states = 'closed'

    def action_cancel(self):
        for rec in self:
            print("inside Cancel action")
            rec.write({
                'states': 'cancel'

            })

    @api.constrains('living_area')
    def _check_living_area(self):
        for record in self:
            if record.living_area and not re.match(r'^\d{9,}$', record.living_area):
                raise ValidationError("The Number of seats	 number must be exactly 9 digits.")


    @api.constrains('age')
    def _check_age(self):
        if self.age <= 10 or self.age >= 15:
            raise ValidationError("please insert age between 10 to  15. ")
