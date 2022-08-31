from odoo import fields, models, api


class pembelian(models.Model):
    _name = 'minimarket.pembelian'
    _description = 'Description'
    _rec_name = 'kode_pemasok'


    no_masuk_ids = fields.One2many(
        comodel_name='minimarket.pembeliandetail',
        inverse_name='no_pembelian',
        string='No Masuk Ids',
        required=False)

    tgl_masuk = fields.Datetime(
        string='Tanggal Masuk',
        required=False,
        default=fields.Datetime.now())
        
    kode_pemasok = fields.Many2one(
        comodel_name='minimarket.pemasok',
        string='Kode_pemasok',
        required=False)
    kode_spec = fields.Char(string=' Kode Spec')
    kode_provinsi = fields.Char(string='Kode Provinsi',
                                compute="_compute_kp")
    kode_keteranganasal = fields.Char(string='Kode asal',
                                omchange='_onchange_asal')
    total = fields.Integer(
        compute='_compute_total',
        string='Total',
        required=False)
        
    user_id = fields.Many2one(
        comodel_name='minimarket.pengguna',
        string='User id',
        required=False)
    
    @api.depends('kode_provinsi')
    def _compute_kp(self):
        for record in self:
            record.kode_provinsi = record.kode_pemasok.kode_provinsi
    
    @api.onchange('kode_pemasok', 'kode_spec')
    def _onchange_asal(self):
        if (self.kode_pemasok.kode_pemasok):
            self.kode_keteranganasal = str(self.kode_pemasok.kode_pemasok) + str(self.kode_spec)
        else :
            self.kode_keteranganasal = ""

        
    @api.depends('total')
    def _compute_total(self):
        for record in self:
            a = sum(self.env['minimarket.pembeliandetail'].search(
                [('no_pembelian', '=', record.id)]).mapped('subtotal'))
            record.total = a
    

    
    
