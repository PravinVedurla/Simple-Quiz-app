import pandas as pd 

class data:
	def __init__(self):
		self.df = pd.read_csv('questions.csv')
		#self.df.head(5)

	def getData(self):
		return self.df


# ob = abcd()
# df1 = ob.getData()
# print(df1.head(10))