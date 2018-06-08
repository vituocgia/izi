# -*- coding: utf-8 -*-
# Part of izi. See LICENSE file for full copyright and licensing details.

from izi import models, api, _
from izi.exceptions import UserError


class BankStatement(models.Model):
    _inherit = 'account.bank.statement'

    @api.multi
    def button_draft(self):
        self.state = 'open'


