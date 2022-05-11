# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'SMS Marketing customize',
    'summary': 'fix SMS to work with other type',
    'description': '',
    'version': '1.0',
    'category': 'Marketing/SMS Marketing',
    'sequence': 245,
    'depends': [
        'mass_mailing_sms'
    ],
    'data': [
        'views/mailing_mailing_views.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}
