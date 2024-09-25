import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
iris=pd.read_csv("IRIS.csv")
sns.displot(iris['sepal_length'],kde=True,rug=True)
plt.title("Distribution of Sepal length")
plt.show()
sns.histplot(iris['petal_width'],kde=True,bins=20)
plt.title("Histogram of Petal width")
plt.show()
sns.relplot(x="sepal_length",y="sepal_width",data=iris,hue="species",style="species")
plt.title("Sepal Length v/s Sepal Width")
plt.show()