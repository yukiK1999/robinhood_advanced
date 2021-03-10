
def filter(data, info=None, prefix=None):
    if info is None:
        return data
    return {prefix + s:data[s] for s in info}
