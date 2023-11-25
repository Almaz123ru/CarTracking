import json
import numpy as np

ZONE_IN_POLYGONS = [
    np.array([[592, 282], [900, 282], [900, 82], [592, 82]]),
    np.array([[950, 860], [1250, 860], [1250, 1060], [950, 1060]]),
    np.array([[592, 582], [592, 860], [392, 860], [392, 582]]),
    np.array([[1250, 282], [1250, 530], [1450, 530], [1450, 282]]),
]

def json_load():
    width = 1920
    height = 1080
    path_json = r"jsons/KRA-2-7-2023-08-22-evening.json"
    with open(path_json, 'r') as file:
        # Загружаем данные из JSON файла
        data = json.load(file)
        print(data['areas'])

    # Извлекаем 'areas' из данных

    areas_data = data['zones']
    pixel_polygon = (areas_data * np.array([width, height])).astype(int)
    zone_in = [pixel_polygon[0], pixel_polygon[2]]
    zone_out = [pixel_polygon[1], pixel_polygon[3]]


    # Преобразуем 'areas' в массив NumPy
    return zone_in, zone_out


zone_in, zone_out = json_load()

# Теперь переменная 'data' содержит данные из строки JSON
print(zone_in, zone_out)

#print(ZONE_IN_POLYGONS)
