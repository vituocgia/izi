import izi.tests


@izi.tests.common.at_install(False)
@izi.tests.common.post_install(True)
class TestUi(izi.tests.HttpCase):
    def test_admin(self):
        self.phantom_js("/", "izi.__DEBUG__.services['web_tour.tour'].run('event')", "izi.__DEBUG__.services['web_tour.tour'].tours.event.ready", login='admin')
