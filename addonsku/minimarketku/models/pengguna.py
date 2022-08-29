from odoo import fields, models, api


class pengguna(models.Model):
    _name = 'minimarket.pengguna'
    _description = 'Description'

    name = fields.Char(
        string='Id', 
        required=False)
    passid = fields.Integer(
        string='Passid',
        required=False)
    nama = fields.Char(
        string='Nama',
        required=False)
    jk = fields.Selection(string='Jenis Kelamin', 
    selection=[('laki-laki', 'Laki-laki'), 
    ('perempuan', 'Perempuan')])
    level = fields.Selection(
        string='Level',
        selection=[('gold', 'Gold'),
                ('silver', 'Silver'),
                ('bronze', 'Bronze'),],
        required=False, )

