from odoo import api, fields, models


class manusia(models.Model):
    _name = 'minimarket.manusia'
    _description = 'New Description'

    name = fields.Char(string='Name')
    gender = fields.Selection(string='Gender',
                    selection=[('male', 'Male'), ('female', 'Female')])
    alamat = fields.Char(string='Alamat')