import pandas as pd

# Read the CSV file
data = pd.read_csv('c:\\Kaggle Machine Learning\\Richter\'s Predictor Modeling Earthquake Damage\\submission4.csv')

# Count the number of rows in each class of damage_grade
class_counts = data['damage_grade'].value_counts()

# Print the result
print(class_counts)

total = class_counts.sum()
weights = total / class_counts

print(total)
print(weights)

# # damage_grade
# # 2    57439
# # 3    23564
# # 1     5865
# # Name: count, dtype: int64
# # 86868
# # damage_grade
# # 2     1.512352
# # 3     3.686471
# # 1    14.811253
# # Name: count, dtype: float64


# damage_grade
# 2    56414
# 3    24058
# 1     6396
# Name: count, dtype: int64
# 86868
# damage_grade
# 2     1.539831
# 3     3.610774
# 1    13.581614
# Name: count, dtype: float64

# Read the CSV file
data2 = pd.read_csv('c:\\Kaggle Machine Learning\\Richter\'s Predictor Modeling Earthquake Damage\\train_labels.csv')

# Count the number of rows in each class of damage_grade
class_counts = data2['damage_grade'].value_counts()

# Print the result
print(class_counts)

total = class_counts.sum()
weights = total / class_counts

print(total)
print(weights)

# damage_grade
# 2    148259
# 3     87218
# 1     25124
# Name: count, dtype: int64
# 260601
# damage_grade
# 2     1.757742
# 3     2.987927
# 1    10.372592
# Name: count, dtype: float64


# damage_grade
# 2    148259
# 3     87218
# 1     25124
# Name: count, dtype: int64
# 260601
# damage_grade
# 2     1.757742
# 3     2.987927
# 1    10.372592
# Name: count, dtype: float64