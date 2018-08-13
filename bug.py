stopwords = open("stopwords", "r").read()


class Bug:
    def __init__(self):
        self.name = ""
        self.words = {}
        self.stopwords = stopwords

    def digest(self, text):
        if not text[0] == "!":
            text = text.lower()
            lines = text.splitlines()
            text = " ".join(lines)
            words = text.split(" ")
            fwords = []

            for w in words:
                nw = ""
                for c in w:
                    if c == "'":
                        break
                    elif not c == "!" and not c == "?" and not c == ".":
                        nw += c
                if nw not in self.stopwords:
                    fwords.append(nw)

            for w in fwords:
                w = w.replace(",", "")
                if w in self.words:
                    self.words[w] += 1
                else:
                    self.words[w] = 1

            print("digested {} words".format(len(fwords)))
