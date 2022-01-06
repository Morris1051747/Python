import openpyxl
from openpyxl.chart import LineChart, Reference

wb = openpyxl.load_workbook('模擬考成績.xlsx')
sheet = wb.active

data = Reference(sheet, min_col=2, min_row=1, max_col=4, max_row=7)

chart = LineChart()
chart.add_data(data, titles_from_data=True)

chart.title = "模擬考成績趨勢"

chart.y_axis.title = '總級分'

chart.x_axis.title = '模擬考'

sheet.add_chart(chart, "B9")

wb.save("成績折線圖.xlsx")

