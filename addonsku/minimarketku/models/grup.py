from odoo import fields, models, api


class grup(models.Model):
    _name = 'minimarket.grup'
    _description = 'Description'
    _rec_name = 'nama_grup'

    kode = fields.Char(string='kode grup')
    
    produk_ids = fields.One2many(
        comodel_name='minimarket.produk',
        inverse_name='grup_id',
        string='Kode Grup Ids',
        required=False)
    nama_grup = fields.Char(
        string='Nama_grup', 
        required=False)

