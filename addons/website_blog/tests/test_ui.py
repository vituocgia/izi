# Part of izi. See LICENSE file for full copyright and licensing details.

import izi.tests


@izi.tests.common.at_install(False)
@izi.tests.common.post_install(True)
class TestUi(izi.tests.HttpCase):
    def test_admin(self):
        self.phantom_js("/", "izi.__DEBUG__.services['web_tour.tour'].run('blog')", "izi.__DEBUG__.services['web_tour.tour'].tours.blog.ready", login='admin')
