# -*- coding: utf-8 -*-
# Part of izi. See LICENSE file for full copyright and licensing details.

from izi.api import Environment
import izi.tests


@izi.tests.common.at_install(False)
@izi.tests.common.post_install(True)
class TestWebsiteCrm(izi.tests.HttpCase):

    def test_tour(self):
        self.phantom_js("/", "izi.__DEBUG__.services['web_tour.tour'].run('website_crm_tour')", "izi.__DEBUG__.services['web_tour.tour'].tours.website_crm_tour.ready")

        # need environment using the test cursor as it's not committed
        cr = self.registry.cursor()
        assert cr is self.registry.test_cr
        env = Environment(cr, self.uid, {})
        record = env['crm.lead'].search([('description', '=', '### TOUR DATA ###')])
        assert len(record) == 1
        assert record.contact_name == 'John Smith'
        assert record.email_from == 'john@smith.com'
        assert record.partner_name == 'izi S.A.'
