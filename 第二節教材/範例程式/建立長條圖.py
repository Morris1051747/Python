import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

for i in range(1, 6):
    sheet.append([i])

from openpyxl.chart import BarChart, Reference

data = Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=5)

chart = BarChart()

chart.add_data(data)

chart.title = "好大的長條圖"
chart.x_axis.title = '他們越來越高'
chart.y_axis.title = 'HAHA'
chart.legend = None

sheet.add_chart(chart, "E2")

wb.save("長條圖.xlsx")

