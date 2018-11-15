import json


def conv_obj_to_dict(obj, all=True, keys=[], inex='in'):
    """Converts an object to a dictionary with
    the keys specified in the third parameter if the second paramter
    is not filled. The second parameter will include all keys that have 
    jsonable values. The fourth parameter will say to include or exclude the keys"""

    if all == True and inex == 'in':
        return {key: obj[key] for key in obj if is_jsonable(obj[key])}

    if all == True and inex == 'ex':
        return {}

    if inex == 'in':
        return {key: obj[key] for key in keys if is_jsonable(obj[key])}

    if inex == 'ex':
        return {key: obj[key] for key in obj if is_jsonable(obj[key] and key not in keys)}

    # Throw an error if the wrong parameters were passed
    raise Exception('Invalid parameters')


def update_obj_with_data(obj, data):
    """Will update an object's attributes with the data specified"""
    for key in data:
        if data[key] != '':
            obj[key] = data[key]


def is_jsonable(data):
    try:
        json.dumps(data)
        return True
    except:
        return False
