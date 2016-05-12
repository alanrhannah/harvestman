def split_list_of_queries(filepath):
    """
    Read from a file and split into list by new lines

    :param filepath:  a string path to file
    :returns keyword_list:  a list of strings 
    """
    with open(filepath, 'r') as keyphrase_file:
        keyword_list = keyphrase_file.read().splitlines()

    return keyword_list

def update_url_start_index_parameter(start_index):
    """
    Update string with correct integer
    
    :return '&start=<int>':  a formatted string
    """
    return '&start={}'.format(start_index)
