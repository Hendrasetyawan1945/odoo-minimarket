from odoo import api, fields, models


class barangdatang(models.TransientModel):
    _name = 'minimarket.barangdatang'

    barang_id = fields.Many2one(comodel_name='kode_barang',
                                string='kode barang',
                                required=True)
    jumlah = fields.Integer(string='Jumlah')


def barang_datang(self):
    pass