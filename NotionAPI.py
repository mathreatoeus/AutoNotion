import requests, json


def read_database(database_id, headers_dict):
    '''
    Reads the data from the pages of the target database and writes them to a
    json file.

    Parameters:
    - database_id: id of the target database;
    - headers_dict: dictionary containing the required headers for the request.

    Returns:
    Status of the HTTP request.
    '''

    read_url = f'https://api.notion.com/v1/databases/{database_id}/query'
    req = requests.request('POST', read_url, headers=headers_dict)
    data = req.json()

    with open('./db_log.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)

    return req.status_code


def add_passive_component(database_id, headers_dict, type, value, location, power=None,
tolerance=None, voltage=None, package='0805', status='Comprado'):
    '''
    Creates a page with the given data in the passive components database.

    Parameters:
    - database_id: id of the targeted database;
    - headers_dict: dictionary containing the required headers for the request;
    - All the other parameters are component specific.

    Returns:
    Status of the HTTP request.
    '''

    write_url = 'https://api.notion.com/v1/pages'

    new_data = {
        'parent': {'database_id': database_id},
        'properties': {
            'Tipo': {
                'select': {
                    'name': type
                }
            },
            'Valor': {
                'title': [
                    {
                        'text': {
                            'content': value
                        }
                    }
                ]
            },
            'Package': {
                'select': {
                    'name': package
                }
            },
            'Potência': {
                'rich_text': [
                    {
                        'text': {
                            'content': power
                        }
                    }
                ]
            },
            'Tolerância': {
                'rich_text': [
                    {
                        'text': {
                            'content': tolerance
                        }
                    }
                ]
            },
            'Voltagem': {
                'rich_text': [
                    {
                        'text': {
                            'content': voltage
                        }
                    }
                ]
            },
            'Status': {
                'select': {
                    'name': status
                }
            },
            'Localização': {
                'rich_text': [
                    {
                        'text': {
                            'content': location
                        }
                    }
                ]
            }
        }
    }

    data = json.dumps(new_data)
    req = requests.request('POST', write_url, headers=headers_dict, data=data)
    
    return req.status_code

def add_active_component(database_id, headers_dict, name, type, value, datasheet,
quantity, location, status='Comprado'):
    '''
    Creates a page with the given data in the active components database.

    Parameters:
    - database_id: id of the targeted database;
    - headers_dict: dictionary containing the required headers for the request;
    - All the other parameters are component specific.

    Returns:
    Status of the HTTP request.
    '''

    write_url = 'https://api.notion.com/v1/pages'

    new_data = {
        'parent': {'database_id': database_id},
        'properties': {
            'Nome': {
                'title': [
                    {
                        'text': {
                            'content': name
                        }
                    }
                ]
            },
            'Tipo': {
                'slect': {
                    'name': type
                }
            },
            'Valor': {
                'rich_text': [
                    {
                        'text': {
                            'content': value
                        }
                    }
                ]
            },
            'Datasheet': {
                'rich_text': [
                    {
                        'text': {
                            'content': datasheet
                        }
                    }
                ]
            },
            'Status': {
                'select': {
                    'name': status
                }
            },
            'Quantidade': {
                'rich_text': [
                    {
                        'text': {
                            'content': quantity
                        }
                    }
                ]
            },
            'Localização': {
                'rich_text': [
                    {
                        'text': {
                            'content': location
                        }
                    }
                ]
            }
        }
    }

    data = json.dumps(new_data)
    req = requests.request('POST', write_url, headers=headers_dict, data=data)
    
    return req.status_code


def update_page(database_id, headers_dict):

    pass

