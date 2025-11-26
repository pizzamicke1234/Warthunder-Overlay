import API.API as api

map_name, map_size = api.get_map_info()
print(f'Map: {map_name}, Size: {map_size}kmx{map_size}km')