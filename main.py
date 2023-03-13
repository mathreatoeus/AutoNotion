import NotionAPI

# Information on the integration and databases

token = 'secret_WwmU9iObdjb8JpPY2ma1XuZxDYB7EefddmftQmLdw95'
active_comp_database_id = '367744f9e2c6436a931e76dfb3d63daa'
passive_comp_database_id = '76b974da090a47439640a2845d4ba7fb'

read_headers = {
    'Authorization': 'Bearer ' + token,
    'Notion-Version': '2022-06-28'
}

write_headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28'
}


