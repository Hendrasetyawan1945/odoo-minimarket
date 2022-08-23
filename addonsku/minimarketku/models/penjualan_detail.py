from odoo import fields, models, api


class penjualandetail(models.Model):
    _name = 'minimarket.penjualandetail'
    _description = 'Description penjualan detail'
    _rec_name = 'kode_barang_ids'
    _rec_name = 'no_nota_id'

    nota_id = fields.Char(
        string='Nota_id',
        required=False)
    no_nota_id = fields.Many2one(
        comodel_name='minimarket.penjualan',
        string='Kode Pelanggan',
        required=False)
    kode_barang_ids = fields.Many2one(
        comodel_name='minimarket.barang',
        inverse_name='kode_barang',
        string='Kode_barang_ids',
        required=False)
    nama_barangpenjualan = fields.Char(
        compute="_compute_namabarang",
        string='Nama_barang',
        required=False)
    harga_jual = fields.Integer(
        compute="_compute_hargajual",
        string='Harge_jual',
        required=False)
    jumlah = fields.Integer(
        string='Jumlah',
        required=False)
    subtotal = fields.Integer(
        string='Subtotal',
        compute="_compute_subtotal",
        required=False)

    @api.depends('harga_jual')
    def _compute_hargajual(self):
        for a in self:
            a.harga_jual = a.kode_barang_ids.harga_jual

    @api.depends('subtotal')
    def _compute_subtotal(self):
        for a in self:
            a.subtotal = a.jumlah

    @api.depends('nama_barangpenjualan')
    def _compute_namabarang(self):
        for a in self:
            a.nama_barangpenjualan = a.kode_barang_ids.nama_barang




