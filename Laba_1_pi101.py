from openpyxl import load_workbook
import pandas as pd

pathname = './lab_pi_101.xlsx'
wb=pd.read_excel(pathname)
groups = wb["Группа"]
all_estimate = wb["Оценка"]
group_estimate=wb["Группа"].shape[0]