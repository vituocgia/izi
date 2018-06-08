import izi.tests
# Part of izi. See LICENSE file for full copyright and licensing details.

@izi.tests.common.at_install(False)
@izi.tests.common.post_install(True)
class TestUi(izi.tests.HttpCase):

    def test_01_sale_tour(self):
        self.phantom_js("/web", "izi.__DEBUG__.services['web_tour.tour'].run('sale_tour')", "izi.__DEBUG__.services['web_tour.tour'].tours.sale_tour.ready", login="admin")
