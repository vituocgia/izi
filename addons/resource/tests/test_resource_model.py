# -*- coding: utf-8 -*-
# Part of izi. See LICENSE file for full copyright and licensing details.

from izi import fields, models


class MailTest(models.Model):
    _description = 'Test Resource Model'
    _name = 'resource.test'
    _inherit = ['resource.mixin']

    name = fields.Char()
