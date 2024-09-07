
def destCity(paths):
    sources = {source for source, _ in paths}
    for _, destination in paths:
        if destination not in sources:
            return destination
    return None


print(destCity([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))  # "Sao Paulo"
print(destCity([["B", "C"], ["D", "B"], ["C", "A"]]))  # "A"
print(destCity([["A", "Z"]]))  # "Z"
