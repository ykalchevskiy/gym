def renumerate(array):
    items = sorted((item, i) for i, item in enumerate(array))
    new_items = [None] * len(array)
    for index, (_, order) in enumerate(items):
        new_items[order] = index
    return new_items
