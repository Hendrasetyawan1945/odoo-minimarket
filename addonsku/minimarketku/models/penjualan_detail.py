from odoo import fields, models, api


class penjualandetail(models.Model):
    _name = 'minimarket.penjualandetail'
    _description = 'Description penjualan detail'

    nota_id = fields.Many2one(
        comodel_name='minimarket.penjualan',
        string='Nota_id',
        required=False)
    harge_jual = fields.Integer(
        string='Harge_jual',
        required=False)
    jumlah = fields.Integer(
        string='Jumlah',
        required=False)
    subtotal = fields.Integer(
        string='Subtotal',
        required=False)