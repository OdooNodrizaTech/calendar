# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class MeetingAct(models.Model):
    _name = 'meeting.act'
    _description = 'Meeting act'
    _inherit = ['mail.thread']

    name = fields.Char(
        string="Name"
    )
    date = fields.Date(
        string="Date"
    )
    meeting_act_category_id = fields.Many2one(
        comodel_name='meeting.act.category', 
        string='Meeting act category',
    )
    description = fields.Text(
        string="Description"
    )