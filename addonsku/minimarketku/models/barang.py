from odoo import fields, models, api


class barang(models.Model):
    _name = 'minimarket.barang'
    _description = 'Description'
    _rec_name = 'kode_barang'

    kode_barang = fields.Char(
        string='Kode_barang',
        required=False)

    kode_produk = fields.Many2one(
        comodel_name='minimarket.produk',
        string='Kode_produk',
        required=False)

    keterangan_produk = fields.Char(
        string='Nama Produk',
        compute="_compute_produk",
        required=False)

    nama_barang = fields.Char(
        string='Nama_barang',
        required=False)
    satuan = fields.Selection(
        string='Satuan',
        selection=[('unit', 'Unit'),
                ('dus', 'Dus'),
                ('lusin', 'Lusin'),
                ('meter', 'Meter'), ],
        required=False, )
    harga_beli = fields.Integer(
        string='Harga_beli', 
        required=False)
    harga_jual = fields.Integer(
        string='Harga_jual', 
        required=False)

    stok = fields.Integer(
        string='Stok',
        required=False)
    kadaluarsa = fields.Date(
        string='Kadaluarsa', 
        required=False)

    kurang = fields.Integer(
        compute="_compute_kurang",
        string='Kurang',
        required=False)

    penyambungpenjualan = fields.Many2one(
        comodel_name='minimarket.penjualandetail',
        string='penyambung',
        required=False)

    @api.depends('kode_produk')
    def _compute_produk(self):
        for a in self:
            a.keterangan_produk = a.kode_produk.nama_produk

    # @api.depends('stok')
    # def _compute_stok(self):
    #     for i in self:  # mapped = mengambil
    #         a = self.env['minimarket.penjualandetail'].search([('jumlah', '=', i.id)])
    #         b = self.env['minimarket.pembeliandetail'].search([('jumlah', '=', i.id)])
    #         i.stok = abs(i.stok - a + b)

    @api.depends('kurang')
    def _compute_kurang(self):
        for i in self:
            # i.kurang = i.penyambungpenjualan.jumlah
            a = self.env['minimarket.penjualandetail'].search([('jumlah', '=', i.id)])
            i.kurang = a


