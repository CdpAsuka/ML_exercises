#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :pyModel2VBA.py
# @Time      :23/11/20 13:51
# @Author    :cc


from sklearn import datasets
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
import m2cgen as m2c

seed = 2020
test_size = 0.3
X, Y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)
# fit model on training data
model = XGBRegressor()
model.fit(X_train, y_train)

X_pre1 = [0.016280675727306498, 0.03081082953138418, -0.06363517019512076, 0.056238598688520124, -0.009147093429829445,
          -0.016412170331868287, 0.038075906433423026, 0.001750521923228816, -0.005514554978810025, 0.07803382939463664]

X_pre2 = [0.03081082953138418, -0.06363517019512076, 0.056238598688520124, -0.009147093429829445, -0.016412170331868287,
          0.038075906433423026, 0.001750521923228816, -0.005514554978810025, 0.07803382939463664, -0.027309785684926546]

print(model.predict([X_pre1, X_pre2]))
code = m2c.export_to_visual_basic(model, function_name='pred')
print(code)
