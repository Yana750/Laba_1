from openpyxl import load_workbook
import pandas as pd

wb = load_workbook('lab_pi_101.xlsx')
a=5

print(wb.get_sheet_names())