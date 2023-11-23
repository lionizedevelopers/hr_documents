{
    'name': 'HR Documents',
    'description    ': """Upload Zip file of bulk Employee and Profile image at a time using HR Documents module.
                          By:lionizedevelopers@gmail.com""",
    'version': '17.0.1.0',
    'category': 'Human Resources',
    "sequence": 1,
    'summary': 'HR Documents',
    'complexity': "easy",
    'author': 'Lionize Developers',
    'depends': ['base','hr'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/wizard_view_bulk_upload.xml',
        'views/hr_employee_view.xml',
        'data/server_action.xml',
    ],
    'demo': [],
    'images': [
        'static/description/vector.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}