# -*- coding: utf-8 -*-
# Part of izi. See LICENSE file for full copyright and licensing details.

import izi.tests

@izi.tests.common.at_install(False)
@izi.tests.common.post_install(True)
class TestUi(izi.tests.HttpCase):

    post_install = True
    at_install = False

    def test_01_admin_rte(self):
        self.phantom_js("/web", "izi.__DEBUG__.services['web_tour.tour'].run('rte')", "izi.__DEBUG__.services['web_tour.tour'].tours.rte.ready", login='admin')

    def test_02_admin_rte_inline(self):
        self.phantom_js("/web", "izi.__DEBUG__.services['web_tour.tour'].run('rte_inline')", "izi.__DEBUG__.services['web_tour.tour'].tours.rte_inline.ready", login='admin')
