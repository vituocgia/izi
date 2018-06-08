# -*- coding: utf-8 -*-
# Part of izi. See LICENSE file for full copyright and licensing details.

{
    'name': 'PosBox Software Upgrader',
    'category': 'Point of Sale',
    'website': 'https://www.izi.asia/page/point-of-sale',
    'sequence': 6,
    'summary': 'Allows to remotely upgrade the PosBox software',
    'description': """
PosBox Software Upgrader
========================

This module allows to remotely upgrade the PosBox software to a
new version. This module is specific to the PosBox setup and environment
and should not be installed on regular izi servers.

""",
    'depends': ['hw_proxy'],
    'installable':  False,
}
