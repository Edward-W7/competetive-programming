class SegmentTree:
    def __init__(self, arr):
        # Store the original array
        self.arr = arr

        # Create the segment tree as a list of Nones
        self.tree = [None] * (4 * len(arr))

        # Build the segment tree
        self.build_tree(0, 0, len(arr) - 1)

    def build_tree(self, node, start, end):
        # If this is a leaf node, store the value at this index of the original array
        if start == end:
            self.tree[node] = self.arr[start]
            return

        # Calculate the midpoint of this segment
        mid = (start + end) // 2

        # Recursively build the left and right subtrees
        self.build_tree(2 * node + 1, start, mid)
        self.build_tree(2 * node + 2, mid + 1, end)

        # Store the minimum value in this segment
        self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, start, end):
        # Query the segment tree for the minimum value in the given range
        return self.query_tree(0, 0, len(self.arr) - 1, start, end)

    def query_tree(self, node, node_start, node_end, query_start, query_end):
        # If the range of this segment is completely contained within the query range, return the value at this node
        if node_start >= query_start and node_end <= query_end:
            return self.tree[node]

        # If the range of this segment is completely outside of the query range, return infinity
        elif node_start > query_end or node_end < query_start:
            return float('inf')

        # Otherwise, calculate the midpoint of this segment
        mid = (node_start + node_end) // 2

        # Recursively query the left and right subtrees
        left_min = self.query_tree(2 * node + 1, node_start, mid, query_start, query_end)
        right_min = self.query_tree(2 * node + 2, mid + 1, node_end, query_start, query_end)

        # Return the minimum value from the left and right subtrees
        return min(left_min, right_min)

#Testing Code for Seg Tree
arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]
tree = SegmentTree(arr)

print(tree.query(0, len(arr) - 1))  # should return 1
print(tree.query(3, 7))  # should return 4
