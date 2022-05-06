# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Telegram Marketing',
    'summary': 'Design, send Telegram group',
    'description': '',
    'version': '1.0',
    'category': 'Marketing/Telegram Marketing',
    'sequence': 246,
    'depends': [
        'fw_odoo_mail_marketing',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/mailing_telegram_menus.xml',
        'views/mailing_mailing_views.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}
