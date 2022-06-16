# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Facebook Marketing',
    'summary': 'Design, send facebook group',
    'description': '',
    'version': '1.0',
    'category': 'Marketing/facebook Marketing',
    'website': 'https://github.com/Frontware/odoo-marketing',
    'author': 'Frontware International',
    'sequence': 246,
    'depends': [
        'fw_odoo_mail_marketing',
        'fw_odoo_sms_marketing',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/cron.xml',
        'data/utm_data.xml',
        'data/help.xml',

        'views/mailing_mailing_views.xml',
        'views/help_view.xml',
        'wizard/facebook_schedule_date_action.xml',

        'views/mailing_facebook_menus.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}
