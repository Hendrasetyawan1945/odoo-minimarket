from odoo import fields, models, api


class penjualan(models.Model):
    _name = 'minimarket.penjualan'
    _description = 'Description'

    no_notaids = fields.One2many(
        comodel_name='minimarket.penjualandetail',
        inverse_name='nota_id',
        string='No Nota ids',
        required=False)
    tgl_nota = fields.Datetime(
        string='Tanggal Nota',
        required=False,
        default=fields.Datetime.now())
    total_bayar = fields.Integer(
        string='Total_bayar',
        required=False)
    kode_pelanggan= fields.Many2one(
        comodel_name='minimarket.pelanggan',
        string='Kode Pelanggan',
        required=False)
