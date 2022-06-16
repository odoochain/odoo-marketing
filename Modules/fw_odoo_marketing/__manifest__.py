# -*- coding: utf-8 -*-
{
    'name': "Statistic Marketing",

    'summary': """show mail, sms marketing statistic    
        """,

    'description': """
        show mail, sms marketing statistic
    """,

    'website': 'https://github.com/Frontware/odoo-marketing',
    'author': 'Frontware International',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Marketing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','fw_odoo_mail_marketing',
        'fw_odoo_sms_marketing'],

    # always loaded
    'data': [
        'views/mailing_marketing_menus.xml',

        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}
