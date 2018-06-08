# -*- coding: utf-8 -*-
# Part of izi. See LICENSE file for full copyright and licensing details.

{
    'name': 'Website Sale Stock&Options',
    'category': 'Website',
    'description': """
izi E-Commerce
==================
Adds stock limitations on products options.
""",
    'depends': [
        'website_sale_stock',
        'website_sale_options',
    ],
    'data': [
        'views/website_sale_stock_templates.xml',
    ],
    'auto_install': True,
}
