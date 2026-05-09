import heapq
import math
from collections import Counter


text = "ABBCCCDDDABCDABCDABCD" * 100


frequencies = Counter(text)
total_symbols = len(text)

probabilities = {
    symbol: count / total_symbols
    for symbol, count in frequencies.items()
}


class Node:
    def __init__(self, symbol=None, prob=0):
        self.symbol = symbol
        self.prob = prob
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.prob < other.prob


heap = []

for symbol, prob in probabilities.items():
    heapq.heappush(heap, Node(symbol, prob))

while len(heap) > 1:
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)

    merged = Node(prob=left.prob + right.prob)
    merged.left = left
    merged.right = right

    heapq.heappush(heap, merged)

root = heap[0]


codes = {}

def generate_codes(node, code=""):

    if node is None:
        return

    if node.symbol is not None:
        codes[node.symbol] = code
        return

    generate_codes(node.left, code + "0")
    generate_codes(node.right, code + "1")

generate_codes(root)


entropy = -sum(
    p * math.log2(p)
    for p in probabilities.values()
)


average_length = sum(
    probabilities[symbol] * len(code)
    for symbol, code in codes.items()
)


print("\nТаблиця кодів Хаффмана:\n")

print(f"{'Символ':<10}{'Ймовірність':<15}{'Код':<15}{'Довжина'}")

for symbol in sorted(codes.keys()):
    print(
        f"{symbol:<10}"
        f"{probabilities[symbol]:<15.4f}"
        f"{codes[symbol]:<15}"
        f"{len(codes[symbol])}"
    )

print("\nЕнтропія H =", round(entropy, 4))
print("Середня довжина коду L =", round(average_length, 4))
print("L - H =", round(average_length - entropy, 4))