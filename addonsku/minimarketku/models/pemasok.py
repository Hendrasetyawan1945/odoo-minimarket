from odoo import fields, models, api


class pemasok(models.Model):
    _name = 'minimarket.pemasok'
    _description = 'Description'
    _rec_name = 'kode_pemasok'

    kode_pemasok = fields.Char(
        string='Kode_pemasok',
        required=False)
    kode_pembelian_ids = fields.One2many(
        comodel_name='minimarket.pembelian',
        inverse_name='kode_pemasok',
        string='Kode_pembelian_ids',
        required=False)
    nama_pemasok = fields.Char(
        string='Nama_pemasok',
        required=False)
    alamat = fields.Char(
        string='Alamat',
        required=False)
    kota = fields.Char(
        string='Kota',
        required=False)
    provinsi = fields.Char(
        string='Provinsi',
        required=False)
    no_tlpn = fields.Char(
        string='No_tlpn',
        required=False)
    no_fak = fields.Char(
        string='No_fak',
        required=False)
    kontak_kp = fields.Char(
        string='Kontak_kp',
        required=False)