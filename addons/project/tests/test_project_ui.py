# Part of izi. See LICENSE file for full copyright and licensing details.

import izi.tests


@izi.tests.common.at_install(False)
@izi.tests.common.post_install(True)
class TestUi(izi.tests.HttpCase):

    def test_01_project_tour(self):
        self.phantom_js("/web", "izi.__DEBUG__.services['web_tour.tour'].run('project_tour')", "izi.__DEBUG__.services['web_tour.tour'].tours.project_tour.ready", login="admin")
