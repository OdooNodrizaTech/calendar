# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Meeting Act",
    "version": "12.0.1.0.0",
    "author": "Odoo Nodriza Tech (ONT), "
              "Odoo Community Association (OCA)",
    "website": "https://nodrizatech.com/",
    "category": "Tools",
    "license": "AGPL-3",
    "depends": [
        "base",
        "calendar"
    ],
    "data": [
        "views/calendar_event_view.xml",
        "views/meeting_act_view.xml",
        "security/ir.model.access.csv",
    ],
    "installable": True
}
