def search(query, data):
    """Функция поиска по данным."""
    results = [item for item in data if query in str(item)]
    return results
