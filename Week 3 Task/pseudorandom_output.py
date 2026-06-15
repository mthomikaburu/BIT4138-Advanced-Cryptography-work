from lfsr import lfsr

seed = [1,0,0,1,1]
taps = [0,2]
sequence = lfsr(seed, taps, 50)

print("Generated Pseudorandom Sequence:")
print(sequence)
