import math
import random
from collections import Counter

import matplotlib.pyplot as plt




def preprocess_text(text):

    text = text.lower()

    
    text = ''.join(
        char for char in text
        if char.isalpha()
    )

    return text




def calculate_entropy(text):

    frequencies = Counter(text)

    total_symbols = len(text)

    entropy = 0

    for count in frequencies.values():

        probability = count / total_symbols

        entropy -= probability * math.log2(probability)

    return entropy



def create_bigrams(text):

    bigrams = []

    for i in range(len(text) - 1):

        bigram = text[i] + text[i + 1]

        bigrams.append(bigram)

    return bigrams




def calculate_bigram_entropy(text):

    bigrams = create_bigrams(text)

    frequencies = Counter(bigrams)

    total_bigrams = len(bigrams)

    entropy = 0

    for count in frequencies.values():

        probability = count / total_bigrams

        entropy -= probability * math.log2(probability)


    entropy = entropy / 2

    return entropy



def calculate_hmax(text):

    alphabet = set(text)

    alphabet_size = len(alphabet)

    return math.log2(alphabet_size)




def calculate_redundancy(h, hmax):

    return 1 - (h / hmax)




def shuffle_text(text):

    text_list = list(text)

    random.shuffle(text_list)

    return ''.join(text_list)




def generate_random_text(alphabet, length):

    random_text = ''.join(
        random.choice(alphabet)
        for _ in range(length)
    )

    return random_text




def plot_entropy_convergence(text):

    sizes = [
        100,
        500,
        1000,
        5000,
        10000,
        20000,
        50000
    ]

    h0_values = []

    h1_values = []

    real_sizes = []

    for size in sizes:


        if size > len(text):
            continue

        sample = text[:size]

        h0 = calculate_entropy(sample)

        h1 = calculate_bigram_entropy(sample)

        h0_values.append(h0)

        h1_values.append(h1)

        real_sizes.append(size)


    if len(real_sizes) == 0:
        print("Недостатньо символів для побудови графіка")
        return


    plt.figure(figsize=(10, 6))

    # H0
    plt.plot(
        real_sizes,
        h0_values,
        marker='o',
        linewidth=2,
        label='H₀ — ентропія символів'
    )

    # H1
    plt.plot(
        real_sizes,
        h1_values,
        marker='s',
        linewidth=2,
        label='H₁ — ентропія біграм'
    )

    plt.xlabel("Довжина тексту", fontsize=12)

    plt.ylabel("Ентропія", fontsize=12)

    plt.title(
        "Залежність ентропії від довжини тексту",
        fontsize=14
    )


    plt.ylim(
        min(h1_values) - 0.3,
        max(h0_values) + 0.3
    )

    plt.grid(True)

    plt.legend()

    plt.tight_layout()

    plt.show()




with open("text.txt", "r", encoding="utf-8") as file:

    text = file.read()



text = preprocess_text(text)

print("=" * 60)
print("АНАЛІЗ ПРИРОДНОГО ТЕКСТУ")
print("=" * 60)


# H0


h0 = calculate_entropy(text)

print(f"H₀ = {h0:.4f}")



# H1


h1 = calculate_bigram_entropy(text)

print(f"H₁ = {h1:.4f}")



# Hmax


hmax = calculate_hmax(text)

print(f"Hmax = {hmax:.4f}")


# Надлишковість


redundancy = calculate_redundancy(h0, hmax)

print(f"Надлишковість = {redundancy:.4f}")



# Перемішаний текс


print("\n" + "=" * 60)
print("ПЕРЕМІШАНИЙ ТЕКСТ")
print("=" * 60)

shuffled_text = shuffle_text(text)

shuffled_h0 = calculate_entropy(shuffled_text)

shuffled_h1 = calculate_bigram_entropy(shuffled_text)

print(f"H₀ перемішаного тексту = {shuffled_h0:.4f}")

print(f"H₁ перемішаного тексту = {shuffled_h1:.4f}")



# Випадковий текст


print("\n" + "=" * 60)
print("ВИПАДКОВИЙ ТЕКСТ")
print("=" * 60)

alphabet = list(set(text))

random_text = generate_random_text(
    alphabet,
    len(text)
)

random_h0 = calculate_entropy(random_text)

random_h1 = calculate_bigram_entropy(random_text)

print(f"H₀ випадкового тексту = {random_h0:.4f}")

print(f"H₁ випадкового тексту = {random_h1:.4f}")




plot_entropy_convergence(text)