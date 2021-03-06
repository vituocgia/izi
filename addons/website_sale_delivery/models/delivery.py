# -*- coding: utf-8 -*-
# Part of izi. See LICENSE file for full copyright and licensing details.

from izi import fields, models


class DeliveryCarrier(models.Model):
    _name = 'delivery.carrier'
    _inherit = ['delivery.carrier', 'website.published.mixin']

    website_description = fields.Text(related='product_id.description_sale', string='Description for Online Quotations')
    website_published = fields.Boolean(default=False)
