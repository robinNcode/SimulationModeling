import pandas
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = pandas.read_csv('insurence_dataset.csv')

x = data[['age']]
y = data['bought_insurance']

# ploting the data
plt.scatter(x, y, marker='+', color='red')
plt.xlabel('Age')
plt.ylabel('Bought Insurance')
# plt.show()

# splitting the data into train and test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=0)

# training the model
model = LogisticRegression()
model.fit(x_train, y_train)

# predicting the results
y_pred = model.predict(x_test)
print(f'bought_insurance prediction = {y_pred}')
print(y_test)

# plotting the results
plt.scatter(x_test, y_test, marker='+', color='black')
plt.show()
# accuracy of the model
print(model.score(x_test, y_test))


