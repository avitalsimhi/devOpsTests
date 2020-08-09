pattern_size = 9
for t in range(pattern_size):
    pattern = list(" " * pattern_size)
    pattern[t] = "*"
    pattern[-(t+1)] = "*"
    print("".join(pattern))