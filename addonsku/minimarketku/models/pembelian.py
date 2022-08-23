from odoo import fields, models, api


class pembelian(models.Model):
    _name = 'minimarket.pembelian'
    _description = 'Description'

    no_masuk_ids = fields.One2many(
        comodel_name='minimarket.pembeliandetail',
        inverse_name='no_masuk',
        string='No Masuk Ids',
        required=False)
    tgl_masuk = fields.Datetime(
        string='Tanggal Masuk',
        required=False,
        default=fields.Datetime.now())
    kode_pemasok = fields.Many2one(
        comodel_name='minimarket.pemasok',
        string='Kode_pemasok',
        required=False)
    total = fields.Integer(
        string='Total',
        required=False)
    user_id = fields.Many2one(
        comodel_name='minimarket.pengguna',
        string='User id',
        required=False)


    
    
    