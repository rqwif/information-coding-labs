import heapq
from collections import Counter
from math import log2


def entropy(probabilities):
    return -sum(p * log2(p) for p in probabilities if p > 0)



class Node:
    def __init__(self, symbol=None, freq=0):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = [Node(sym, freq) for sym, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, current_code="", codes={}):
    if node is None:
        return

    if node.symbol is not None:
        codes[node.symbol] = current_code

    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)

    return codes



text = open("text.txt", "r", encoding="utf-8").read()

# Частоти символів
frequencies = Counter(text)

total = len(text)

# Ймовірності
probabilities = {
    symbol: freq / total
    for symbol, freq in frequencies.items()
}

# Ентропія
H = entropy(probabilities.values())

# Код Хаффмана
tree = build_huffman_tree(frequencies)
codes = generate_codes(tree)

# Середня довжина
L = sum(
    probabilities[symbol] * len(code)
    for symbol, code in codes.items()
)

# Ефективність
eta = H / L

# Надлишковість
R = 1 - eta


print(f"Ентропія H = {H:.4f}")
print(f"Середня довжина L = {L:.4f}")
print(f"Ефективність η = {eta:.4f}")
print(f"Надлишковість R = {R:.4f}")

print("\nКоди Хаффмана:")
for symbol, code in codes.items():
    print(f"{repr(symbol)} : {code}")