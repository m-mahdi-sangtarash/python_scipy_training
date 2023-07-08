import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

dataframe = pd.read_excel("Practice-50-1-data.xlsx")
data = dataframe.iloc[:, [1, 2]].values

plt.scatter(dataframe["W_Life_expectancy"], dataframe["Literate_pop_p"])
plt.show()

linked = linkage(data, "single")
dendrogram(linked)
plt.show()

model = AgglomerativeClustering(n_clusters=2, linkage="single")
model.fit_predict(data)
print(model.labels_)
plt.scatter(data[:, 0], data[:, 1], c=model.labels_)
plt.show()