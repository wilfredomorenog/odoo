# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'After Sales Commissioning',
    'version': '11.0',
    'summary': 'You can create commissioning and manage them very easily',
    'author': 'FOSS INFOTECH PVT LTD',
    'category': 'Extra Tools',
    'website': 'http://www.fossinfotech.com',
    'description': """After Sales Commissioning module for Odoo 11. This module allows you to define service engineers to their commissions and generates visits for the respective commissions. """,
    'depends': ['base','product','sale', 'account','stock','project'],
    'data': [
        'security/commission_security.xml',
        'security/ir.model.access.csv',
        'data/mail_commissioning.xml',
        'data/ir.sequence.xml',
        'wizard/crm_commissioning_failure_views.xml',
        'views/crm_commissioning_views.xml',
            ],

    'images': [
        'static/description/banner.png',
        'static/description/icon.png',
        'static/description/index.html',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}