def swap_unique_keys_values(d):
    
    unique_values = list(set(d.values()))

    d = {v:k for k,v in d.items()}
    new_d = {}

    for key in unique_values:
        if key in d:
            new_d[key] = d[key]
    return new_d





dic = {"a":4, "b":7, "c":10, "d":7}

print(swap_unique_keys_values(dic))
