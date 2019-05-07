# -*- coding: utf-8 -*-
{
    # Module name in English
    'name': "GRC Parthenay-Gatine",
    # Version, "odoo.min.yy.m.d"
    'version': '10.0.0.0.1',
    # Short description (with keywords)
    'summary': "Gestion de la relation citoyen",
    # Description with metadata (in french)
    'description': "Gestion de la relation citoyen",
    'author': "Moi",
    'website': "http://cc-parthenay-gatine.fr",
    # distribution license for the module (defaults: AGPL-3)
    'license': "AGPL-3",
    # Categories can be used to filter modules in modules listing. For the full list :
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    'category': 'Citizen Management',
    'external_dependencies': {
        'python': []
    },
    # any module necessary for this one to work correctly. Either because this module uses features
    # they create or because it alters resources they define.
    'depends': [
        # --- Odoo --- #

        # --- External --- #
        'website_support',
    ],
    # always loaded
    'qweb': [
    ],
    # list of XML files with data that will load to DB at moment when you install module
    'init_xml': [],
    # list of XML files with data that will load to DB at moment when you install or update module.
    'update_xml': [],
    # List of data files which must always be installed or updated with the module.
    # A list of paths from the module root directory
    'data': [
            'data/groups.xml',
            'templates/web_services_templates.xml',
            'views/website_support_dashboard.xml',
            'views/inherited_website_support_views.xml',
            'views/inherited_website_support_sub_category_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'application': True,
    'auto_install': False,
    # permet d'installer automatiquement le module si toutes ses dépendances sont installés
    # -default value set is False
    # -If false, the dependent modules are not installed if not installed prior to the dependent module.
    # -If True, all corresponding dependent modules are installed at the time of installing this module.
    'installable': True
    # -True, module can be installed.
    # -False, module is listed in application, but cannot install them.
}
