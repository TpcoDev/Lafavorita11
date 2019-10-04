# -*- coding: utf-8 -*-
{
    'name': "Ahorasoft Latproject Account",
    'summary': """
        Latproject Module
===========================

Custom module for Latproject""",
    'description': """
Latproject Module
===========================

Custom module for Latproject Account
    """,
    'author': "Ahorasoft",
    'version': '1.0.0',
    'website': "http://www.ahorasoft.com",
    'category': 'Uncategorized',
    'depends': ['base','l10n_cl_fe'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/as_sii_xml_envio.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}