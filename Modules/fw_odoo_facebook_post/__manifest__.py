# -*- coding: utf-8 -*-
{
    'name': "fw_odoo_facebook_post",

    'summary': """
        Module used to Post on Facebook""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Odoo thailand",
    'website': "https://www.odoo.co.th",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'data/cron.xml',
        'views/views.xml',
        'views/help_views.xml',
        'wizard/facebook_schedule_date_action.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        
    ],
}
