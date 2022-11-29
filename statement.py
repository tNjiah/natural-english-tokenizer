import re




class statement_tokenizer:
    def __init__(self):

        self._pattern = r"[A-Z]+[a-z]*\s\."
        self._sentence_pattern = r'([A-Z][^\.!?]*[\.!?])'
        self._word_pattern = r'\w+'
        self._regex = re.compile(self._sentence_pattern)
        self._tokens = []

    def get_tokens(self, text) -> list:

        self._tokens = self.peformSentenceSplit(text)
        return self._tokens

    def __str__(self) -> str:

        for s in self._tokens:
            print(f"statement -> {s}")

    def __repr__(self) -> str:

        for s in self._tokens:
            print(f"statement -> {s}")

    def peformSentenceSplit(self, text):

        formatter = re.compile(self._sentence_pattern, re.M)
        return formatter.findall(text)

    def performWordSplit(self, text):

        formatter = re.compile(self._word_pattern, re.M)
        return formatter.findall(text)

    def getAllTokens(self, text):

        textData = self.retainAllTokens(text)
        return textData.split()

    def retainAllTokens(self, text):
     
        new_text = ""
        for i in range(len(text)):
            if re.match(r'\.|,|\?|\'|\)|\}|\]|\:|\;', text[i]):
                new_text = new_text+" "+text[i]
            elif re.match(r'\(|\{|\[|\s', text[i]):
                new_text = new_text+text[i]+" "
            else:
                new_text = new_text+text[i]
        return new_text


if __name__ == "__main__":
    data = statement_tokenizer()
    text = """ Living without computers today is close to an impossibility?
      As our reliance on computers and computer-controlled technologies grows the computer has evolved from a luxury item to a necessity."""
    # checker = data.get_tokens(text)

    # for i in checker:
    #     print(data.performWordSplit(i))
    print(data.getAllTokens(text.strip()))
