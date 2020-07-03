# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, models, fields

class MeetingActCategory(models.Model):
    _name = 'meeting.act.category'

    name = fields.Char(
        string="Nombre"
    )    