{
    'name': 'eCommerce',
    'category': 'Website',
    'sequence': 55,
    'summary': 'Sell Your Products Online',
    'website': 'https://www.izi.asia/page/e-commerce',
    'version': '1.0',
    'description': "",
    'depends': ['website', 'sale_payment', 'website_payment', 'website_mail', 'website_form', 'website_rating'],
    'data': [
        'security/ir.model.access.csv',
        'security/website_sale.xml',
        'data/data.xml',
        'data/web_planner_data.xml',
        'data/mail_template_data.xml',
        'views/product_views.xml',
        'views/account_views.xml',
        'views/sale_report_views.xml',
        'views/sale_order_views.xml',
        'views/crm_team_views.xml',
        'views/templates.xml',
        'views/payment_views.xml',
        'views/snippets.xml',
        'views/report_shop_saleorder.xml',
        'views/res_config_settings_views.xml',
    ],
    'demo': [
        'data/demo.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}
