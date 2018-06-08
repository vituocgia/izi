# -*- coding: utf-8 -*-
# Part of izi. See LICENSE file for full copyright and licensing details.

{
    'name': 'VAT Number Autocomplete',
    'version': '1.0',
    'category': 'Accounting',
    'description': """
Auto-Complete Addresses based on VAT numbers
============================================

    This module requires the python library stdnum to work.
    """,
    'depends': ['base_vat'],
    'website': 'https://www.izi.asia/page/accounting',
    'data': [
        'views/res_partner_views.xml',
        'views/res_company_view.xml',
    ],
    'auto_install': True
}
