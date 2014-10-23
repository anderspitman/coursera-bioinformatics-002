INPUT_TEXT = "GATTACA"

from frequency_array import computing_frequencies, number_to_pattern2

def pattern_count(text, pattern):
    count = 0
    len_pattern = len(pattern)
    for i in range(0, len(text)-len_pattern+1):
        if text[i:i+len_pattern] == pattern:
            count += 1
    return count

def frequent_words(text, k):
    freq = []
    count = []
    for i in range(0, len(text)-k+1):
        pattern = text[i:i+k]
        pat_count = pattern_count(text, pattern)
        count.append(pat_count)
    max_count = sorted(count, reverse=True)[0]
    for i in range(0, len(text)-k+1):
        if count[i] == max_count:
            if not text[i:i+k] in freq:
                freq.append(text[i:i+k])
    return freq

def fast_frequent_words(text, k):
    freq = []
    freq_arr = computing_frequencies(text, k)
    max_val = max(freq_arr)
    num_kmers = len(text)-k+1
    for i in range(0, 4**k):
        if freq_arr[i] == max_val:
            pattern = number_to_pattern2(i, k)
            freq.append(pattern)
    return freq

if __name__ == "__main__":
    freq = frequent_words(INPUT_TEXT, 3)
    for word in freq:
        print word
    print
    fastfreq = fast_frequent_words(INPUT_TEXT, 3)
    for word in fastfreq:
        print word
