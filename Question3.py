import pandas as pd

#Reading data from csv file
foot_ball = pd.read_csv("C:/Users/Sibonelo Faye/Desktop/tp2_test_1/dataset - 2020-09-24.csv")
print(foot_ball.tail(7))

#3.3.1
print(foot_ball["Nationality"])
print(foot_ball["Club"])

#3.3.2
print(foot_ball.loc[10,"Name"])


