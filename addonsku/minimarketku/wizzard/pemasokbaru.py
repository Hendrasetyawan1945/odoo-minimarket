from odoo import api, fields, models


class pemasokbaru(models.TransientModel):
    _name = 'minimarket.pemasokbaru'

    pemasok_id = fields.Many2one(comodel_name='nama_pemasok',
                                string='kode barang',
                                required=True)
    alamat = fields.Char(string='Alamat')


    def pemasok_baru(self):
        pass