# -*- coding: utf-8 -*-
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
    'data': ['view/openacademy_course_view.xml','view/openacademy_session_view.xml',],
    # data files containing optionally loaded demonstration data
    'demo': ['demo/demo.xml' ],
    'installable': True,
    'active': True
}
