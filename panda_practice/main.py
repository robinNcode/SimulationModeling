import pandas
import numpy as np

if __name__ == '__main__':
    # Define a dictionary containing employee data
    data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
            'Age': [27, 24, 22, 32],
            'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
            'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

    df = pandas.DataFrame(data)

    # Print the dataframe
    print(df[['Name', 'Qualification']])

    # dictionary of lists
    dict = {'First Score': [100, 90, np.nan, 95],
            'Second Score': [30, 45, 56, np.nan],
            'Third Score': [np.nan, 40, 80, 98]}

    numpyDf = pandas.DataFrame(dict)

    # check for null values
    print(numpyDf.isnull())

    # fill all null values with 0
    numpyDf = numpyDf.fillna(0)
    print(numpyDf)

    # Checking iteration over dataframe
    gameInfo = {'name': ["aparna", "pankaj", "sudhir", "Geeku"],
                'degree': ["MBA", "BCA", "M.Tech", "MBA"],
                'score': [90, 40, 80, 98]}

    gameDf = pandas.DataFrame(gameInfo)
    # iterating on rows
    for index, row in gameDf.iterrows():
        print(row['name'], row['degree'], row['score'])

    # iterating on columns
    for column in gameDf:
        print(column)
        print(gameDf[column])
