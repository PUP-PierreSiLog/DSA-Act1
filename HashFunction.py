class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function_1(self, key):
        result = key % self.size
        print(f"Hash Function 1: Key {key} hashed to {result}")
        return result

    def hash_function_2(self, key):
        return ((1731 * key + 520123) % 524287) % self.size

    def hash_function_3(self, key):
        # Using Python's default hash function
        return hash(key) % self.size

    def insert(self, word, hash_function):
        key = sum(ord(char) for char in word)
        index = hash_function(key)

        if self.table[index] is None:
            self.table[index] = [{'word': word, 'key': key}]  # Store both the word and the key
        else:
            self.table[index].append({'word': word, 'key': key})
        
        print(f"Inserted {word} with key {key} at index {index}")

    def delete(self, word):
        # Deletion is done by marking the word as None
        key = sum(ord(char) for char in word)
        for i in range(self.size):
            if self.table[i] is not None and word in self.table[i]:
                self.table[i].remove(word)
                if not self.table[i]:
                    self.table[i] = None
                print(f"Deleted: {word}")
                return
        print(f"{word} not found for deletion")

    def display(self):
        result = []
        for i in range(self.size):
            if self.table[i] is not None:
                result.append(f"Index {i}: {self.table[i]}")
            else:
                result.append(f"Index {i}: Empty")
        return result