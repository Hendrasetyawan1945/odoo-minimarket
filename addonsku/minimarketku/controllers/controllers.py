from crypt import methods
from odoo import http, models, fields
from odoo.http import request
import json


class Minimarketku(http.Controller):
    @http.route('/minimarketku/get_barang', auth='public', method=['GET'])
    def getbarang(self, **kw):
        barang = request.env['minimarket.barang'].search([])
        isi = []
        for a in barang:
            isi.append({
                'namabarang' : a.nama_barang,
                'satuan' : a.satuan,
                'hargab' : a.harga_beli,
                'hargaj' : a.harga_jual,
                'stok' : a.stok
            })
        return json.dumps(isi)    


    # @http.route('/minimarketku/minimarketku/objects/', auth='public')
    # def list(self, **kw):
    #     return http.request.render('minimarketku.listing', {
    #         'root': '/minimarketku/minimarketku',
    #         'objects': http.request.env['minimarketku.minimarketku'].search([]),
    #     })

    # @http.route('/minimarketku/minimarketku/objects/<model("minimarketku.minimarketku"):obj>/', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('minimarketku.object', {
    #         'object': obj
    #     })
