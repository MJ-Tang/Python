import pandas as pd

print("-"*30 + "import excel" + "-"*30)

# df = pd.read_excel(r"/Users/tangmingjun/dev/python/excel/everyDayPrice.xlsx")
# print('1.date of excel is:',"*"*15)
# print(df,"\n")

# df = pd.read_excel(r"/Users/tangmingjun/dev/python/excel/everyDayPrice.xlsx",sheet_name = 0)
# print('2.date of excel is:',"*"*15)
# print(df,"\n")

# df = pd.read_excel(r"/Users/tangmingjun/dev/python/excel/everyDayPrice.xlsx",index_col= 0)
# print('2.date of excel is:',"*"*15)
# print(df,"\n")

# df = pd.read_excel(r"/Users/tangmingjun/dev/python/excel/everyDayPrice.xlsx",header = 1)
# print('2.date of excel is:',"*"*15)
# print(df,"\n")

# df = pd.read_excel(r"/Users/tangmingjun/dev/python/excel/everyDayPrice.xlsx",usecols = [0,2])
# print('2.date of excel is:',"*"*15)
# print(df,"\n")

df = pd.read_csv(r"/Users/tangmingjun/dev/python/excel/everyDayPrice.csv")
print('2.date of csv is:',"*"*15)
print(df,"\n")

# df = pd.read_csv(r"/Users/tangmingjun/dev/python/excel/everyDayPrice.csv", nrows = 3)
# print('2.date of csv is:',"*"*15)
# print(df,"\n")

# df = pd.read_csv(r"/Users/tangmingjun/dev/python/excel/everyDayPrice.csv", sep = ' ')
# print('2.date of csv is:',"*"*15)
# print(df,"\n")

print("-"*30 + "know date" + "-"*30)

print(df.head(3),'\n')
print(df.shape,'\n')
print(df.info(),'\n')


print('date')
print(df.describe(),'\n')



