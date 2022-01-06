import openpyxl

book = openpyxl.Workbook()

sheet = book.active

rows = [
    ('學號', '姓名', '分數'),
    (78001, '大欣恆', 69),
    (78002, '魯文文', 87),
    (78003, '杜美欣', 88)
]

for row in rows:
    sheet.append(row)
    
book.save('成績表.xlsx')

for row in sheet.iter_rows(min_row=1, min_col=1, max_row=4, max_col=3):

    data = []

    for cell in row:
        print(cell.value, end=" ")
        data.append(cell.value)
    print()
    
