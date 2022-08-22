from odoo import fields, models, api


class grup(models.Model):
    _name = 'minimarket.grup'
    _description = 'Description'
    
    kode_grup_ids = fields.One2many(
        comodel_name='minimarket.produk',
        inverse_name='kode_grup',
        string='Kode Grup Ids',
        required=False)
    # kode_grup_ids = fields.One2many(
    #     comodel_name='minimarket.produk',
    #     inverse_name='kode_grup',
    #     string='Kode_grup_ids',
    #     required=False)
    nama_grup = fields.Char(
        string='Nama_grup', 
        required=False)
