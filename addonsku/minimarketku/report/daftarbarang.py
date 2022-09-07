
from odoo import models, fields


class daftarbarang(models.AbstractModel):
    _name = 'report.minimarketku.report_barang_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl = fields.Date.today()
    def generate_xlsx_report(self, workbook, data, b):

        sheet = workbook.add_worksheet('Daftar Barang xlsx')
        bold = workbook.add_format({'bold': True})
        italic = workbook.add_format({'italic': True})

        row = 1
        col = 0
        sheet.write(0, 0, str(self.tgl))
        sheet.write(row, col,"Kode barang", bold)
        sheet.write(row, col+1, "Nama_barang", bold)
        sheet.write(row, col+2, "Satuan", bold)
        sheet.write(row, col+3,"harga_beli", bold)
        sheet.write(row, col+4, "harga_jual", bold)
        sheet.write(row, col+5, "stok", bold)

        for obj in b:
            row += 1
            col = 0
            sheet.write(row, col, obj.kode_barang)
            sheet.write(row, col+1, obj.Nama_barang)
            sheet.write(row, col+2, obj.satuan)
            sheet.write(row, col+3, obj.harga_beli)
            sheet.write(row, col+4, obj.harga_jual)
            sheet.write(row, col+5, obj.stok)
            # for i in obj.barang_ids:
            #         sheet.write(row, col+3, i.nama_barang)
            #         col +=1

