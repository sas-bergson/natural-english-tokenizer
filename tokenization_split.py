import regex as re
import DemoTokenizer 

if __name__ =="__main__":
    f = open('./assets/tokenized.txt', 'r')
    tokenized = f.read()
    f.close()
    if re.search(r'[A-Z].*',tokenized):
          sentenceProcessing ="".join(DemoTokenizer.DemoTokenizer.performSentenceSplit(tokenized))
          data =   DemoTokenizer.DemoTokenizer.performWordSplit(sentenceProcessing)
          print( DemoTokenizer. DemoTokenizer.tag(data))
    else:
        print("Invalid")
        


