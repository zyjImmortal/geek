

def print_list_node(list_node):
    result = []
    while list_node != None:
        result.append(list_node.val)
        list_node = list_node.next
    return '->'.join(result)

import requests

