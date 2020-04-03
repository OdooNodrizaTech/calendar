# -*- coding: utf-8 -*-
from openerp import api, models, fields
from dateutil.relativedelta import relativedelta
from datetime import datetime

import logging

_logger = logging.getLogger(__name__)

class CalendarEvent(models.Model):
    _inherit = 'calendar.event'
        
    meeting_act_id = fields.Many2one(
        comodel_name='meeting.act', 
        string='Acta reunion',
    )                                                 