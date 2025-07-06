
import pytest
from example import TreeNode, averageOfLevels

def create_tree_node(val, left=None, right=None):
 return TreeNode(val, left, right)

# Test cases for TreeNode
def test_tree_node_init_positive_value_left_right_child():
 node = create_tree_node(5, create_tree_node(2), create_tree_node(3))
 assert node.val == 5
 assert node.left.val == 2
 assert node.right.val == 3

def test_tree_node_init_negative_value_no_children():
 node = create_tree_node(-1)
 assert node.val == -1
 assert node.left is None
 assert node.right is None

def test_tree_node_init_zero_value_left_right_child():
 node = create_tree_node(0, create_tree_node(1), create_tree_node(-1))
 assert node.val == 0
 assert node.left.val == 1
 assert node.right.val == -1

# Test cases for averageOfLevels
def test_average_of_levels_balanced_tree():
 root = create_tree_node(1)
 root.left = create_tree_node(2)
 root.right = create_tree_node(3)
 root.left.left = create_tree_node(4)
 root.left.right = create_tree_node(5)
 root.right.left = create_tree_node(6)
 root.right.right = create_tree_node(7)
 assert averageOfLevels(root) == [1, 2.5, 5.5]

def test_average_of_levels_unbalanced_tree():
 root = create_tree_node(1)
 root.left = create_tree_node(2)
 root.left.left = create_tree_node(3)
 root.left.right = create_tree_node(4)
 root.left.left.left = create_tree_node(5)
 assert averageOfLevels(root) == [1, 2, 3.5, 5]

def test_average_of_levels_single_node_tree():
 root = create_tree_node(5)
 assert averageOfLevels(root) == [5]

def test_average_of_levels_empty_tree():
 assert averageOfLevels(None) == []

def test_average_of_levels_single_level_tree():
 root = create_tree_node(1)
 root.left = create_tree_node(2)
 root.right = create_tree_node(3)
 assert averageOfLevels(root) == [1, 2.5]

def test_average_of_levels_multiple_levels_one_node_per_level():
 root = create_tree_node(1)
 root.right = create_tree_node(2)
 root.right.right = create_tree_node(3)
 assert averageOfLevels(root) == [1, 2, 3]

def test_average_of_levels_large_values():
 root = create_tree_node(1000000)
 root.left = create_tree_node(2000000)
 root.right = create_tree_node(3000000)
 assert averageOfLevels(root) == [1000000, 2500000]

def test_average_of_levels_small_values():
 root = create_tree_node(-1000000)
 root.left = create_tree_node(-2000000)
 root.right = create_tree_node(-3000000)
 assert averageOfLevels(root) == [-1000000, -2500000]