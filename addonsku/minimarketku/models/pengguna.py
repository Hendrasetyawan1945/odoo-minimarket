from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'minimarket.pengguna'
    _description = 'Description'

    id = fields.Char(
        string="ID"
    )
    userid = fields.Integer(
        string='User id',
        required=False)
    passid = fields.Integer(
        string='Passid',
        required=False)
    nana = fields.Char(
        string='Nama',
        required=False)
    level = fields.Integer(
        string='Level',
        required=False)
