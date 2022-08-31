from odoo import fields, models, api


class pelanggan(models.Model):
    _name = 'minimarket.pelanggan'
    _description = 'Description pelanggan'
    _rec_name = 'kode_pelanggan'


    kode_pelanggan = fields.Char(
        string='Kode_pelanggan', 
        required=False)
    pelanggan_ids = fields.One2many(
        comodel_name='minimarket.penjualan',
        inverse_name='kode_pelanggan',
        string='Kode_pelanggan IDs',
        required=False)
    nama_pelanggan = fields.Char(
        string='Nama Membership',
        required=False)
    jk = fields.Selection(string='Jenis Kelamin',
                        selection=[('laki-laki', 'Laki-laki'),
                                    ('perempuan', 'Perempuan')],
                        required=True)
    alamat = fields.Char(
        string='Alamat',
        required=False)
    no_tlpn = fields.Char(
        string='No tlpn',
        required=False)

