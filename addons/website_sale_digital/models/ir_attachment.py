# -*- coding: utf-8 -*-
# Part of izi. See LICENSE file for full copyright and licensing details.

from izi import fields, models


class Attachment(models.Model):

    _inherit = ['ir.attachment']

    product_downloadable = fields.Boolean("Downloadable from product portal", default=False)
