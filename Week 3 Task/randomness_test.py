import random

def frequency_test(bits):
    zeros = bits.count(0)
    ones = bits.count(1)
    print(f"Zeros: {zeros}, Ones: {ones}")

def runs_test(bits):
    runs = 1
    for i in range(1, len(bits)):
        if bits[i] != bits[i-1]:
            runs += 1
    print(f"Runs: {runs}")



bits = [random.randint(0,1) for _ in range(100)]
print("Random Bits:", bits)
frequency_test(bits)
runs_test(bits)
