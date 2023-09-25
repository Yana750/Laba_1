import pandas as pd

wayname = './lab_pi_101.xlsx'
wb = pd.read_excel(wayname)

groups_column = wb["Группа"]
groups_name=input("Номер группы = ")
all_estimate = wb["Оценка"]
group_estimate = wb[groups_column == groups_name].shape[0]