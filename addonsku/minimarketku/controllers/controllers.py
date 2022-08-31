# from crypt import methods
# from odoo import http, models, fields
# from odoo.http import request
# import json


# class Minimarketku(http.Controller):
#     @http.route('/minimarketku/get_barang', auth='public', method=['GET'])
#     def getbarang(self, **kw):
#         barang = request.env['minimarket.barang'].search([])
#         isi = []
#         for a in barang:
#             isi.append({
#                 'namabarang' : a.nama_barang,
#                 'satuan' : a.satuan,
#                 'hargab' : a.harga_beli,
#                 'hargaj' : a.harga_jual,
#                 'stok' : a.stok
#             })
#         return json.dumps(isi)

#     @http.route('/minimarketku/get_pemasok', auth='public', method=['GET'])
#     def getbarang(self, **kw):
#         pemasok= request.env['minimarket.pemasok'].search([])
#         isi = []
#         for a in pemasok:
#             isi.append({
#                 'kode_pemasok': a.kode_pemasok,
#                 'nama_pemasok': a.nama_pemasok,
#                 'alamat': a.alamat,
#                 # 'kode_provinsi': a.kode_provinsi,
#                 # 'provinsi': a.provinsi
#             })
#         return json.dumps(isi)

#     @http.route('/minimarketku/get_pengguna', auth='public', method=['GET'])
#     def getbarang(self, **kw):
#         pengguna = request.env['minimarket.pengguna'].search([])
#         daftar = []
#         for a in pengguna:
#             daftar.append({
#                 'name': a.name,
#                 'jk': a.jk,
#                 'level': a.level,
#             })
#         return json.dumps(daftar)

    # @http.route('/minimarketku/penjualan', auth='public', method=['GET'])
    # def getpenjualan(self, **kw):
    #     penjualan = request.env['minimarket.penjualan'].search([])
    #     daftar = []
    #     for a in penjualan:
    #         daftar.append({
    #             'tgl_nota': a.tgl_nota,
    #             'total_bayar': a.total_bayar,
    #             'kode_pelanggan': a.kode_pelanggan,
    #             'membership': a.membership
    #         })
    #     return json.dumps(daftar)


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
