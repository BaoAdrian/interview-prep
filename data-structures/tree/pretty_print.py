def pretty_print(tree):
    print("")
    pp = pretty_print_strs(tree)
    for line in reversed(pp):
        print(line)

def pretty_print_strs(tree):
    if tree.is_leaf():
        return ['+--- ' + str(tree.get_value())]
    else:
        ltree = pretty_print_strs(tree.get_left()) if tree.get_left() else None
        rtree = pretty_print_strs(tree.get_right()) if tree.get_right() else None
        nltree = len(ltree) if ltree else 0
        nrtree = len(rtree) if rtree else 0
        adjusted = _adjust_left(ltree, 0, nltree) + [str(tree.get_value())] +  _adjust_right(rtree, 0, nrtree)
        return _shift(adjusted, 0, len(adjusted))

def _shift(strlist, i, n):
    if strlist == []:
        return []
    else:
        if i == n//2:
            sh_str = ['+---' + strlist[0]]
        else:
            sh_str = ['    ' + strlist[0]]

        return sh_str + _shift(strlist[1:], i+1, n)

def _adjust_left(L, i, n):
    if i == n:
        return []
    else:
        if i <= n//2:
            adj = ' '
        else:
            adj = '|'

        return [adj + L[i]] + _adjust_left(L, i+1, n)


def _adjust_right(L, i, n):
    if i == n:
        return []
    else:
        if i >= n//2:
            adj = ' '
        else:
            adj = '|'

        return [adj + L[i]] + _adjust_right(L, i+1, n)