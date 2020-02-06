# -*- encoding: utf-8 -*-
{
    'name': 'To-do Application',
    'version': '1.0',
    'author': 'EEP - Profesor',
    'description': """ Modulo primero de las pruebas de desarrollo grupo DAM.""",
    'depends': ['mail'],
    'application': True,
    'data' : [
        'views/todo_views.xml', 
        'security/ir.model.access.csv',
        'security/todo_access_rules.xml',
            ],
}
