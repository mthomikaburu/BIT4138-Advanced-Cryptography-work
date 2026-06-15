def lfsr(seed, taps, length=20):
    sr = seed[:]  # shift register
    output = []
    for _ in range(length):
        new_bit = 0
        for t in taps:
            new_bit ^= sr[t]
        output.append(sr[-1])
        sr = [new_bit] + sr[:-1]
    return output


seed = [1,0,0,1,1]  # initial state
taps = [0,2]        # feedback taps
sequence = lfsr(seed, taps, 20)
print("LFSR Output:", sequence)
