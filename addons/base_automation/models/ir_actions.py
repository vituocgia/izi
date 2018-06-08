# -*- coding: utf-8 -*-
# Part of izi. See LICENSE file for full copyright and licensing details.

from izi import fields, models


class ServerAction(models.Model):
    _inherit = "ir.actions.server"

    usage = fields.Selection(selection_add=[('base_automation', 'Automated Action')])
