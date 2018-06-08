# -*- coding: utf-8 -*-
# Part of izi. See LICENSE file for full copyright and licensing details.

from izi import fields, models


class Attachment(models.Model):

    _inherit = "ir.attachment"

    # related for backward compatibility with saas-6
    website_url = fields.Char(string="Attachment URL", related='local_url', deprecated=True)
