class Node:
    """A node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """A singly linked list."""
    def __init__(self):
        self.head = None

    def add(self, data):
        """Add a node with the given data to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def __str__(self):
        """Return a string representation of the list."""
        values = []
        curr = self.head
        while curr:
            values.append(str(curr.data))
            curr = curr.next
        return " -> ".join(values) if values else "Empty List"

    def delete_nth(self, n):
        """
        Delete the nth node (1-based index).
        Raises:
            IndexError: If list is empty or n is out of range.
        """
        if not self.head:
            raise IndexError("Cannot delete from an empty list.")

        if n < 1:
            raise IndexError(f"Index must be ≥ 1. Got {n}.")

        # Deleting the head
        if n == 1:
            removed = self.head
            self.head = self.head.next
            return removed.data

        # Find (n-1)th node
        prev = self.head
        for i in range(n - 2):
            if not prev.next:
                raise IndexError(f"Index {n} out of range.")
            prev = prev.next

        # Now prev is (n-1)th, prev.next is nth (to delete)
        to_delete = prev.next
        if not to_delete:
            raise IndexError(f"Index {n} out of range.")
        prev.next = to_delete.next
        return to_delete.data


if __name__ == "__main__":
    # Sample usage / testing
    ll = LinkedList()
    for value in [10, 20, 30, 40, 50]:
        ll.add(value)

    print("Initial list:")
    print(ll)  # 10 -> 20 -> 30 -> 40 -> 50

    # Delete 3rd node
    try:
        removed = ll.delete_nth(3)
        print(f"\nDeleted node at position 3, value = {removed}")
        print("List after deletion:")
        print(ll)  # 10 -> 20 -> 40 -> 50
    except IndexError as e:
        print("Error:", e)

    # Attempt to delete out-of-range
    try:
        ll.delete_nth(10)
    except IndexError as e:
        print("\nError on deleting position 10:", e)

    # Delete head
    try:
        removed = ll.delete_nth(1)
        print(f"\nDeleted head node, value = {removed}")
        print("List now:")
        print(ll)
    except IndexError as e:
        print("Error:", e)

    # Delete until empty
    try:
        while True:
            ll.delete_nth(1)
    except IndexError as e:
        print("\nAfter deleting all nodes:", ll)
        print("Error on further deletion:", e)
