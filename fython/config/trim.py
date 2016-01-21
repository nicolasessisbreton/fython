import re

newline = '\n'
leading_space = re.compile('\s*')

def trim(s):
    # only strip when uniline
    if newline not in s:
        return s

    # multiline, so process
    lines = s.splitlines()

    # first line ignored
    lines = lines[1:]

    # determine minimum indentation 
    maxindent = float('inf')
    indent = maxindent
    for line in lines:
        if line.strip():
            current_indent = len(leading_space.findall(line)[0])
            indent = min(indent, current_indent)

    # remove indentation
    if indent < maxindent:
        trimmed = []
        for line in lines:
            if line.strip():
                trimmed.append(line[indent:])
            else:
                trimmed.append('')
    else:
        trimmed = lines

    # return a single string
    return '\n'.join(trimmed)