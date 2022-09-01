from odoo import fields, models, api


class grup(models.Model):
    _name = 'minimarket.grup'
    _description = 'Description'
    _rec_name = 'nama_grup'

    kode = fields.Char(string='kode grup')
    kode_spec = fields.Char(string='Kode Spec')
    nama_grup = fields.Char(
        string='Nama_grup',
        required=False)
    kode_grup = fields.Char(string='kode grup',
                        onchange='_onchange_grub')
    
    produk_ids = fields.One2many(
        comodel_name='minimarket.produk',
        inverse_name='grup_id',
        string='Kode Grup Ids',
        required=False)

    @api.onchange('nama_grup', 'kode_spec')
    def _onchange_grub(self):
        self.kode_grup = str(self.nama_grup) + str(self.kode_spec)
