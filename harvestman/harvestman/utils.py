def split_list_of_queries(filepath):
    with open(filepath, 'r') as keyphrase_file:
        keyword_list = keyphrase_file.read().splitlines()
    return keyword_list