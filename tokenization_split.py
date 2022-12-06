import regex as re
import DemoTokenizer 

if __name__ =="__main__":
    f = open(r'./assets/tokenized.txt', 'r')
    tokenized = f.read()
    f.close()
    if re.search(r'[A-Z].*',tokenized):
          sentenceProcessing ="".join(DemoTokenizer.DemoTokenizer.performSentenceSplit(tokenized))  # type: ignore
          data =   DemoTokenizer.DemoTokenizer.performWordSplit(sentenceProcessing)
          print(data)
        #   print( DemoTokenizer. DemoTokenizer.tag(data))  # type: ignore
    else:
        print("Invalid")
        



