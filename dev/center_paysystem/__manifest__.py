{
    'name': 'Center PaySystem',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Manage students, teachers, courses, groups, and payments',
    'depends': ['base'],
    'data': [
        # 'security/security.xml',
        # 'security/ir.model.access.csv',
        # 'views/menu.xml',
        # 'views/student_views.xml',
        'views/teacher_views.xml',
        'reports/student_report.xml',
    ],
    'installable': True,
    'application': True,
}
