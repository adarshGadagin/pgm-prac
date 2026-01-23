# 1.Writing basic Python programs (Hello World, arithmetic operations)
print("Hello World!")
# input a and b 
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
# 1. Addition
print(f"Addition : {a} + {b} = {a+b}")
# 2. Substraction
print(f"Substraction : {a} - {b} = {a-b}")
# 3. Multiplication
print(f"Multiplication : {a} * {b} = {a*b}")
# 4. Division
print(f"Division : {a} / {b} = {a/b}")
# 5. Floor division
print(f"Floor division : {a} // {b} = {a//b}")
# 6. Modulo
print(f"Modulo : {a} % {b} = {a%b}")
# 7. Exponential
print(f"Exponential : {a} ** {b} = {a**b}")

# 2.Implementing control structures and functions in Python
# if statement
a=int(input("Enter a number to check positive or not : "))
if(a>0):
    print(f"{a} is positive")

# if...else
b=int(input("Enter a number to check even or odd : "))
if(b%2==0):
    print(f"{b} is even number")
else:
    print(f"{b} is odd number")

# if-if...else-else
p=int(input("Enter your percentage to check grade : "))
if(0<=p<=100):
    if(p>=90):
        print("Grade A")
    elif(p>=80):
        print("Grade B")
    elif(p>=70):
        print("Grade C")
    elif(p>=60):
        print("Grade D")
    elif(p>=50):
        print("Grade E")
    else:
        print("Grade F")
else:
    print("Invalid percentage")

# for loop
n=int(input("Enter till where to print : "))
for i in range(n):
    print(i)
# while loop
m=int(input("Enter till where to count : "))
count=1
while count<=m:
    print(count)
    count+=1

# defining a function without arguments an return value
def greet():
    print("Good Morning")

# calling a function
greet()

# defining a function with arguments
def addNumbers(a,b):
    print(f"The sum of {a} and {b} is {a+b}")

# calling a function with arguments
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
addNumbers(a,b)

# defining a function with arguments an return value
def twoNumProduct(p,q):
    return p*q

# calling a function with arguments an return value
p=int(input("Enter first number : "))
q=int(input("Enter second number : "))
product=twoNumProduct(p,q)
print(f"Product of {p} and {q} is {product}")

# 3.Manipulating lists, tuples, sets, and dictionaries
# a) List Operations
fruits=["Apple","Banana","Cherry"]
print("Original List : ",fruits)

fruits.append("Orange") # add element
fruits.remove("Banana") # remove element
fruits[1]="Grapes" # Update element
print("Updated List : ",fruits) 
print("Sliced List : ",fruits[0:2]) # Slicing

# b) Tuple Operations
tup=(1,2,3,4,'Python','hi')
print("Tuple : ",tup)
print("First Element :",tup[0])
print("Last Element :",tup[-1])

# Tuple Slicing
print(tup[1:])
print(tup[0:1])

# Tuple Concatention using + operator
print(tup+tup)

# Tuple repatition using * operator
print(tup*3)

# c) Set Operations
set1={'James',2,2,'Python'}
# printing set value
print(set1)
# Adding element to the set
set1.add(10)
print(set1)
# Removing element from the set
set1.remove(2)
print(set1)

# d) Dictionary Operations
d={1:'Jimmy',2:'Alex',3:'John',4:'Mike'}
# printing dictionary
print(d)

# Accessing value using keys
print("first name is "+d[1])
print("last name is "+d[4])
print(d.keys())
print(d.values())

# 4.Reading and writing data from text and CSV files
# writing a text file
with open ("sample.txt","w") as f:
    f.write("Hello, this is text file.\n")
    f.write("Python made file handling easy.\n")

# reading from a text file
with open ("sample.txt","r") as f:
    content=f.read()
    print("File content :\n",content)

# appending data to a text file
with open ("sample.txt","w") as f:
    f.write("The line is appendedd.\n")

# reading from a text file
with open ("sample.txt","r") as f:
    content=f.read()
    print("File content :\n",content)

import csv
# wrinting a CSV file
data=[
    ["ID","Name","Marks"],
    [1,"Alice",85],
    [2,"Bob",78],
    [3,"Charlie",92]
]
with open ("marks.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerows(data)

# reading data from a csv file
with open ("marks.csv") as f:
    reader=csv.reader(f)
    print("CSV File Data : ")
    for row in reader:
        print(row)

# 5.Performing array operations using NumPy
import numpy as np
# creating arrays
a=np.array([1,2,3,4,5])
b=np.array([10,20,30,40,50])
print("Array a :",a)
print("Array b :",b)

# Arithmetic operators
print("Additon :",a+b)
print("Substracion :",b-a)
print("multiplication :",a*b)
print("Division :",b/a)

# Array Slicing
print("First three elements of a :",a[:3])
print("Last tw element of b :",b[-2:])

# Reshaping
c=np.arange(1,10) # create array [1....9]
print("Original array :",c)
print("Reshaped to 3*3 matrix :\n",c.reshape(3,3))

# Aggregation and Stastical functions
d=np.array([5,10,15,20,25])
print("Sum :",np.sum(d))
print("Mean :",np.mean(d))
print("Minimum :",np.min(d))
print("Maximum : ",np.max(d))
print("Standard Deviation :",np.std(d))

# 6.Data manipulation and cleaning using Pandas
import pandas as pd
import numpy as np
# create a dataframe
data={
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi'],
    'Age': [24, 30, np.nan, 28, 22, 35, 29, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Boston', 'Los Angeles', 'Chicago', ''],
    'Salary': [50000, 60000, 55000, 62000, np.nan, 70000, 58000, 75000],
    'Department': ['IT', 'HR', 'IT', 'Sales', 'HR', 'IT', 'Sales', 'IT']
}
df=pd.DataFrame(data)
print("Original Dataframe : ")
print(df)
print("\n"+"="*30+"\n")

# check missing values
print("Missing values before cleaning : ")
print(df.isnull().sum())

# fill missing 'Age' with the mean
df['Age'].fillna(df['Age'].mean(),inplace=True)

# fill missing 'Salary' with specific value (e.g., 0)
df['Salary'].fillna(0,inplace=True)

# drop rows where 'city' is an empty string
df=df[df['City']!='']
print("\nDataFrame after handling missing values : ")
print(df)
print("\n"+"="*30+"\n")

# 7.Creating various plots with Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# sample dataset
x=np.linspace(2,10,50)
y=np.sin(x)

# i) Line Plot (Matplotlib)
plt.plot(x,y,label="Sin(x)",color="blue",marker="o")
plt.title("Line Plot - Sine Function")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

# ii) Bar Chart (Matplotlib)
categories=['A','B','C','D']
values=[10,24,36,18]
plt.bar(categories,values,color="orange")
plt.title("Bar Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# iii) Histogram (Matplotlib)
data=np.random.randn(1000) # normal distribution
plt.hist(data,bins=30,color="blue",edgecolor="black")
plt.title("Histogram Example")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

# iv) Scatter Plot (Seaborn)
df=sns.load_dataset("iris")
sns.scatterplot(x="sepal_length",y="sepal_width",hue="species",data=df)
plt.title("Scatter Plot - Iris Dataset")
plt.show()

# v) Box Plot (Seaborn)
sns.boxplot(hue="species",y="petal_length",data=df,palette="Set2")
plt.title("Box Plot - Petal length by species")
plt.show()

# vi) Pair Plot (Seaborn)
sns.pairplot(df,hue="species")
plt.suptitle("Pair plot - Iris Dataset",y=1.02)
plt.show()

# 8.Exploratory Data Analysis (EDA) on sample datasets
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load sample dataset (Iris dataset)
df=sns.load_dataset("iris")

# i) Basic Inspection
print("First 5 rows of dataset :\n",df.head())
print("\nDataset Info :",df.info())
print("\nSummary statistics :",df.describe())

# ii) Checking missing values
print("\nMissing values in dataset :",df.isnull().sum())

# iii) Univariate Analysis - Distribution
sns.histplot(df["sepal_length"],kde=True,bins=20,color="blue")
plt.title("Distribution of sepal length")
plt.show()

# iv) Bivariate Analysis - Scatter Plot
sns.scatterplot(x="sepal_length",y="petal_length",hue="species",data=df)
plt.title("Sepal vs Petal by Species")
plt.show()

# v) Multivariate Analysis - Pair Plot
sns.pairplot(df,hue="species")
plt.suptitle("Pair Plot of iris Dataset",y=1.02)
plt.show()

# vi) Correlation Heatmap
corr = df.select_dtypes(include='number').corr()
sns.heatmap(corr,annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()