from odoo import models, fields, api
from odoo.exceptions import ValidationError


class allow(models.Model):
    _name = 'allow1'
    _description = 'Hello World'
    # اضافة الشاطر
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _rec_name = "first"
    first = fields.Char(required=True, help='insert first', default='New', size=10, tracking=True)
    namee = fields.Char(tracking=True, readonly=False)
    descraption = fields.Text()
    pstcode = fields.Char()
    numb = fields.Char()
    expected_price = fields.Float()
    selling_price = fields.Float(digits=(0, 5))
    bedrooms = fields.Integer()
    living_area = fields.Integer(string="Number of seats")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    date_of_birth = fields.Date()
    gardean_area = fields.Integer()
    sales_date = fields.Date()
    is_late = fields.Boolean()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ], default='north')
    col1 = fields.Float()
    col2 = fields.Float()
    result = fields.Float()
    computed = fields.Float(compute='_value_computed', readonly=True, store=True)
    total = fields.Float(compute="_compute_total", inverse="_inverse_total", store=True)
    # To display data in the field, provided that the status is done, and any other status if it is draft does not appear in the
    # selection, this is done through the domain on the status field.
    ow_id = fields.Many2one('owner1', string="owner1",  domain="[('states', '=', 'done')]")
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    customer_id = fields.Many2one('res.partner', string='Customer', )

    @api.depends("expected_price")
    def _compute_total(self):
        for record in self:
            record.total = record.selling_price * record.expected_price

    def _inverse_total(self):
        for record in self:
            if record.selling_price != 0.0:
                record.expected_price = record.total / record.selling_price

    @api.onchange('col1')
    def on_change_value(self):
        self.result = self.col1 + self.col2



    @api.depends('result')
    def _value_computed(self):
        for record in self:
            record.computed = float(record.result) / 100


    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for record in self:
            if record.date_of_birth and record.date_of_birth >= fields.Date.today():
                raise ValidationError("The end date cannot be set in the past")


    def check_sales_date(self):
        print("inside check")



