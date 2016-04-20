def split_list_of_queries(filepath):
    with open(filepath, 'r') as keyphrase_file:
        keyword_list = keyphrase_file.read().splitlines()
    return keyword_list

def update_url_start_index_parameter(start_index):
    return '&start={}'.format(start_index)
