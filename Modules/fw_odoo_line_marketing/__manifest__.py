# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'LINE Marketing',
    'summary': 'Design, send LINE group',
    'description': '',
    'version': '1.0',
    'category': 'Marketing/LINE Marketing',
    'sequence': 245,
    'depends': [
        'mass_mailing'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/mailing_line_menus.xml',
        'views/mailing_mailing_views.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}
