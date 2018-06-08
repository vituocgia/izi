# -*- coding: utf-8 -*-

import izi

def migrate(cr, version):
    registry = izi.registry(cr.dbname)
    from izi.addons.account.models.chart_template import migrate_set_tags_and_taxes_updatable
    migrate_set_tags_and_taxes_updatable(cr, registry, 'l10n_at')
