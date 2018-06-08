# -*- coding: utf-8 -*-
# Part of izi. See LICENSE file for full copyright and licensing details.

from izi import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    l10n_in_hsn_code = fields.Char(string="HSN/SAC Code", help="Harmonized System Nomenclature/Services Accounting Code")
