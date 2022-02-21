import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.model_selection import train_test_split


iris = load_iris()
X = iris.data
y = iris.target


class Node:
    
    def __init__(self, X, y, gini):
        self.X = X
        self.y = y
        self.gini = gini
        self.feature_index = 0
        self.threshold = 0
        self.left = None
        self.right = None




class MyDecisionTreeClassifier:
    
    def __init__(self, max_depth):
        self.max_depth = max_depth



    def test_split(self, index, value, dataset):
        left_group, right_group = list(), list()
        for row in dataset:
            if row[index] < value:
                left_group.append(row)
            else:
                right_group.append(row)
        return left_group, right_group

    def gini_index(self, groups, classes):
        instances = float(sum([len(group) for group in groups]))
        gini = 0.0
        for group in groups:
            size = float(len(group))
            if size == 0:
                continue
            score = 0.0
            for class_val in classes:
                p = [row[-1] for row in group].count(class_val) / size
                score += p * p
            gini += (1.0 - score) * (size / instances)
        return gini

    # Select the best split point for a dataset
    def get_split(self, X, y):
        dataset = []
        for i in range(len(X)):
            dataset.append(X[i])
        for i in range(len(dataset)):
            dataset[i].append(y[i])
        print(len(dataset))
        class_values = list(set(row[-1] for row in dataset))
        desired_index, desired_value, desired_score, desired_groups = 999, 999, 999, None
        for index in range(len(dataset[0])):
            for row in dataset:
                groups = self.test_split(index, row[index], dataset)
                gini = self.gini_index(groups, class_values)
                if gini < desired_score:
                    desired_index, desired_value, desired_gini, desired_groups = index, row[index], gini, groups
        return {'index':desired_index, 'value':desired_value, 'gini': desired_gini, 'groups':desired_groups}
    
    
    def build_tree(self, X, y, depth = 0):
        
        # create a root node
        
        root = Node(X, y, 1)

        result = self.get_split(X, y)
        groups = result["groups"]
        gini = result["gini"]

        left = [element for element in groups[0]]
        right = [element for element in groups[1]]
        
        left_class = [element[-1] for element in groups[0]]        
        right_class = [element[-1] for element in groups[1]]

        if gini == 0.0 or depth == self.max_depth:
            node = Node(X, y, gini)
            print(f"Created leaf {depth}, 0_amount: {(right_class+left_class).count(0)}, 1_amount: {(right_class+left_class).count(1)}, 2_amount: {(right_class+left_class).count(2)}, gini: {gini}")
            return node

        print(f"Created node {depth}, 0_amount: {(right_class+left_class).count(0)}, 1_amount: {(right_class+left_class).count(1)}, 2_amount: {(right_class+left_class).count(2)}, gini: {gini}")
        root.left = self.build_tree(left, left_class, depth=depth + 1)
        root.right = self.build_tree(right, right_class, depth=depth + 1)


        # recursively split until max depth is not exeeced
        
        return root
    
    def fit(self, X, y):
        
        # basically wrapper for build tree
        # root = self.build_tree(X, y)


        pass
    
    def predict(self, X_test):
        
        # traverse the tree while there is left node
        # and return the predicted class for it, 
        # note that X_test can be not only one example
        pass
X, y = X.tolist(), y.tolist()
dataset = [[5.1, 3.5, 1.4, 0.2, 0], [4.9, 3.0, 1.4, 0.2, 0], [4.7, 3.2, 1.3, 0.2, 0], [4.6, 3.1, 1.5, 0.2, 0], [5.0, 3.6, 1.4, 0.2, 0], [5.4, 3.9, 1.7, 0.4, 0], [4.6, 3.4, 1.4, 0.3, 0], [5.0, 3.4, 1.5, 0.2, 0], [4.4, 2.9, 1.4, 0.2, 0], [4.9, 3.1, 1.5, 0.1, 0], [5.4, 3.7, 1.5, 0.2, 0], [4.8, 3.4, 1.6, 0.2, 0], [4.8, 3.0, 1.4, 0.1, 0], [4.3, 3.0, 1.1, 0.1, 0], [5.8, 4.0, 1.2, 0.2, 0], [5.7, 4.4, 1.5, 0.4, 0], [5.4, 3.9, 1.3, 0.4, 0], [5.1, 3.5, 1.4, 0.3, 0], [5.7, 3.8, 1.7, 0.3, 0], [5.1, 3.8, 1.5, 0.3, 0]]   

