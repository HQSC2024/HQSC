# -*- coding: utf-8 -*-
{
    'name': "invoice_print_customize",
    'version': '17.0.1.0.1',
    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Amr Wahba",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'l10n_sa', 'l10n_gcc_invoice', 'web'],

    # always loaded
    'data': [
        'reports/paperformat_custom.xml',
        'reports/report_invoice_inherit.xml',
    ],

}
