from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'minimarket.pengguna'
    _description = 'Description'

    userid_ids = fields.One2many(
        comodel_name='minimarket.pembelian',
        inverse_name='user_id',
        string='User Ids',
        required=False)
    id = fields.Char(
        string='Id', 
        required=False)
    passid = fields.Integer(
        string='Passid',
        required=False)
    nama = fields.Char(
        string='Nama',
        required=False)
    level = fields.Integer(
        string='Level',
        required=False)
