# -*- coding: utf-8 -*-
from odoo import api, models, fields

class MeetingActCategory(models.Model):
    _name = 'meeting.act.category'

    name = fields.Char(
        string="Nombre"
    )    