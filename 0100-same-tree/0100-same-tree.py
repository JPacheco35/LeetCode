class Solution(object):
    def isSameTree(self, p, q):

        # both are empty
        if p is None and q is None:
            return True

        # one is empty
        if p is None or q is None:
            return False

        # values are different --> FALSE
        if p.val != q.val:
            return False

        # recurse the left and right subtrees
        return self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)