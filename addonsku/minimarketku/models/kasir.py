from odoo import api, fields, models


class kasir(models.Model):
    _name = 'minimarket.kasir'
    _inherit = 'minimarket.manusia'
    _description = 'New Description'

    id_pegawai = fields.Char(string='Id Pegawai')
    status_pegawai = fields.Selection(string='Status Pegawai', 
    selection=[('tetap', 'Tetap'), ('kontrak', 'Kontrak'),
                ('magang', 'Magang') ])
    