# -*- coding: utf-8 -*-
# Part of izi. See LICENSE file for full copyright and licensing details.

from izi import fields, models
from izi.tools.translate import html_translate


class ProductTemplate(models.Model):
    _inherit = "product.template"

    website_description = fields.Html('Description for the website', sanitize_attributes=False) # hack, if website_sale is not installed
    quote_description = fields.Html('Description for the quote', sanitize_attributes=False, translate=html_translate)
