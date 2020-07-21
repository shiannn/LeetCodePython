import xlwt

book = xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet = book.add_sheet('mysheet',cell_overwrite_ok=True)
sheet.write(0,0,'日期')
sheet.write(0,1,'100元裝盒數')
sheet.write(0,2,'120元裝盒數')
sheet.write(0,3,'150元裝盒數')
sheet.write(0,4,'蝦販收購')
sheet.write(0,5,'購買耗材')

book.save('./test.xls')