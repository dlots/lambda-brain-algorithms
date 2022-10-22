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

    def test_depth_first_search(self):
        graph = SimpleGraph(5)
        graph.AddVertex(0)
        graph.AddVertex(1)
        graph.AddEdge(0, 1)
        path = graph.DepthFirstSearch(0, 1)
        self.assertEqual(path[0].Value, 0)
        self.assertEqual(path[1].Value, 1)
        graph.AddVertex(2)
        graph.AddEdge(1, 2)
        graph.AddVertex(3)
        graph.AddEdge(1, 3)
        graph.AddEdge(3, 2)
        path = graph.DepthFirstSearch(0, 2)
        self.assertEqual(path[0].Value, 0)
        self.assertEqual(path[1].Value, 1)
        self.assertEqual(path[2].Value, 2)
        path = graph.DepthFirstSearch(0, 3)
        self.assertEqual(path[0].Value, 0)
        self.assertEqual(path[1].Value, 1)
        self.assertEqual(path[2].Value, 3)

    def test_breadth_first_search(self):
        graph = SimpleGraph(5)
        graph.AddVertex(0)
        graph.AddVertex(1)
        graph.AddEdge(0, 1)
        path = graph.BreadthFirstSearch(0, 1)
        self.assertEqual(path[0].Value, 0)
        self.assertEqual(path[1].Value, 1)
        graph.AddVertex(2)
        graph.AddEdge(1, 2)
        graph.AddVertex(3)
        graph.AddEdge(1, 3)
        graph.AddEdge(3, 2)
        path = graph.BreadthFirstSearch(0, 2)
        self.assertEqual(path[0].Value, 0)
        self.assertEqual(path[1].Value, 1)
        self.assertEqual(path[2].Value, 2)
        path = graph.BreadthFirstSearch(0, 3)
        self.assertEqual(path[0].Value, 0)
        self.assertEqual(path[1].Value, 1)
        self.assertEqual(path[2].Value, 3)

    def test_weak_vertices(self):
        graph = SimpleGraph(10)
        for i in range(9):
            graph.AddVertex(i)
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        graph.AddEdge(0, 3)
        graph.AddEdge(1, 3)
        graph.AddEdge(1, 4)
        graph.AddEdge(2, 3)
        graph.AddEdge(3, 5)
        graph.AddEdge(4, 5)
        graph.AddEdge(5, 7)
        graph.AddEdge(5, 8)
        graph.AddEdge(6, 8)
        graph.AddEdge(7, 8)
        result = graph.WeakVertices()
        self.assertEqual(result[0].Value, 4)
        self.assertEqual(result[1].Value, 6)


if __name__ == '__main__':
    unittest.main()
