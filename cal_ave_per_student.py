import pandas as pd

stu_scores = pd.read_csv('stu_ave_score.csv')
stu_ave_score = stu_scores.groupby(['student.name']).mean()
stu_ave_score.to_csv('stu_ave_score.csv')

