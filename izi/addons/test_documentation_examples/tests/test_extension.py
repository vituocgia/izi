# -*- coding: utf-8 -*-
# Part of izi. See LICENSE file for full copyright and licensing details.

from izi.tests import common

class TestBasicInheritance(common.TransactionCase):
    def test_extend_fields(self):
        env = self.env

        record = env['extension.0'].create({})

        self.assertDictContainsSubset(
        {'name': "A", 'description': "Extended"}
        ,
        record.read()[0]
        )
