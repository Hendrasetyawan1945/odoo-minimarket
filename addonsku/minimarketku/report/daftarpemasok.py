
from odoo import models, fields


class daftarpemasok(models.AbstractModel):
    _name = 'report.minimarketku.report_pemasok_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl = fields.Date.today()
    def generate_xlsx_report(self, workbook, data, pemasok):

        sheet = workbook.add_worksheet('Daftar Pemasok')
        bold = workbook.add_format({'bold': True})
        italic = workbook.add_format({'italic': True})

        row = 1
        col = 0
        sheet.write(0, 0, str(self.tgl))
        sheet.write(row, col,"Nama Perusahaan", bold)
        sheet.write(row, col+1, "Kode Provinsi Perusahaan", bold)
        sheet.write(row, col+2, "Provinsi Perusahaan", bold)

        for obj in pemasok:
            row += 1
            col = 0
            sheet.write(row, col, obj.nama_pemasok)
            sheet.write(row, col+1, obj.kode_provinsi)
            sheet.write(row, col+2, obj.provinsi,italic)
            for i in obj.barang_ids:
                    sheet.write(row, col+3, i.nama_barang)
                    col +=1

