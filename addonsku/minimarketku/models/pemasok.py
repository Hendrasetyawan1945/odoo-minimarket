from odoo import fields, models, api


class pemasok(models.Model):
    _name = 'minimarket.pemasok'
    _description = 'Description'
    _rec_name = 'kode_pemasok'

    kode_pemasok = fields.Char(
        string='Kode_pemasok',
        required=False)
        
    kode_pembelian_ids = fields.One2many(
        comodel_name='minimarket.pembelian',
        inverse_name='kode_pemasok',
        string='Kode_pembelian_ids',
        required=False)

    nama_pemasok = fields.Char(
        string='Nama_pemasok',
        required=False)
    alamat = fields.Char(
        string='Alamat',
        required=False)
    kota = fields.Char(
        string='Kota',
        required=False)
    kode_provinsi = fields.Selection(string='Kode provisi', 
    selection=[('01', '01'), ('02', '02'),
            ('03', '03'), ('04', '04'),
        ('05', '05'), ('06', '06'), ],
        required=True)
    provinsi = fields.Char(
        onchange='_onchange_kp',
        string='Provinsi',
        required=False)
    no_tlpn = fields.Char(
        string='No_tlpn',
        required=False)
    no_fak = fields.Char(
        string='No_fak',
        required=False)
    kontak_kp = fields.Char(
        string='Kontak_kp',
        required=False)
    barang_ids = fields.Many2many(comodel_name='minimarket.barang', string='Supply Barang')

    @api.onchange('kode_provinsi')
    def _onchange_kp(self):
        if (self.kode_provinsi == '01'):
            self.provinsi = 'DKI Jakarta'
        elif (self.kode_provinsi == '02'):
            self.provinsi = 'Jawa Barat'
        elif (self.kode_provinsi == '03'):
            self.provinsi = 'DI Yogyakarta'
        elif (self.kode_provinsi == '04'):
            self.provinsi = 'Jawa Timur'
        elif (self.kode_provinsi == '05'):
            self.provinsi = 'Nangroe Aceh Darusalam'
        elif (self.kode_provinsi == '06'):
            self.provinsi = 'Sumatera Barat'
