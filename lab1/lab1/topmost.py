import sys
import urllib.request
import wordfreq

def main():
    stopWordsfile= sys.argv[1]
    source= sys.argv[2]
    n = int(sys.argv[3])

    stopWords = []
    with open(stopWordsfile, encoding="utf-8")as file:
        for line in file:
            stopWords.append(line.strip())

    if source.startswith("http://") or source.startswith("https://"):
        response = urllib.request.urlopen(source)
        lines = response.read().decode("utf8").splitlines()
        words = wordfreq.tokenize(lines)
    else: 
        with open(source, encoding="utf-8")as file:
            words = wordfreq.tokenize(file)

    
    frequencies= wordfreq.countWords(words, stopWords)
    wordfreq.printTopMost(frequencies, n)

main()