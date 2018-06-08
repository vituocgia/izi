# Part of izi. See LICENSE file for full copyright and licensing details.

import izi.tests


@izi.tests.common.at_install(False)
@izi.tests.common.post_install(True)
class TestUi(izi.tests.HttpCase):
    
    def test_01_main_flow_tour(self):
        self.phantom_js("/web", "izi.__DEBUG__.services['web_tour.tour'].run('main_flow_tour')", "izi.__DEBUG__.services['web_tour.tour'].tours.main_flow_tour.ready", login="admin", timeout=180)
