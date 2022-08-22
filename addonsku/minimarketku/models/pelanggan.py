from odoo import fields, models, api


class pelanggan(models.Model):
    _name = 'minimarket.pelanggan'
    _description = 'Description pelanggan'

    kode_pelangganids = fields.One2many(
        comodel_name='minimarket.pelanggan',
        inverse_name='kode_pelanggan',
        string='Kode_pelanggan IDs',
        required=False)
    nama_pelanggan = fields.Char(
        string='Nama_pelanggan',
        required=False)
    alamat = fields.Char(
        string='Alamat',
        required=False)
    no_tlpn = fields.Char(
        string='No tlpn',
        required=False)

