# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'LINE Marketing',
    'summary': 'Design, send LINE group',
    'description': '',
    'version': '1.0',
    'website': 'https://github.com/Frontware/odoo-marketing',
    'author': 'Frontware International',
    'category': 'Marketing/LINE Marketing',
    'sequence': 245,
    'depends': [
        'fw_odoo_mail_marketing'
    ],
    'data': [
        'security/ir.model.access.csv',
        "data/fw_bot_group_help.xml",

        'views/mailing_line_menus.xml',
        'views/mailing_mailing_views.xml',

        "views/fw_bot_group.xml",
        "views/fw_bot_group_help.xml",

    ],
    'application': False,
    'license': 'LGPL-3',
}
