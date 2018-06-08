# -*- coding: utf-8 -*-
# Part of izi. See LICENSE file for full copyright and licensing details.

{
    'name': 'Customer References',
    'category': 'Website',
    'website': 'https://www.izi.asia/page/website-builder',
    'summary': 'Publish Your Customer References',
    'version': '1.0',
    'description': """
izi Customer References
===========================
""",
    'depends': [
        'website_crm_partner_assign',
        'website_partner',
        'website_google_map',
    ],
    'demo': [
        'data/res_partner_demo.xml',
    ],
    'data': [
        'views/website_customer_templates.xml',
        'views/res_partner_views.xml',
        'security/ir.model.access.csv',
        'security/ir_rule.xml',
    ],
    'qweb': [],
    'installable': True,
}
