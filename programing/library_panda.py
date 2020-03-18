import numpy as np
import pandas as pd

# Creating a Series by passing a list of values, letting pandas create a default integer index:
# s = pd.Series([1,2,3,'ajay', 6, 7, 8])
# print(s)

# Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns:
# dates = pd.date_range('20200201', periods=6)
# df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
# print(df)

# Creating a DataFrame by passing a dict of objects that can be converted to series-like.
# df = pd.DataFrame(
#     {'A': 1, 'B': pd.Timestamp('20200102'), 'C': pd.Series(1, index=list(range(4)), dtype=''),
#      'D': np.array([3] * 4, dtype='float32'), 'E': pd.Categorical(['test', 'train', 'test', 'train']), 'F': "foo"})
# print(df)
# print(df.dtypes)


# Here is how to view the top and bottom rows of the frame:
# dates = pd.date_range(pd.Timestamp('20200201'), periods=6)
# df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
# print(df.head(2))
# print('--------------------------------------------------')
# print(df.tail(2))

# Display the index, columns:

# web_data = {'Day': [1, 2, 3, 4, 5, 6], "Visitors": [1000, 700, 6000, 1000, 400, 350],
#             "Bounce_Rate": [20, 20, 23, 15, 10, 34]}
# df = pd.DataFrame(web_data)
# print(df.head(2))
# print('-----------------------------------')
# print(df.tail(2))

# merging and joining dataframe
# df1 = pd.DataFrame({"HPI": [80, 50, 70, 60], "Int_Rate": [2, 5, 2, 3], "IND_GDP": [50, 90, 45, 67]},
#                    index=[2001, 2002, 2003, 2004])
#
# df2 = pd.DataFrame({"HPI": [80, 90, 70, 60], "Int_Rate": [2, 1, 2, 3], "IND_GDP": [50, 45, 45, 67]},
#                    index=[2005, 2006, 2007, 2008])
# print(df1)
# print(df2)
# print(pd.merge(df2, df1))
# print(pd.merge(df1, df2, on='HPI'))
# print(pd.concat([df1, df2]))


# df1 = pd.DataFrame({"Int_Rate": [2, 1, 2, 3], "IND_GDP": [50, 45, 45, 67]}, index=[2001, 2002, 2003, 2004])
#
# df2 = pd.DataFrame({"Low_Tier_HPI": [50, 45, 67, 34], "Unemployment": [1, 3, 5, 6]}, index=[2001, 2003, 2004, 2004])
#
# joined = df1.join(df2)
# print(joined)
