# -*- encoding: utf-8 -*-
{
    'name': 'Developments Manager',
    'version': '1.0',
    'author': 'EEP - Profesor',
    'description': """ Modulo gestion de solicitudes de desarrollo.""",
    'depends': ['base'],
    'application': True,
    'data' : [
        'views/devman_views.xml',
        'views/report_devman_tasks_hours.xml',
        'views/report_devman_tasks_responsible.xml',
        'dev_manager_report.xml',
            ],
}
