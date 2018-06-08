# -*- coding: utf-8 -*-
# Part of izi. See LICENSE file for full copyright and licensing details.
import izi.tests


@izi.tests.common.at_install(False)
@izi.tests.common.post_install(True)
class TestUi(izi.tests.HttpCase):
    def test_01_wishlist_tour(self):
        self.phantom_js("/", "izi.__DEBUG__.services['web_tour.tour'].run('shop_wishlist')", "izi.__DEBUG__.services['web_tour.tour'].tours.shop_wishlist.ready")
