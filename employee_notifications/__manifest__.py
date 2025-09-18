{
    'name' : 'Employee Notifications',
    'version' : '1.0',
    'summary': 'Send notifications to employees on Aniversary and Birthday',
    'description': """
        This module sends notifications to employees on their work anniversary and birthday.
    """,
    'category': 'Human Resources',
    'depends' : ['base', 'hr'],
    'data': [
        'views/hr_employee_views.xml',
        'data/mail_templates.xml',
        'data/ir_cron.xml',
    ],
    'installable': True,
    'application': False,
} 