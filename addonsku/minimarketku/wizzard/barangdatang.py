from odoo import api, fields, models


class barangdatang(models.TransientModel):
    _name = 'minimarket.barangdatang'

    barang_id = fields.Many2one(comodel_name='minimarket.barang',
                                string='kode barang',
                                required=True)
    jumlah = fields.Integer(string='Jumlah')


    def barang_datang(self):
        for i in self :
            self.env['minimarket.barang'].search([('id', '=', i.barang_id.id)]).write(
                {'stok' : i.barang_id.stok + i.jumlah })