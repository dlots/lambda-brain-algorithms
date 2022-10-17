class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов
        self.level = -1


class SimpleTree:

    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode

    def DeleteNode(self, NodeToDelete):
        if NodeToDelete.Parent is not None:
            NodeToDelete.Parent.Children.remove(NodeToDelete)
            NodeToDelete.Parent = None

    def get_all_nodes_in_subtree(self, subtree_root, nodes):
        nodes.append(subtree_root)
        for child in subtree_root.Children:
            self.get_all_nodes_in_subtree(child, nodes)

    def GetAllNodes(self):
        result = []
        self.get_all_nodes_in_subtree(self.Root, result)
        return result

    def find_nodes_by_value_in_subtree(self, subtree_root, value, nodes):
        if subtree_root.NodeValue == value:
            nodes.append(subtree_root)
        for child in subtree_root.Children:
            self.find_nodes_by_value_in_subtree(child, value, nodes)

    def FindNodesByValue(self, val):
        result = []
        self.find_nodes_by_value_in_subtree(self.Root, val, result)
        return result

    def MoveNode(self, OriginalNode, NewParent):
        old_parent = OriginalNode.Parent
        if old_parent is None or old_parent is NewParent:
            return
        self.DeleteNode(OriginalNode)
        NewParent.Children.append(OriginalNode)
        OriginalNode.Parent = NewParent

    def subtree_count(self, subtree_root):
        count = 1
        for child in subtree_root.Children:
            count += self.subtree_count(child)
        return count

    def Count(self):
        if self.Root is None:
            return 0
        return self.subtree_count(self.Root)

    def subtree_leaf_count(self, subtree_root):
        if len(subtree_root.Children) == 0:
            return 1
        leaf_count = 0
        for child in subtree_root.Children:
            leaf_count += self.subtree_leaf_count(child)
        return leaf_count

    def LeafCount(self):
        if self.Root is None:
            return 0
        return self.subtree_leaf_count(self.Root)

    def set_level_in_subtree(self, subtree_root, subtree_root_level):
        subtree_root.level = subtree_root_level
        for child in subtree_root.Children:
            self.set_level_in_subtree(child, subtree_root_level + 1)

    # чтобы не анализировать все дерево, можно задавать уровень при добавлении, удалении, перемещении узлов
    # как (уровень родителя + 1)
    def set_all_nodes_level(self):
        if self.Root is not None:
            self.set_level_in_subtree(self.Root, 0)

    def __even_trees_recursive(self, current_node, result):
        count = 1
        for child in current_node.Children:
            count += self.__even_trees_recursive(child, result)
        if count % 2 == 0 and current_node.Parent is not None:
            result.append(current_node.Parent)
            result.append(current_node)
            count = 0
        return count

    def EvenTrees(self):
        result = []
        if self.Root is not None:
            self.__even_trees_recursive(self.Root, result)
        return result
