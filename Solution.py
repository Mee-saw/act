import pandas as pd
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer

#final data with updated values
final = pd.read_csv('Codelistupd.csv')
final["CodeList"].fillna("",inplace=True) ## Incase if it contain any NaN values

mlb = MultiLabelBinarizer()
s1 = final["CodeList"]
t1 = mlb.fit_transform(s1)
submission = pd.DataFrame(t1)
print(submission.shape)
print(list(mlb.classes_))