import os
import gzip
import lzma
import random
import string



# Текстовий файл
text = """
Інформаційні технології відіграють важливу роль у сучасному суспільстві.
""" * 5000

with open("text.txt", "w", encoding="utf-8") as f:
    f.write(text)

# Випадковий файл
random_text = ''.join(
    random.choices(string.ascii_letters + string.digits, k=200000)
)

with open("random.txt", "w") as f:
    f.write(random_text)

# Шаблонний файл
pattern_text = ("ABC123XYZ " * 20000)

with open("pattern.txt", "w") as f:
    f.write(pattern_text)



def compress_gzip(filename):
    with open(filename, 'rb') as f_in:
        with gzip.open(filename + '.gz', 'wb') as f_out:
            f_out.writelines(f_in)

def compress_xz(filename):
    with open(filename, 'rb') as f_in:
        with lzma.open(filename + '.xz', 'wb') as f_out:
            f_out.writelines(f_in)



files = ["text.txt", "random.txt", "pattern.txt"]

results = []

for file in files:

    original_size = os.path.getsize(file)

    # gzip
    compress_gzip(file)
    gzip_size = os.path.getsize(file + ".gz")

    gzip_ratio = gzip_size / original_size
    gzip_percent = (1 - gzip_ratio) * 100

    results.append([
        file,
        "gzip",
        original_size,
        gzip_size,
        round(gzip_ratio, 4),
        round(gzip_percent, 2)
    ])

    # xz
    compress_xz(file)
    xz_size = os.path.getsize(file + ".xz")

    xz_ratio = xz_size / original_size
    xz_percent = (1 - xz_ratio) * 100

    results.append([
        file,
        "xz",
        original_size,
        xz_size,
        round(xz_ratio, 4),
        round(xz_percent, 2)
    ])



print(
    f"{'Файл':15}"
    f"{'Алгоритм':10}"
    f"{'Початковий':15}"
    f"{'Стиснений':15}"
    f"{'Коеф.':10}"
    f"{'%':10}"
)

for row in results:
    print(
        f"{row[0]:15}"
        f"{row[1]:10}"
        f"{row[2]:15}"
        f"{row[3]:15}"
        f"{row[4]:10}"
        f"{row[5]:10}"
    )