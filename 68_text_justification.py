from math import ceil

def get_next_sentence_data(words, max_width, index):
    i, current_width = index, 0
    while i < len(words):
        current_width += len(words[i]) + 1
        if current_width-1 > max_width:
            break
        i += 1
    if i < len(words):
        words_width = current_width - len(words[i]) - (i - index) - 1
    else:
        words_width = current_width - 1
    return i, words_width, i >= len(words)


def pad_with_spaces(words, words_width, sentence_width, is_last_sentence):
    remaining_spaces = sentence_width - words_width
    if is_last_sentence:
        return " ".join(words) + (" " * remaining_spaces)
    gaps = len(words) - 1
    sentence = []
    if not gaps:
        sentence.append(words[-1])
        sentence.append(" " * remaining_spaces)
    else:
        for i in range(len(words)-1):
            sentence.append(words[i])
            spaces = ceil(remaining_spaces/gaps)
            sentence.append(" " * spaces)
            remaining_spaces -= spaces
            gaps -= 1
        sentence.append(words[-1])
    return "".join(sentence)


def fullJustify(words, maxWidth):
    i, j, n = 0, 0, len(words)
    text = []
    while i < n:
        j, words_total_len, is_last = get_next_sentence_data(words, maxWidth, j)
        sentence = pad_with_spaces(words[i:j], words_total_len, maxWidth, is_last)
        text.append(sentence)
        i = j
    return text


print(fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]


#print(fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16))
# # [
# #   "What   must   be",
# #   "acknowledgment  ",
# #   "shall be        "
# # ]
#
#
#print(fullJustify(
#     ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
#      "Art", "is", "everything", "else", "we", "do"], 20))
# # [
# #   "Science  is  what we",
# #   "understand      well",
# #   "enough to explain to",
# #   "a  computer.  Art is",
# #   "everything  else  we",
# #   "do                  "
# # ]
