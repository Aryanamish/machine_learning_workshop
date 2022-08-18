import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

class Model:
    def __init__(self):
        self.mt_dicision = DecisionTreeClassifier()

    def train(self):
        df = pd.read_csv('../day2/diabetes.csv')
        df.columns = df.columns.str.lower()



        X = df.iloc[:,0:-1]
        Y = df.iloc[:,-1:]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X,Y, test_size=0.10)
        # y_test

        
        self.mt_dicision.fit(self.X_train, self.y_train)
        self.mt_prediction = self.mt_dicision.predict(self.X_test)

    def accuracy(self):
        return accuracy_score(self.mt_prediction, self.y_test)

    def predict(self, data):
        return self.mt_dicision.predict(data)


if __name__ == '__main__':
    diabities = Model()
    diabities.train()
    
    print(f"Accuracy = {diabities.accuracy()}")