class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False
        self.bfs_predecessor = None


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

    def __shortest_path_to(self, vertex):
        result = [vertex]
        while vertex.bfs_predecessor is not None:
            result.append(vertex.bfs_predecessor)
            vertex = vertex.bfs_predecessor
        return list(reversed(result))

    def BreadthFirstSearch(self, VFrom, VTo):
        queue = []
        for v in self.vertex:
            if v is not None:
                v.Hit = False
                v.bfs_predecessor = None
        self.vertex[VFrom].Hit = True
        queue.append(VFrom)
        while len(queue) > 0:
            current_index = queue.pop()
            for index, is_adjacent in enumerate(self.m_adjacency[current_index]):
                if not is_adjacent:
                    continue
                if index == VTo:
                    end = self.vertex[VTo]
                    end.bfs_predecessor = self.vertex[current_index]
                    return self.__shortest_path_to(end)
                if not self.vertex[index].Hit:
                    non_hit = self.vertex[index]
                    non_hit.Hit = True
                    non_hit.bfs_predecessor = self.vertex[current_index]
                    queue.insert(0, index)
        return []

    def WeakVertices(self):
        result = []
        for index, vertex in enumerate(self.vertex):
            if vertex is None:
                continue
            weak = True
            adjacent = []
            for adjacent_index, is_adjacent in enumerate(self.m_adjacency[index]):
                if not is_adjacent:
                    continue
                for second_adjacent_index in adjacent:
                    if self.m_adjacency[adjacent_index][second_adjacent_index] == 1:
                        weak = False
                        break
                if not weak:
                    break
                adjacent.append(adjacent_index)
            if weak:
                result.append(vertex)
        return result
