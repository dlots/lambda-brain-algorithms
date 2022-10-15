import unittest
from random import sample
from graph import SimpleGraph


def create_graph():
    size = 5
    high_limit = size * 10
    graph = SimpleGraph(size)
    array = sample(range(high_limit), size)
    for x in array:
        graph.AddVertex(x)
    return graph, array, size


def is_edge(i, j, edge):
    return (i == edge[0] and j == edge[1]) or (j == edge[0] and i == edge[1])


class TestGraph(unittest.TestCase):
    def test_add_vertex(self):
        graph, array, _ = create_graph()
        for vertex in graph.vertex:
            self.assertIn(vertex.Value, array)
        self.assertNotIn(None, graph.vertex)
        for i, row in enumerate(graph.m_adjacency):
            for j, _ in enumerate(row):
                self.assertFalse(graph.IsEdge(i, j))

    def test_add_edge(self):
        graph, _, size = create_graph()
        vertices_to_join = sample(range(size), 2)
        graph.AddEdge(*vertices_to_join)
        for i, row in enumerate(graph.m_adjacency):
            for j, _ in enumerate(row):
                if is_edge(i, j, vertices_to_join):
                    self.assertTrue(graph.IsEdge(i, j))
                    continue
                self.assertFalse(graph.IsEdge(i, j))

    def test_remove_vertex(self):
        graph, _, size = create_graph()
        vertices_to_join = sample(range(size), 2)
        graph.AddEdge(*vertices_to_join)
        for i, row in enumerate(graph.m_adjacency):
            for j, _ in enumerate(row):
                if is_edge(i, j, vertices_to_join):
                    self.assertTrue(graph.IsEdge(i, j))
                    continue
                self.assertFalse(graph.IsEdge(i, j))
        graph.RemoveVertex(vertices_to_join[0])
        self.assertIsNone(graph.vertex[vertices_to_join[0]])
        for i, row in enumerate(graph.m_adjacency):
            for j, _ in enumerate(row):
                self.assertFalse(graph.IsEdge(i, j))

    def test_remove_edge(self):
        graph, _, size = create_graph()
        vertices_to_join = sample(range(size), 2)
        graph.AddEdge(*vertices_to_join)
        for i, row in enumerate(graph.m_adjacency):
            for j, _ in enumerate(row):
                if is_edge(i, j, vertices_to_join):
                    self.assertTrue(graph.IsEdge(i, j))
                    continue
                self.assertFalse(graph.IsEdge(i, j))
        graph.RemoveEdge(*vertices_to_join)
        self.assertIsNotNone(graph.vertex[vertices_to_join[0]])
        for i, row in enumerate(graph.m_adjacency):
            for j, _ in enumerate(row):
                self.assertFalse(graph.IsEdge(i, j))


if __name__ == '__main__':
    unittest.main()
