# -*- coding: utf-8 -*-
# Part of izi. See LICENSE file for full copyright and licensing details.

from izi import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = ['res.config.settings']

    module_website_hr_recruitment = fields.Boolean(string='Online Posting')
    module_hr_recruitment_survey = fields.Boolean(string='Interview Forms')
