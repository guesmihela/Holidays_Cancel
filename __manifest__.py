

{
    'name': 'Cancel_Holidays_Request',
    'version': '1.0',
    'sequence' : 1,
    'category': 'Human Ressources',
    'summary': 'Employé peut annuler une demande de congé aprés validation et confirmation par superieur hierarchique',
    'author': 'TNT',
    'license': 'AGPL-3',
    'website': 'http://tnt.com.tn',
    'depends': ['base','hr_holidays'],
    'active': True,
    'data': [
        'views/hr_holidays_status.xml',
        'views/hr_holidays_cancel.xml',
        'security/hr_holidays_security.xml',
    ],
    'auto_install': False,
    'application': True,
    'installable': True,
}
