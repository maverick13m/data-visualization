'''
#Data - number, string, dictionary, list, float, integer
There is another data object which is called a dataframe. In the data frame the data is aligned
in tabular form i.e., rows and columns.
And these rows and columns can have any type of data such as string or integer or float.
'''
#CVS - comma seperated values
#Data becomes much more meaningful for humans when visualized in the form of graphs.
#read the data

import pandas as pd
#DataFrame - row and column

data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)

df1 = pd.DataFrame()
print(df1)

#PLOTLY_EXPRESS
import plotly_express as px

#.read_csv() - automaticall converts the cvs file to rows and columns
df2=pd.read_csv("line_chart.csv")
print(df2)
#line graph
fig = px.line(df2, x="Year" ,y="Per capita income" ,color="Country" , title="Per Capita Income")
#fig.show()

df3=pd.read_csv("data.csv")
print(df3)

#bar graph
fig1 = px.bar(df3, x="Country", y ="InternetUsers", title = "Per capita & InternetUsers")
#fig1.show()

#scattered graph
fig2 = px.scatter(df3, x="Population", y ="Per capita",color="Country",size= "Percentage",title = "Per capita & InternetUsers",size_max=60)
#fig2.show()


#HOMEWORKKKKKKK.................................................................................................................................................................
df4=pd.read_csv("covid.csv")
fig3 = px.line(df4, x="date", y ="cases",color="country", title = "covid Cases")
fig4 = px.scatter(df4, x="date", y ="cases",color="country",size ="cases",title = "covid Cases",size_max=30)

fig4.show()
fig3.show()
