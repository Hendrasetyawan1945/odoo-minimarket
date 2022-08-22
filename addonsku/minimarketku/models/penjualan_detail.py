from odoo import fields, models, api


class penjualandetail(models.Model):
    _name = 'minimarket.penjualandetail'
    _description = 'Description penjualan detail'

    nota_id = fields.Many2one(
        comodel_name='minimarket.penjualan',
        string='Nota_id',
        required=False)
    kode_barang_ids = fields.One2many(
        comodel_name='minimarket.barang',
        inverse_name='kode_barang',
        string='Kode_barang_ids',
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
        required=False)

    @api.depends('harga_jual')
    def _compute_hargajual(self):
        for a in self:
            a.harga_jual = a.kode_barang_ids.harga_jual