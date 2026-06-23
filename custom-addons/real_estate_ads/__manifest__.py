{
    "name": "real_estate_ads",
    "version": "1.0",
    "website": "www.odoo.com",
    "author": "Daniel",
    "description": """
    Real Estate Module To Show Available Properties
    """,
    "category": "Sales",
    "depends": ["base","mail", 'website'],
    "data": [
        'security/ir.model.access.csv',
        'security/res_groups.xml',
        'security/model_access.xml',
        'security/ir_rule.xml',
        
        'views/property_view.xml',
        'views/property_type_view.xml',
        'views/property_tag_view.xml',
        'views/property_offer_view.xml',
        'views/menu_items.xml',
        'views/property_web_template.xml',
        # 'views/email_template.xml',
        
        #Data File
        
        # 'data/property_type.xml',
        'data/estate.property.type.csv',
        'data/email_template.xml',
        
        'report/property_report.xml'
        
        ],
    "demo": [
        'demo/property_tag.xml',
        ],
    "installable": True,
    "application": True,   
    "license": "LGPL-3"
}
