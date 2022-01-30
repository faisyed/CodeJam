class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode'):
        def stack(node):
            if node is not None:
                stack(node.getNext())
                node.printValue()
        stack(head)