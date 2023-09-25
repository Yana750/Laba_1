import pandas as pd

wayname = './lab_pi_101.xlsx'
wb = pd.read_excel(wayname)

groups_column = wb["Группа"]
groups_name=input("Номер группы = ")
all_estimate = wb["Оценка"]
group_estimate = wb[groups_column == groups_name].shape[0]
student_number = wb[groups_column == groups_name]["Личный номер студента"]
unique_student_number = student_number.unique()
unique_control_level = wb["Уровень контроля"].unique()
unique_years = sorted(wb["Год"].unique())
output=(f"В исходном датасете содержалось {all_estimate.size} оценок, из них {group_estimate} оценок относятся к группе ПИ101\n"
f"Используемые формы контроля: {unique_control_level}\n"
f"Данные представлены по следующим учебным годам: {sorted(unique_years)}")
print(output)