# QUESTION ID: "EZSTIQ0002"


def get_words(input_str):
    words = [x.strip() for x in input_str.split(" ") if x.strip()]
    return words


def get_swapped_words(words):
    swapped_words = []
    for w in words:
        swapped_word = [w[0]]
        for i in range(1, len(w) - 1, 2):
            if (i + 1) < len(w) - 1:
                if str.isalpha(w[i + 1]) and str.isalpha(w[i]):
                    swapped_word.append(w[i + 1])
                    swapped_word.append(w[i])
                else:
                    swapped_word.append(w[i])
                    swapped_word.append(w[i + 1])
            else:
                swapped_word.append(w[i])

        if len(w) > 1:
            swapped_word.append(w[-1])
        swapped_words.append("".join(swapped_word))
    return swapped_words

# Main Function: swap_chars
def swap_chars(input_str):
    # TODO: implement the real logic here!!!
    # raise NotImplementedError("TODO: implement the real logic here!!!")
    words = get_words(input_str)
    swapped_words = get_swapped_words(words)
    return " ".join(swapped_words)


def test_swap_chars():
    assert swap_chars("Hello World") == "Hlelo Wrold"
    assert swap_chars("Hello   World") == "Hlelo Wrold"
    assert swap_chars("Hello +-  World") == "Hlelo +- Wrold"
    assert swap_chars("Hello +-ab  World") == "Hlelo +-ab Wrold"
    assert swap_chars("Hello +-ab-  World") == "Hlelo +-ab- Wrold"
    assert swap_chars("Hello +ab-  World") == "Hlelo +ba- Wrold"
    assert swap_chars("Hello +-+ab-+-  World") == "Hlelo +-+ba-+- Wrold"
    assert swap_chars("abc") == "abc"
    assert swap_chars("abcd") == "acbd"
    assert swap_chars("abcd ") == "acbd"
    assert swap_chars("I will be back!?!") == "I wlil be bcak!?!"
    x = """The 14 English Punctuation Marks With Examples
By Ali Hale
Punctuation-marks

Do you know how to use punctuation marks correctly in English? While some might seem straightforward, you may come across punctuation marks that you’re unsure about … so this post is designed to serve as a handy reference."""
    assert swap_chars(x) == """The 14 Egnilsh Pnutcauiton Mraks Wtih Eaxpmels
By Ali Hlae
uPcnuttaoin-amkrs

Do you konw how to use pnutcauiton mraks croertcly in Egnilhs? Wihle smoe mgiht seem srtiahgftroawdr, you may cmoe arcsos pnutcauiton mraks taht yuo’re usnrue aobut … so tihs psot is dsegiend to sreve as a hnady rfereneec."""
    

if __name__ == "__main__":
    test_swap_chars()
