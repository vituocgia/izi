# -*- coding: utf-8 -*-
# Part of izi. See LICENSE file for full copyright and licensing details.

{
    'name': 'izi Settings Dashboard',
    'version': '1.0',
    'summary': 'Quick actions for installing new app, adding users, completing planners, etc.',
    'category': 'Extra Tools',
    'description':
    """
izi dashboard
==============
* Quick access to install apps
* Quick users add
* Access all planners at one place
* Quick access to the `App Store` and `Theme Store`

        """,
    'data': [
        'views/dashboard_views.xml',
        'views/dashboard_templates.xml',
    ],
    'depends': ['web_planner'],
    'qweb': ['static/src/xml/dashboard.xml'],
    'auto_install': True,
}
