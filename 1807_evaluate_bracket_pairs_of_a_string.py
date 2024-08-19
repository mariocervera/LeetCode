
def get_closed_bracket_index(s, start):
    i = start
    while i < len(s) and s[i] != ")":
        i += 1
    return i


def evaluate(s, knowledge):
    ht = {pair[0]: pair[1] for pair in knowledge}
    i, res = 0, []
    while i < len(s):
        if s[i] != "(":
            res.append(s[i])
            i += 1
        else:
            j = get_closed_bracket_index(s, i)
            k = s[i+1:j]
            if k in ht:
                res.extend(ht[s[i+1:j]])
            else:
                res.extend(["?"])
            i = j+1
    return "".join(res)


print(evaluate("(name)is(age)yearsold", [["name", "bob"], ["age", "two"]]))  # "bobistwoyearsold"
print(evaluate("hi(name)", [["a", "b"]]))  # "hi?"
print(evaluate("(a)(a)(a)aaa", [["a", "yes"]]))  # "yesyesyesaaa"
