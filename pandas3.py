"""
read_csv
read_excel
read_hdf
read_sql
read_json
read_msgpack(experimental)
read_html
read_gbq(experimental)
read_stata
read_sas
read_clipboard
read_pickle
"""
import pandas as pd
import xlrd

df = pd.read_excel(r'D:\工作\项目\a72\c02.xls')
print(df)
