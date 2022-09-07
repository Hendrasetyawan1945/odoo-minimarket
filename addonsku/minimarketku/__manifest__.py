# -*- coding: utf-8 -*-
{
    'name': "minimarketku",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base','report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/pengguna_view.xml',
        'views/pelanggan_view.xml',
        'views/penjualan_view.xml',
        #'views/penjualandetail_view.xml',
        'views/barang_view.xml',
        'views/produk_view.xml',
        'views/grup_view.xml',
        'views/pemasok_view.xml',
        'views/pembelian_view.xml',

        'views/manusia_view.xml',
        'views/kasir_view.xml',
        'views/komisaris_view.xml',
        'views/status_view.xml',


        'report/report.xml',

        'wizzard/barangdatang_wizz_view.xml',
        'wizzard/pemasokbaru_wizz_view.xml'

        #'views/pembeliandetail_view.xml',
        #'views/dagangan_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
