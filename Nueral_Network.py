import pandas as pd
import numpy as np
import seaborn as sns
# Reading data 
Concrete = pd.read_csv("E:\\Bokey\\Excelr Data\\Python Codes\\all_py\\Neural Networks\\concrete.csv")
Concrete.head()

#
Concrete.describe()

# boxplots for each independent variables 
sns.boxplot(Concrete.cement)
sns.boxplot(Concrete.slag)
sns.boxplot(Concrete.ash)
sns.boxplot(Concrete.water)
sns.boxplot(Concrete.superplastic)

# Scatter plot between all possible independent variables and histogram for each independent variable
sns.pairplot(Concrete)

# Correlation values 
Concrete.corr()

colnames = list(Concrete.columns)
colnames
predictors = colnames[:8]
target = colnames[8]

Y = np.asarray(Concrete[target], dtype="|S6")
X = np.asarray(Concrete[predictors])

from sklearn.neural_network import MLPClassifier

clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(3), random_state=1)
clf.fit(X,Y)

pred_values = clf.predict(X)


#### Predicted scores
clf.score(X,Y)
# 10 hidden layers suits best for predicting the strength of the 
# concrete
# as the hidden layers increases the accuracy of the model decreases
np.sqrt(np.mean((pred_values-Concrete[predictors])))
pred_values = int(pred_values)
