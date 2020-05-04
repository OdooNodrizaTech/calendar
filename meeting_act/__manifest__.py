# -*- coding: utf-8 -*-
{
    'name': 'Meeting Act',
    'version': '12.0.1.0.0',    
    'author': 'Odoo Nodriza Tech (ONT)',
    'website': 'https://nodrizatech.com/',
    'category': 'Tools',
    'license': 'AGPL-3',
    'depends': ['base', 'calendar'],    
    'installable': True,
    'auto_install': False,
    'data': [
        'views/calendar_event_view.xml',
        'views/meeting_act_view.xml',        
        'security/ir.model.access.csv',        
    ],    
}