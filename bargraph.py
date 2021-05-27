from os import name
from graph import Graph
import matplotlib.pyplot as plt
graph = Graph()
data = graph.read_data("MATCH (a:`Not Verified`)-[r:FOLLOW]->(b:Verified) RETURN a.name,b.name")
values = data['b.name'].value_counts().rename_axis('name').reset_index(name='counts')
names=list(values['name'])
values=list(values['counts'])
plt.bar(names, values, width=0.2)
plt.xlabel('Influencers',size=20)
plt.ylabel('No. of occurence',size=20)
plt.title('Influencer Occurence', size = 20)
plt.xticks(size = 15)
plt.yticks(size = 20)
plt.xlim([0, 10])
plt.show()

