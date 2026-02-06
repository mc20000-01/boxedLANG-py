import box_to_json as b2j

def to_py(code_json)
    py = ""
    for i in code_json:
        cmd = i['cmd']
        args = i['args']
        if cmd == "say":
