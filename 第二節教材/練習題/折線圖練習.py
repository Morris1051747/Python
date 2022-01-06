import openpyxl
from openpyxl.chart import LineChart, Reference

wb = openpyxl.load_workbook('折線圖練習.xlsx')
sheet = wb.active

