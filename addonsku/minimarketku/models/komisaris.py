from odoo import api, fields, models


class komisaris(models.Model):
    _inherit = 'res.partner'
    _description = 'New Description'

    jabatan = fields.Selection(string='Jabatan', 
    selection=[('komut', 'Komisaris Utama'), ('anggota', 'Komisaris')])