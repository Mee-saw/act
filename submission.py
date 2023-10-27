import pandas as pd
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer

#final data with updated values
final = pd.read_csv('Codelistupd.csv')
final["CodeList"].fillna("",inplace=True) ## Incase if it contain any NaN values


def remove_classes_from_mlb(mlb, data, classes_to_remove):
    """
    Remove specified classes from a fitted MultiLabelBinarizer and the transformed data.

    Parameters:
    - mlb: A fitted MultiLabelBinarizer object
    - data: The dataset (already transformed using the mlb)
    - classes_to_remove: List of classes to remove

    Returns:
    - Filtered dataset with the specified classes removed
    """
    # Get indices of classes to remove
    indices_to_remove = [mlb.classes_.tolist().index(c) for c in classes_to_remove if c in mlb.classes_]

    # Remove the classes from the transformed data
    filtered_data = np.delete(data, indices_to_remove, axis=1)

    # Update the classes_ attribute of the mlb
    mlb.classes_ = np.delete(mlb.classes_, indices_to_remove)

    return filtered_data


mlb = MultiLabelBinarizer()
s1 = final["CodeList"]
t1 = mlb.fit_transform(s1)
filtered_data = remove_classes_from_mlb(mlb, t1, ['\t', '\n', '\r'])

submission = pd.DataFrame(filtered_data)
print(submission.shape)
print(list(mlb.classes_))

submission.to_csv("submission5.csv",index=False)