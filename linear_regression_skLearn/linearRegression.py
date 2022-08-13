import pandas
import matplotlib.pyplot as plt
# to training or testing the data
from sklearn.model_selection import train_test_split
# for linear regression ..
from sklearn.linear_model import LinearRegression

# reading data ...
# data = pandas.read_csv('/content/drive/MyDrive/Colab Notebooks/code/smiulationandmodel/house_pricing.csv')
data = pandas.read_csv('house_pricing.csv')

# plotting the data ...
plt.title("Initial ratio of house pricing")
plt.xlabel('area')
plt.ylabel('price')
plt.scatter(data["area"], data["price"])

plt.show()

# specify dependent or independent by giving extra []
x = data[['area']]
y = data['price']

# splitting the data
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=.3, random_state=1)

# linear regression starts here ..
reg = LinearRegression()

# to train fit function is used here ...
reg.fit(xTrain, yTrain)

# to test predict function is used here ...
print(reg.predict(xTest))
print(yTest)
