def simplifyPath(path):
    segments, stack = path.split("/"), []
    for segment in segments:
        if not segment or segment == ".":
            continue
        if segment == "..":
            if stack:
                stack.pop()
        else:
            stack.append(segment)
    return "/" + "/".join(stack)



print(simplifyPath("/home/"))  # /home
print(simplifyPath("/../"))  # /
print(simplifyPath("/home//foo/"))  # /home/foo
