# -*- coding: utf-8 -*-

import izi

def migrate(cr, version):
    registry = izi.registry(cr.dbname)
    from izi.addons.account.models.chart_template import migrate_tags_on_taxes
    migrate_tags_on_taxes(cr, registry)
