# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Twitter Marketing',
    'summary': 'Design, send twitter group',
    'description': '',
    'version': '1.0',
    'website': 'https://github.com/Frontware/odoo-marketing',
    'author': 'Frontware International',
    'category': 'Marketing/twitter Marketing',
    'sequence': 246,
    'depends': [
        'fw_odoo_mail_marketing',
        'fw_odoo_sms_marketing',
    ],
    'external_dependencies': {
        'python': ['tweepy']
    },    
    'data': [
        'security/ir.model.access.csv',
        'data/cron.xml',
        'data/utm_data.xml',
        'data/help.xml',
        
        'views/mailing_mailing_views.xml',
        'views/help_view.xml',
        'wizard/twitter_schedule_date_action.xml',
        'views/mailing_twitter_menus.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}
