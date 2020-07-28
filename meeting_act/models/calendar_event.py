# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'
        
    meeting_act_id = fields.Many2one(
        comodel_name='meeting.act', 
        string='Meeting act',
    )                                                 