from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order.line'

    @api.constrains('discount')
    def action_confirm(self):
        for rec in self:
            # Add your custom validation logic here
            if rec.discount <= 11:
                raise ValidationError("The discount must be greater than 11 to confirm the order.")


# # علشان امنع ان مايكونش فية اى سطور فاضية فى جدول المنتجات والزم المستخدم بوضع
# منتجات
# class SaleOrder(models.Model):
#     _inherit = 'sale.order'
#
#     def action_confirm(self):
#         for order in self:
#             # Add your custom validation logic here
#             if order.amount_total <= 0:
#                 raise ValidationError("The total amount must be greater than zero to confirm the order.")
#             # Example: Ensure all products have been specified
#             if any(line.product_id is None for line in order.order_line):
#                 raise ValidationError("All order lines must have a product specified.")
#
#         # Call the super method to proceed with the original confirm action
#         return super(SaleOrder, self).action_confirm()