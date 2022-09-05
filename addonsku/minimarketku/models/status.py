from odoo import api, fields, models


class status(models.Model):
    _inherit = 'res.partner'
    _description = 'New Description'

    status_pekerjaan = fields.Selection(string='status_pekerjaan',
                    selection=[('tetap', 'Tetap'), ('kontrak', 'Kontrak'), ('magang', 'Magang')])
