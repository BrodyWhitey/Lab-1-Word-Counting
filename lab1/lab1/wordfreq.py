def tokenize(lines):
    words= []

    for line in lines:
        start=0
        while start < len(line):
            while start < len(line) and line[start].isspace():
                start = start + 1
            if start >= len(line):
                break
            if line[start].isalpha():
                end = start
                while end < len(line) and line[end].isalpha():
                    end = end + 1
                words.append(line[start:end].lower())
                start=end
            elif line[start].isdigit():
                end=start

                while end < len(line) and line[end].isdigit():
                    end=end + 1
                words.append(line[start:end].lower())
                start=end
            else:
                words.append(line[start].lower())
                start= start + 1
    return words

def countWords(words, stopwords):
    start = 0
    frequencies = {}
    for word in words:
        if word not in stopwords:
            if word not in frequencies:
                frequencies[word] = 1
            else: 
                frequencies[word] = frequencies[word] +1
    return frequencies

def printTopMost(frequencies, n):
    sortedfreq = sorted(frequencies.items(), key=lambda x: -x[1])

    start= 0
    for word, freq in sortedfreq:
        if start < n:
            print(word.ljust(20) + str(freq).rjust(5))
            start = start + 1
        else: 
            break