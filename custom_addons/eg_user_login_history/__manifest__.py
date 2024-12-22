{
    'name': 'Users Login History',
    'version': '17.0',
    'category': 'Sales/CRM',
    'summary': "Track and view the login history of users in Odoo. Monitor login activity with detailed records, including login dates and times, for enhanced user management and system security. Keywords: Users Login History, Odoo User Management, Login Activity Tracking, User Login Records, System Security, User Monitoring, Odoo Security Features, Login History in Odoo.",
    'author': 'INKERP',
    'website': 'https://www.inkerp.com/',
    'depends': ['base', 'mail'],
    
    'data': [
        'security/ir.model.access.csv',
        'views/user_attendance.xml',
    ],
    
    'images': ['static/description/banner.png'],
    'license': "OPL-1",
    'installable': True,
    'application': True,
    'auto_install': False,
}
