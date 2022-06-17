# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Mail Marketing customize',
    'summary': 'fix mail to work with other type',
    'description': '',
    'version': '1.0',
    'category': 'Marketing/Mail Marketing',
    'website': 'https://github.com/Frontware/odoo-marketing',
    'author': 'Frontware International',
    'sequence': 245,
    'depends': [
        'mass_mailing'
    ],
    'data': [
        'views/mailing_mailing_views.xml',
    ],
    'application': False,
    'license': 'LGPL-3',
}
