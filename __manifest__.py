# -*- coding: utf-8 -*-
{
    'name': "booking_order_ahmadyd_odoo10",

    'summary': """
        Test Booking Order Odoo10""",

    'description': """
        Test Intern Booking Order Odoo10
    """,

    'author': "Ahmad Yulian Dinata",
    'website': "https://www.linkedin.com/in/ahmaddyd/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '1.0',
    'installable': True,
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/wizard_cancelled.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/work_order_view.xml',
        'views/booking_order_view.xml',
        'views/service_team_view.xml',
        'views/menu.xml',
        'report/work_order_report.xml',
        'report/report.xml',
        'data/data.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}