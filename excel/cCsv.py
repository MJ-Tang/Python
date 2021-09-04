from datetime import datetime
import pandas as pd
import datetime

print("-"*30 + "import excel" + "-"*30)

df = pd.read_excel(r"/Users/tangmingjun/dev/python/excel/everyDayPrice.xls")
print(df,"\n")
print(df.info(),'\n')
print(df.isnull(),'\n')
print(df.dropna(),'\n')
# print(df.dropna(how = 'all'),'\n')
print(df.fillna(0),'\n')

# dateTimeP = datetime.datetime.strptime('2020/7/20 00:00:00',r'%Y/%m/%d %H:%M%S')
# print(df.fillna({'日期':dateTimeP}))

df1 = pd.read_excel(r"/Users/tangmingjun/dev/python/excel/everyDayPrice.xls",sheet_name=1)
print(df1.drop_duplicates(subset = '日期', keep= 'last'),"\n")