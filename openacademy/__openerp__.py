# -*- coding: utf-8 -*-
<<<<<<< HEAD
{
    'name': "openacademy",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Your Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'active': True
}
=======

{

    'name': "Open Academy",
    'version': '0.1',
    'depends': ['base'], #esto indica si depende de algun modulo existente 
    'author': "Miguel Hiciano",
    'category': 'Test',
    'description': """
    Open Academy module for managing trainings:
	-Training courses 
	-training sessions
	-attendees registration
    """,
    # data files always loaded at installation
    'data': [],
    # data files containing optionally loaded demonstration data
    'demo': [],
    'installable': True,
    'active': True
}

>>>>>>> 0ff3f62932172ce445e9d5a1b0e75817da80a75c
