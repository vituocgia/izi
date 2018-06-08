# -*- coding: utf-8 -*-
# Part of izi. See LICENSE file for full copyright and licensing details.

import izi
import izi.exceptions

def login(db, login, password):
    res_users = izi.registry(db)['res.users']
    return res_users._login(db, login, password)

def check(db, uid, passwd):
    res_users = izi.registry(db)['res.users']
    return res_users.check(db, uid, passwd)

def compute_session_token(session):
    with izi.registry(session.db).cursor() as cr:
        self = izi.api.Environment(cr, session.uid, {})['res.users'].browse(session.uid)
        return self._compute_session_token(session.sid)

def check_session(session):
    with izi.registry(session.db).cursor() as cr:
        self = izi.api.Environment(cr, session.uid, {})['res.users'].browse(session.uid)
        if izi.tools.misc.consteq(self._compute_session_token(session.sid), session.session_token):
            return True
        self._invalidate_session_cache()
        return False
