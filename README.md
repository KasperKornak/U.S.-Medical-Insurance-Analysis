## Introduction

This repository is created for purposes of Data Science career path at codecademy. This is an updated version of first README file, since I felt that I left this code without any explanation nor analysis.

So, first things first: I was given a task to have fun and create few graphs to explore possible correlations between data that I received (it contained US Medical Insurance prices). My main challenge was to use as many dictionaries as possbile, to show that I have a good understanding of them. I won't be discussing code here, but I would like to list packages that I used in this small project:

- csv,
- matplotlib,
- numpy,
- setuptools (needed only if you want to have a jumpstart in installing packages)

To learn more about dataset that I used visit [Kaggle](https://www.kaggle.com/datasets/mirichoi0218/insurance).

## Running code

To run the program type: `python3 insurance_analysis.py` in your terminal. Program runs in a simple loop, in which you can choose from three analyses. This is how it looks after typing the command above:
<p align="center">
  <img width="402" alt="Zrzut ekranu 2022-06-10 o 20 37 37" src="https://user-images.githubusercontent.com/80947256/173129462-58a5a9eb-f194-4292-8d50-301d83018d1c.png">
</p>
Select graph or information that you would like to see. Graphs will pop up in new window (option number 2 and 3) and text analysis will be shown in terminal (option 1). 
After closing it, program will ask you whether to continue or not. Obviously, everyone can make typos sometimes, but no worries! Program is well-equipped to fight it! 😁

## Analysis
To start analyzing what's happening there, let me explain some of the data metrics:

- *price* - price of insurance in USD of considered person,
- *smoking status* - tells us if person smokes or not; 1 for smoking person, 0 for non-smoking person,
- *BMI* - Body Mass Index of considered person,

### What is the relationship between smoking status and insurance price?
<p align="center">
  <img width="558" alt="Zrzut ekranu 2022-06-10 o 21 00 45" src="https://user-images.githubusercontent.com/80947256/173132740-20831f14-ba0e-4ce5-a851-bc7dfd914bfd.png">
</p>
Comparing an average price of insurance between smoking and non-smoking people is a simple, yet quite powerful information. Obviously, I didn't take into account many other things like age or number of children, but I think that smoking not only kills you, but also kills your wallet.

### What is the relationship between person's BMI and insurance price?
<p align="center">
  <img width="624" alt="Zrzut ekranu 2022-06-10 o 21 11 49" src="https://user-images.githubusercontent.com/80947256/173134369-366a906a-c346-4e4c-b6d6-00cd484d0130.png">
</p>Okay, okay I know - this polynomial regression is kind of an overkill. Still, I wanted to create something that may contain more information rather than scatterplot of every individual in the datset. I'm also aware of the outliers, but I wanted to create a visualistion of every single entry in the datset. In the next release, I will work on it and create more meaningful graph.


As most of the people in provided dataset fall within Overweight and Obese weight range, you can see the most dense spot is approximately between 25 and 35 BMI. Even though these ranges are considered as unhealthy or even life-threatening, one can deduct that BMI isn't considered as a prime metric when calculating insurance price.

After closing the graph, you can see additional statistics about weight ranges.

### What is the average age of parents in dataset?
<p align="center">
  <img width="608" alt="Zrzut ekranu 2022-06-10 o 21 28 12" src="https://user-images.githubusercontent.com/80947256/173136640-bd96e539-b346-4aaf-94db-8e5016fc10d9.png">
</p>
This one was done out of curiosity. Whole numbers on the x axis represent number of children of parent. As you can see, the only clear trend is that the more the children, the older the parents are. What surprised me to be honest, is the average age of parents without children.

## To sum up...
This code was something that I worked on for a while, but during the process of writing this README, I noticed many things that I could implement in the future or improve fairly quickly:

- better scaled x axis on average age of parent graphs, while creating better tools to compare average age and number of children,
- deleting outliers or creating a second graph without them in BMI/price scatterplot,
- compare parent data with historical entries,
- explore more and more the relationship of smoking status and insurance price.

The last one is probably the most exciting to pursuit and I will probably try to find some relationships between BMI and smoking status. 

The key take-aways from this analysis?
- smoking affects your insurance price very severely,
- BMI doesn't affect your insurance price as much as one could think,
- people start having children when they are over 35 😀.

Thank you for reading this analysis, I really encourage you to play around with my code. This was a great learning experience and I hope you enjoyed it.
















