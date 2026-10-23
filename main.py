from linked_list import LinkedList 


if __name__ == "__main__":
    # 1) Create a LinkedList instance
    roster = LinkedList()

    # 2) Insert some sample data
    roster.insert_at_front(103)
    roster.insert_at_front(102)
    roster.insert_at_front(101)
    roster.insert_at_end(104)

    # 3) Display the list to verify insertion
    print("Roster:")
    roster.display()

    # 4) Recursive sum
    print("Sum of IDs:", roster.recursive_sum())

    # 5) Recursive search
    print("Is 103 on the roster?", roster.recursive_search(103))
    print("Is 999 on the roster?", roster.recursive_search(999))

    # 6) Reverse, then display
    roster.recursive_reverse()
    print("Reversed roster:")
    roster.display()