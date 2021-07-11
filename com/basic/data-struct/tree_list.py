"""
 树的基本操作： 定义列表函数的 二叉树

"""

# 基础的结构如下
my_tree = ['a', # 根节点
               [
                   'b',  # 左子树
                   ['e',[],[]],
                   ['d',[],[]]
               ],[
                    'c', # 右子树
                    ['f',[],[]]
               ]
           ]

# print(my_tree)

# 取出 左子树
# print(my_tree[1])

# 取出 右子树
# print(my_tree[2])


def Binary_Tree(root):
    """
    定义列表函数的 二叉树
    :param root:
    :return:
    """
    return [root, [], []]

def insert_left(tree, new_data):
    """
    插入左 子树
    1.先获取 当前的左子树对应的列表(可能为空), 将旧的左子树作为新节点的左子树
    :param tree: 二叉树
    :param new_data: 新的左子树
    :return:
    """
    left_tree = tree.pop(1)
    if len(left_tree) > 1:
        tree.insert(1,[new_data, left_tree,[]])
    else:
        # 如果旧左子树为空
        tree.insert(1, [new_data, [],[]])
    return tree


def insert_right(tree, new_data):
    """
    插入右 子树
    1.先获取 当前的右子树对应的列表(可能为空), 将旧的右子树作为新节点的右子树
    :param tree: 二叉树
    :param new_data: 新的右子树
    :return:
    """
    right_tree = tree.pop(2)
    if len(right_tree) > 1:
        tree.insert(2,[new_data, [],right_tree])
    else:
        # 如果旧右子树为空
        tree.insert(2, [new_data, [],[]])
    return tree

# 树的访问函数

def get_root_val(tree):
    return tree[0]

def set_root_val(tree, new_val):
    tree[0] = new_val

def get_left_child(tree):
    return tree[1]

def get_right_child(tree):
    return tree[2]



if __name__ == '__main__':
    tree = Binary_Tree(3)
    tree = insert_left(tree, 4)
    print(tree)

    insert_right(tree,6)
    print(tree)

    insert_right(tree,7)
    print(tree)

    l = get_left_child(tree)
    print(l)

    r = get_right_child(tree)
    print(r)

    # 设置左子树的根节点值
    set_root_val(l, 10)
    print(tree)




