#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict):
        return None

    return list(dict(sorted(a_dictionary.items(),
                            key=lambda item: item[1])))[-1]
