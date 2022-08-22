from odoo import fields, models, api


class produk(models.Model):
    _name = 'minimarket.produk'
    _description = 'Description produk'

    kode_produk_ids = fields.One2many(
        comodel_name='minimarket.barang',
        inverse_name='kode_produk',
        string='Kode_produk_ids',
        required=False)
    kode_grup = fields.Many2one(
        comodel_name='minimarket.grup',
        string='Kode_grup',
        required=False)
    # kode_grub = fields.Many2one(
    #     comodel_name='minimarket.grup',
    #     string='Kode_grub',
    #     required=False)
    nama_produk = fields.Char(
        string='Nama_produk', 
        required=False)
