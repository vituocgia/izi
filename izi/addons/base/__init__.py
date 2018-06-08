# -*- coding: utf-8 -*-
# Part of izi. See LICENSE file for full copyright and licensing details.

from . import ir
from . import module
from . import res

def post_init(cr, registry):
    """Rewrite ICP's to force groups"""
    from izi import api, SUPERUSER_ID

    env = api.Environment(cr, SUPERUSER_ID, {})
    env['ir.config_parameter'].init(force=True)
