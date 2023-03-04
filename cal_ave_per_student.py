import pandas as pd

stu_scores = pd.read_csv('my_database_score.csv')
stu_scores.columns = ['id', 'stu_id', 'course_id', 'num']
stu_ave_score = stu_scores.groupby('stu_id')['num'].mean()
stu_ave_score.to_csv('stu_ave_score.csv')




