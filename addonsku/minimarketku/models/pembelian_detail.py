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
    harga_beli = fields.Integer(
        string='Harga_beli',
        required=False)
    jumlah = fields.Integer(
        string='Jumlah',
        required=False)
    subtotal = fields.Integer(
        string='Subtotal',
        required=False)
