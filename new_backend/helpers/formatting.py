def change_keys(dic, new_keys):
    if len(new_keys) != len(dic.items()):
        raise IndexError("the number of new keys doesn't match the number of items")
    else:
        return {
            new_keys.pop(0) : value for key, value in dic.items()
        }

def change_keys_in_list(dicts, new_keys):
    return [ change_keys(dic, list(new_keys)) for dic in dicts ]
