# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Whatsapp Marketing',
    'summary': 'Design, send Whatsapp group',
    'description': '',
    'version': '1.0',
    'category': 'Marketing/Whatsapp Marketing',
    'sequence': 246,
    'depends': [
        'fw_odoo_mail_marketing',
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/multiple_contact_wizard_view.xml',
        'views/mailing_whatsapp_menus.xml',
        'views/mailing_mailing_views.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}
