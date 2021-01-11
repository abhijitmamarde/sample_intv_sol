# QUESTION ID: "EZSTIQ0001"


def get_words(input_str):
    words = [x.strip() for x in input_str.split(" ") if x.strip()]
    return words


def get_swapped_words(words):
    swapped_words = []
    for w in words:
        swapped_word = []
        for i in range(0, len(w), 2):
            if (i + 1) < len(w):
                if str.isalpha(w[i + 1]) and str.isalpha(w[i]):
                    swapped_word.append(w[i + 1])
                    swapped_word.append(w[i])
                else:
                    swapped_word.append(w[i])
                    swapped_word.append(w[i + 1])
            else:
                swapped_word.append(w[i])
            
        swapped_words.append("".join(swapped_word))
    return swapped_words


# Main Function: "swap_chars"
def swap_chars(input_str):
    # TODO: implement the real logic here!!!
    # raise NotImplementedError("TODO: implement the real logic here!!!")
    words = get_words(input_str)
    swapped_words = get_swapped_words(words)
    return " ".join(swapped_words)


def test_swap_chars():
    assert swap_chars("Hello World") == "eHllo oWlrd"
    assert swap_chars("Hello   World") == "eHllo oWlrd"
    assert swap_chars("Hello +-  World") == "eHllo +- oWlrd"
    assert swap_chars("Hello +-ab  World") == "eHllo +-ba oWlrd"
    assert swap_chars("This is    a   sample Test string !?!") == "hTsi si a aspmel eTts tsirgn !?!"
    assert swap_chars("abc") == "bac"
    assert swap_chars("abc ") == "bac"
    assert swap_chars("abc.") == "bac."
    assert swap_chars("I will be back!") == "I iwll eb abkc!"
    x = swap_chars("""The 14 English Punctuation Marks With Examples
By Ali Hale
Punctuation-marks

Do you know how to use punctuation marks correctly in English? While some might seem straightforward, you may come across punctuation marks that you’re unsure about … so this post is designed to serve as a handy reference.""")
    assert x == """hTe 14 nElgsih uPcnuttaoin aMkrs iWht xEmalpse
By lAi aHel
Pnutcauitno-mrask

oD oyu nkwo ohw ot sue upcnuttaoin amkrs ocrrcelty ni nElgsih? hWlie osem imhgt esme tsargithofwrrad, oyu amy ocem caorss upcnuttaoin amkrs htta oyu’er nuuser bauot … os htsi opts si edisngde ot esvre sa a ahdny erefercne."""

    
if __name__ == "__main__":
    test_swap_chars()
