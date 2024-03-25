import pandas as pd

#Reading data from csv file
foot_ball = pd.read_csv("C:/Users/Sibonelo Faye/Desktop/tp2_test_1/dataset - 2020-09-24.csv")
print(foot_ball.tail(7))

#Question 3.3.1
print(foot_ball["Nationality"])
print(foot_ball["Club"])

#Question 3.3.2
print(foot_ball.loc[10,"Name"])

#Question 3.3.3
'''print("Player index 100")
print(foot_ball.loc[100,"Goals"])
print(foot_ball.loc[100,"Appearance"])

print("Player index 110")
print(foot_ball.loc[110,"Goals"])
print(foot_ball.loc[110,"Appearance"])'''

#Question 3.3.4
#foot_ball["Goals_Per_Appearance"] = []

#Question 3.3.5
print(foot_ball[foot_ball["Club"]=="Arsenal"])

#Question 3.3.6
#evens = list(filter(lambda x: x % 2 == 0, nums))
'''my_list = []
my_list.append(foot_ball[foot_ball["Goals"]])'''


print()








