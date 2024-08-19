import collections

def getFolderNames(names):
    exists = set()
    last = collections.defaultdict(int)
    result = []
    for name in names:
        k = last[name]
        modified = name
        while modified in exists:
            k += 1
            modified = f'{name}({k})'
        last[name] = k
        result.append(modified)
        exists.add(modified)
    return result


# ["a(1)", "a", "a(2)"]
print(getFolderNames(["a", "a(1)", "a"]))


# # ["kaido","kaido(1)","kaido(2)","kaido(1)(1)","kaido(2)(1)"]
# print(getFolderNames(["kaido","kaido(1)","kaido","kaido(1)","kaido(2)"]))
#
#
# # ["wano","wano(1)","wano(2)","wano(3)"]
# print(getFolderNames(["wano","wano","wano","wano"]))
#
#
# # ["pes","fifa","gta","pes(2019)"]
# print(getFolderNames(["pes", "fifa", "gta", "pes(2019)"]))
#
#
# # ["pes","fifa","pes(1)"]
# print(getFolderNames(["pes", "fifa", "pes"]))
#
#
# # ["gta","gta(1)","gta(2)","avalon"]
# print(getFolderNames(["gta", "gta(1)", "gta", "avalon"]))
#
#
# # ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]
# print(getFolderNames(["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]))
