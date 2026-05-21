def i_before_e(sentence):
    new: list = []
    for inWord, word in enumerate(sentence.split()):
        if "cie" in word:
            new.append(word.replace("cie", "cei"))
        elif "cei" not in word:
            new.append(word.replace("ei", "ie"))
        else:
            new.append(word)
    # return new
    return " ".join(new)
_
