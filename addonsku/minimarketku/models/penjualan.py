from odoo import fields, models, api


class penjualan(models.Model):
    _name = 'minimarket.penjualan'
    _description = 'Description'
    _rec_name = 'kode_pelanggan'
   #_rec_name = 'no_notaids'

    no_notaids = fields.One2many(
        comodel_name='minimarket.penjualandetail',
        inverse_name='no_penjualan',
        string='No Penjualan Ids',
        required=False)

    tgl_nota = fields.Datetime(
        string='Tanggal Nota',
        required=False,
        default=fields.Datetime.now())
    total_bayar = fields.Integer(
        compute="_compute_totalbayar",
        string='Total_bayar',
        required=False)

    kode_pelanggan = fields.Many2one(
        comodel_name='minimarket.pelanggan',
        string='Kode Pelanggan',
        required=False)

    @api.depends('total_bayar')
    def _compute_totalbayar(self):
        for record in self:
            a = sum(self.env['minimarket.penjualandetail'].search(
                [('no_penjualan', '=', record.id)]).mapped('subtotal'))
            record.total_bayar = a
