
from sklearn.datasets import load_iris, fetch_20newsgroups
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

iris = load_iris()
# news = fetch_20newsgroups()

iris_data = pd.DataFrame(data=iris.data, columns=['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'])

iris_data['target'] = iris.target


def iris_plot(data, col1, col2):
    sns.lmplot(x=col1, y=col2, data=data, hue='target', fit_reg=False)
    plt.title("鸢尾花数据展示")
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.show()
#
# iris_plot(iris_data, 'Sepal_Length', 'Petal_Width')
# iris_plot(iris_data, 'Sepal_Width', 'Petal_Length')

x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=22, test_size=0.2)

# 特征预处理
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.fit_transform(x_test)

# 模型训练
estimator = KNeighborsClassifier(n_neighbors=5)
estimator.fit(x_train, y_train)

# 预测
y_predict = estimator.predict(x_test)

# 计算准确率
score = estimator.score(x_test, y_test)