# -*- coding: utf-8 -*-

from izi import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    event_ok = fields.Boolean(string='Is an Event Ticket', help='Determine if a product needs '
      'to create automatically an event registration at the confirmation of a sales order line.')

    @api.onchange('event_ok')
    def _onchange_event_ok(self):
        if self.event_ok:
            self.type = 'service'


class Product(models.Model):
    _inherit = 'product.product'

    event_ticket_ids = fields.One2many('event.event.ticket', 'product_id', string='Event Tickets')

    @api.onchange('event_ok')
    def _onchange_event_ok(self):
        """ Redirection, inheritance mechanism hides the method on the model """
        if self.event_ok:
            self.type = 'service'
