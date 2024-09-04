# -*- coding: utf-8 -*-
{
    'name': "allow",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'hr_contract', 'hr', 'l10n_sa', 'l10n_sa_invoice', 'sale_management', 'sale', 'account'],
    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/open_academy.xml',
        'views/owner.xml',
        'views/addfields.xml',
        'views/custom_invoice_report.xml',
        'views/editeqr.xml',
        'views/validation_on_sales.xml',
        'reports/report_owner.xml',
        'reports/report_allow.xml',
        'reports/create_header&Footeer.xml.xml',
        'reports/sale_report.xml',
    ],
}
