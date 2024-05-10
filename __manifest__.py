# -*- coding: utf-8 -*-
{
    'name': "Aden",

    'summary': "Challenge Aden",

    'description': """
Challenge Aden
    """,

    'author': "Luciano Esperlazza",
    'website': "lucianoespe98@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu_principal.xml',
        'views/alumno_views.xml',
        'views/programa_views.xml',
        'views/inscripcion_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

