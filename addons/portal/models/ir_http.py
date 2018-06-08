# -*- coding: utf-8 -*-
# Part of izi. See LICENSE file for full copyright and licensing details.

from izi import api, fields, models
from izi.osv import expression


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    @classmethod
    def _get_translation_frontend_modules_domain(cls):
        domain = super(IrHttp, cls)._get_translation_frontend_modules_domain()
        return expression.OR([domain, [('name', '=', 'portal')]])

