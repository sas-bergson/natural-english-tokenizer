from tokenizer import StatementTokenizer

if __name__ == '__main__':
    sentence = "Xian phrase xenia now xes needing many word. This is the xenia second phrase!"
    st = StatementTokenizer(sentence)
    st.run()

