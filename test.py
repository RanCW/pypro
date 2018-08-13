# 任务1.1： 导入库以及数据
#
# 载入需要的库 NumPy、Pandas、matplotlib、seaborn。
# 利用 Pandas 库，读取 tmdb-movies.csv 中的数据，保存为 movie_data。
# 提示：记得使用 notebook 中的魔法指令 %matplotlib inline，否则会导致你接下来无法打印出图像。


import numpy as np
import pandas as pd
import matplotlib as mat
import seaborn as sb
# %matplotlib inline
movie_data=pd.read_csv('tmdb-movies.csv')
print(movie_data)


# 任务1.2: 了解数据
#
# 你会接触到各种各样的数据表，因此在读取之后，我们有必要通过一些简单的方法，来了解我们数据表是什么样子的。
#
# 获取数据表的行列，并打印。
# 使用 .head()、.tail()、.sample() 方法，观察、了解数据表的情况。
# 使用 .dtypes 属性，来查看各列数据的数据类型。
# 使用 isnull() 配合 .any() 等方法，来查看各列是否存在空值。
# 使用 .describe() 方法，看看数据表中数值型的数据是怎么分布的。