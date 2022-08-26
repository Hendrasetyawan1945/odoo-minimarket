from odoo import fields, models, api


class pembelian_detail(models.Model):
    _name = 'minimarket.pembeliandetail'
    _description = 'Description'
    #_rec_name = 'no_pembelian'
    #_rec_name = 'no_masuk_ids'

    no_masuk = fields.Char(
        string='No_masuk',
        required=False)
    no_pembelian = fields.Many2one(
        comodel_name='minimarket.pembelian',
        string='No_pembelian',
        required=False)
    kode_barang_ids = fields.Many2one(
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
        compute="_compute_subtotal",
        string='Subtotal',
        required=False)

    @api.model
    def create(self, vals):
        record = super(pembelian_detail, self).create(vals)
        if record.jumlah:
            self.env['minimarket.barang'].search([('id', '=', record.kode_barang_ids.id)]).write({
                'stok': record.kode_barang_ids.stok+record.jumlah})
            return record

    @api.depends('harga_beli')
    def _compute_hargabeli(self):
        for a in self:
            a.harga_beli = a.kode_barang_ids.harga_beli

    @api.depends('nama_barangpembelian')
    def _compute_namabarang(self):
        for a in self:
            a.nama_barangpembelian = a.kode_barang_ids.nama_barang

    @api.depends('subtotal')
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.jumlah * record.harga_beli


