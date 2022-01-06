import openpyxl
from openpyxl.chart import BarChart, Reference
    
wb = openpyxl.load_workbook('成績表.xlsx')
sheet = wb.active
  
data = Reference(sheet, min_col=3, min_row=2, max_col=3, max_row=4)

categs = Reference(sheet, min_col=2, min_row=2, max_col=2, max_row=4)

chart = BarChart()
chart.add_data(data)
chart.set_categories(categs)

chart.varyColors = True

chart.title = "成績長條圖"

sheet.add_chart(chart, "D6")

wb.save("成績長條圖.xlsx")

