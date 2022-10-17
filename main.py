import openpyxl
import pandas
src = 'files/20211015_COJ-Parcel-Data_Website.xlsx'
# df = pandas.read_excel(src)
# print(df.to_string(),)
wb = openpyxl.load_workbook(src)
sheet = wb.active
dataset = []
for row in sheet.iter_rows(values_only=True):
    if row[0] is not None:
        map_key = row[0]
    if row[1] is not None:
        row = list(row)
        if row[0] is None:
            row[0] = map_key
        print(row)
        dataset.append(row)
print(dataset)
df = pandas.DataFrame(data=dataset[1:],columns=dataset[0])
df.to_csv('files/dia_props.csv', index=False)


