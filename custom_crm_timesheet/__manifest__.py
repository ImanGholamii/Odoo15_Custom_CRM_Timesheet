# -*- coding: utf-8 -*-
{
    'name': "Custom CRM Timesheet",

    'summary': """
        Adds timesheet tracking to CRM opportunities.
        """,

    'description': """
        Adds timesheet tracking to CRM opportunities.
    """,

    'author': "Iman Gholami",
    'website': "https://github.com/ImanGholamii/Odoo15_Custom_CRM_Timesheet.git",

    'category': 'Sales/CRM',
    'version': '0.1',
    'sequence': -99,
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/custom_crm_timesheet_security.xml',
        'views/timesheet_views.xml',
        'views/crm_lead_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
    'icon': 'custom_crm_timesheet/static/description/icon.png',
    'installable': True,
    'auto_install': False,
    'application': False,
}
