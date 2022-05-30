import pandas as pd  #to read csv files

import numpy as np  #used for working with arrays

import matplotlib.pyplot as plt  #for data visualization and graphical plotting library 
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

df=pd.read_csv("LinearRegression\AppleStock.csv")
df.head() #show first 5 rows by defult
df.tail() #show last 5 rows by defult

df = df[['Total Trade Quantity','Turnover (Lacs)']] 

df.columns=['volume','turnover'] #rename columns

x=np.array(df['volume']).reshape(-1,1) #independant variable

y=np.array(df['turnover'])  #dependant variable

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred =model.predict(X_test) #predict response 

result = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

print(result)


print('The Accuracy of the Model: ', model.score(X_test, y_test))

#Visulization
plt.scatter(X_test,y_test,color='r')

plt.plot(X_test, y_pred ,color='k')
plt.title('volume vs turnover')
plt.xlabel('volume')
plt.ylabel('turnover')
plt.show()