import numpy as np
import tensorflow as tf;
import pandas as pd
import mnist
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline


#Preparing the data for categorical analysis

data = pd.read_csv('data.csv')
train_y = data.COST_PER_DAY

train_x = data[['AVG_DIST','STAR_RATING','pos_value']]
final_data=[];

# print(train_x)
# print(train_y)
# print(len(train_y))
a = [1,0,0,0,0,0]
b = [0,1,0,0,0,0]
c = [0,0,1,0,0,0]
d = [0,0,0,1,0,0]
e = [0,0,0,0,1,0]
f = [0,0,0,0,0,1]

for i in range(len(data)):
    if(train_y[i]==1000):
        final_data.append(a);
    if(train_y[i]==3000):
        final_data.append(b);
    if(train_y[i]==5000):
        final_data.append(c);
    if(train_y[i]==6000):
        final_data.append(d);
    if(train_y[i]==9000):
        final_data.append(e);
    if(train_y[i]==12000):
        final_data.append(f);

print(len(final_data))


input_one_hot_encoded = np.array(train_x)
output_one_hot_encoded = np.array(final_data)



model = Sequential([
  Dense(64, activation='relu', input_shape=(3,)),
  Dense(64, activation='relu'),
  Dense(6, activation='softmax'),
])
# Compile the model.
model.compile(
  optimizer='adam',
  loss='categorical_crossentropy',
  metrics=['accuracy'],
)
# Train the model.
model.fit(
  input_one_hot_encoded,
  output_one_hot_encoded,
  epochs=500,
)

model.save_weights('model.h5')

