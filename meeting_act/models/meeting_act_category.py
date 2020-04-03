# -*- coding: utf-8 -*-
from openerp import api, models, fields

class MeetingActCategory(models.Model):
    _name = 'meeting.act.category'

    name = fields.Char(
        string="Nombre"
    )    