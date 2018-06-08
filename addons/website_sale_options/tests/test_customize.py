# Part of izi. See LICENSE file for full copyright and licensing details.

import izi.tests

class TestUi(izi.tests.HttpCase):

    post_install = True
    at_install = False

    def test_01_admin_shop_customize_tour(self):
        self.phantom_js("/", "izi.__DEBUG__.services['web_tour.tour'].run('shop_customize')", "izi.__DEBUG__.services['web_tour.tour'].tours.shop_customize.ready", login="admin")
