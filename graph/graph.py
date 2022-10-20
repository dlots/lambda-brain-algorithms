class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, value):
        for index, vertex in enumerate(self.vertex):
            if vertex is None:
                self.vertex[index] = Vertex(value)
                break

        # здесь и далее, параметры v -- индекс вершины

    # в списке  vertex
    def RemoveVertex(self, v):
        self.vertex[v] = None
        for u in range(self.max_vertex):
            self.m_adjacency[u][v] = 0
            self.m_adjacency[v][u] = 0

    def IsEdge(self, v1, v2):
        return self.m_adjacency[v1][v2] == 1

    def AddEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0

    def DepthFirstSearch(self, VFrom, VTo):
        stack = []
        for v in self.vertex:
            if v is not None:
                v.Hit = False
        stack.append(VFrom)
        while len(stack) > 0:
            current_index = stack[-1]
            self.vertex[current_index].Hit = True
            for index, is_adjacent in enumerate(self.m_adjacency[current_index]):
                if is_adjacent and index == VTo:
                    stack.append(VTo)
                    return [self.vertex[i] for i in stack]
            found_non_hit = False
            for index, is_adjacent in enumerate(self.m_adjacency[current_index]):
                if is_adjacent and not self.vertex[index].Hit:
                    stack.append(index)
                    found_non_hit = True
                    break
            if found_non_hit:
                continue
            stack.pop()
        return []
