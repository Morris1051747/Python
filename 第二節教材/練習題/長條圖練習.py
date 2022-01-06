import openpyxl
from openpyxl.chart import BarChart, Reference
    
wb = openpyxl.load_workbook('長條圖練習.xlsx')
sheet = wb.active

