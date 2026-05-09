import numpy as np
import random
from collections import Counter
import math

# Алфавіт
alphabet = ['A', 'B', 'C', 'D']

# Матриця переходів
transition_matrix = np.array([
    [0.4, 0.3, 0.2, 0.1],
    [0.1, 0.4, 0.3, 0.2],
    [0.2, 0.1, 0.4, 0.3],
    [0.3, 0.2, 0.1, 0.4]
])

# Генерація джерела з пам’яттю
def generate_markov_sequence(matrix, length):
    sequence = [random.choice(alphabet)]

    for _ in range(length - 1):
        prev_symbol = sequence[-1]
        prev_index = alphabet.index(prev_symbol)

        next_symbol = random.choices(
            alphabet,
            weights=matrix[prev_index]
        )[0]

        sequence.append(next_symbol)

    return ''.join(sequence)

# Генерація джерела без пам’яті
def generate_memoryless_sequence(length):
    return ''.join(random.choices(alphabet, k=length))

# Обчислення ентропії
def calculate_entropy(sequence):
    freq = Counter(sequence)
    total = len(sequence)

    entropy = 0

    for count in freq.values():
        p = count / total
        entropy -= p * math.log2(p)

    return entropy

# Частоти символів
def calculate_frequencies(sequence):
    freq = Counter(sequence)
    total = len(sequence)

    return {
        symbol: freq[symbol] / total
        for symbol in alphabet
    }

# Довжини послідовностей
lengths = [1000, 5000, 10000]

for length in lengths:

    markov_seq = generate_markov_sequence(
        transition_matrix,
        length
    )

    random_seq = generate_memoryless_sequence(length)

    markov_entropy = calculate_entropy(markov_seq)
    random_entropy = calculate_entropy(random_seq)

    markov_freq = calculate_frequencies(markov_seq)
    random_freq = calculate_frequencies(random_seq)

    print(f"\nДовжина: {length}")

    print("\nДжерело з пам’яттю:")
    print("Ентропія:", round(markov_entropy, 4))
    print("Частоти:", markov_freq)

    print("\nДжерело без пам’яті:")
    print("Ентропія:", round(random_entropy, 4))
    print("Частоти:", random_freq)