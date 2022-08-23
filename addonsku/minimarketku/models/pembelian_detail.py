from odoo import fields, models, api


class pembelian_detail(models.Model):
    _name = 'minimarket.pembeliandetail'
    _description = 'Description'

    no_masuk = fields.Many2one(
        comodel_name='minimarket.pembelian',
        string='No_masuk',
        required=False)
    kode_barang_ids = fields.One2many(
        comodel_name='minimarket.barang',
        inverse_name='kode_barang',
        string='Kode_barang_ids',
        required=False)
    nama_barangpembelian = fields.Char(
        compute="_compute_namabarang",
        string='Nama_barang',
        required=False)
    harga_beli = fields.Integer(
        compute="_compute_hargabeli",
        string='Harga_beli',
        required=False)
    jumlah = fields.Integer(
        string='Jumlah',
        required=False)
    subtotal = fields.Integer(
        string='Subtotal',
        required=False)


    @api.depends('harga_beli')
    def _compute_hargabeli(self):
        for a in self:
            a.harga_beli = a.kode_barang_ids.harga_beli

    @api.depends('nama_barangpembelian')
    def _compute_namabarang(self):
        for a in self:
            a.nama_barangpembelian = a.kode_barang_ids.nama_barang


