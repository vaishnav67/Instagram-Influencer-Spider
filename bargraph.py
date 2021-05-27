from os import name
from graph import Graph
import matplotlib.pyplot as plt
graph = Graph()
data = graph.read_data("MATCH (a:`Not Verified`)-[r:FOLLOW]->(b:Verified) RETURN a.name,b.name")
values = data['b.name'].value_counts().rename_axis('name').reset_index(name='counts')
names=list(values['name'])
values=list(values['counts'])
plt.figure(figsize=(9, 3))
plt.bar(names, values)
plt.xlim([0, 10])
plt.show()

