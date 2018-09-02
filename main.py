import pandas as pd
import numpy as np
from  sklearn.cross_validation import train_test_split
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures

train = pd.read_csv('train_NIR5Yl1.csv')
train = train.drop(train[train.Views > 3000000].index)

     
labelencoder_X = LabelEncoder()
train['Tag'] = labelencoder_X.fit_transform(train['Tag'])
train.drop(['ID','Username'], axis=1,inplace =True)
target = train['Upvotes']

from sklearn.preprocessing import Binarizer
bn = Binarizer(threshold=7)
pd_watched = bn.transform([train['Answers']])[0]
train['pd_watched'] = pd_watched


feature_names = [x for x in train.columns if x not in ['Upvotes']]

x_train, x_val, y_train, y_val = train_test_split(train[feature_names], target,test_size = 0.22,random_state =205)
sc_X = StandardScaler()
x_train = sc_X.fit_transform(x_train)
x_val = sc_X.transform(x_val)

poly_reg = PolynomialFeatures(degree = 4,interaction_only=False, include_bias=True)
X_poly = poly_reg.fit_transform(x_train)
poly_reg.fit(x_train, y_train)
lin_reg_1 = linear_model.LassoLars(alpha=0.021,max_iter=150)
lin_reg_1.fit(X_poly, y_train)

# predicitng 
pred_val = lin_reg_1.predict(poly_reg.fit_transform(x_val))

print(r2_score(y_val, pred_val))

# ---------------------------------------------------------------------------------------

# testing

test = pd.read_csv('test_8i3B3FC.csv')
ids = test['ID']
test.drop(['ID','Username'], axis=1,inplace =True)


labelencoder_X = LabelEncoder()
test['Tag'] = labelencoder_X.fit_transform(test['Tag'])

from sklearn.preprocessing import Binarizer
bn = Binarizer(threshold=7)
pd_watched = bn.transform([test['Answers']])[0]
test['pd_watched'] = pd_watched

   
test = sc_X.fit_transform(test)

pred_test = lin_reg_1.predict(poly_reg.fit_transform(test))
pred_test=abs(pred_test)


submission = pd.DataFrame({'ID': ids,
                           'Upvotes':pred_test
                           })

submission.to_csv("final_sub477.csv",index=False)
