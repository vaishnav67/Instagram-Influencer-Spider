from py2neo import Graph as NeoGraph, Node, Relationship
class Graph:
    def __init__(self):
        self.graph = NeoGraph("bolt://localhost:7687",user="neo4j", password="Instagram")

    def add_node(self, username, verification):
        node = Node(verification, name=username)
        tx = self.graph.begin()
        tx.merge(node, primary_label="Person", primary_key=('name'))
        tx.commit()

    def add_edge(self, username_a, username_b, t_a, t_b):
        node_a = Node(t_a, name=username_a)
        node_b = Node(t_b, name=username_b)
        rel = Relationship(node_a, "FOLLOW", node_b)
        tx = self.graph.begin()
        tx.merge(rel,primary_label="Person", primary_key=('name'))
        tx.commit()
    def del_graph(self):
        NeoGraph.delete_all(self.graph)