from odoo import fields, models, api


class penjualandetail(models.Model):
    _name = 'minimarket.penjualandetail'
    _description = 'Description penjualan detail'
    _rec_name = 'kode_barang_ids'
    #_rec_name = 'no_nota_id'

    nota_id = fields.Char(
        # comodel_name='minimarket.penjualan',
        string='Nota_id',
        required=False)
    no_penjualan = fields.Many2one(
        comodel_name='minimarket.penjualan',
        string='Kode penjualan',
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
        for record in self:
            record.subtotal = record.jumlah * record.harga_jual

    @api.depends('nama_barangpenjualan')
    def _compute_namabarang(self):
        for a in self:
            a.nama_barangpenjualan = a.kode_barang_ids.nama_barang


total = fields.Integer(compute='_compute_total', string='Total',store=True)

@api.depends('total')
def _compute_total(self):
    for record in self:
        a = sum(self.env['minimarket.penjualandetail'].search(
            [('no_penjualan', '=', record.id)]).mapped('harga_jual'))
        record.total = a


