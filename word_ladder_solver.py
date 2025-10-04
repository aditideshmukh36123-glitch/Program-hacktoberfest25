from collections import deque

def word_ladder(start, end, word_list):
    word_set = set(word_list)  # For O(1) lookups
    if end not in word_set:
        return []  # No solution if end word is not in dictionary

    queue = deque()
    queue.append((start, [start]))  # Each element: (current_word, path_so_far)

    while queue:
        current_word, path = queue.popleft()
        if current_word == end:
            return path  # Found the shortest path

        # Try changing each letter from 'a' to 'z'
        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + c + current_word[i+1:]
                if next_word in word_set:
                    queue.append((next_word, path + [next_word]))
                    word_set.remove(next_word)  # Avoid revisiting

    return []  # No path found

# Example usage
start_word = "hit"
end_word = "cog"
dictionary = ["hot","dot","dog","lot","log","cog"]

path = word_ladder(start_word, end_word, dictionary)
if path:
    print("Shortest transformation sequence:")
    print(" -> ".join(path))
else:
    print("No transformation sequence exists.")
