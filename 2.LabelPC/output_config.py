import pickle


def main():
    P_dict = open('../DATA/Temp/P_dict_labelled.p', 'rb')
    P_dict = pickle.load(P_dict)

    asset_list = {
        'surface_course': [255, 0, 255],  # Magenta
        'sidewalk': [0, 255, 255],  # Cyan
        'arrow_straight': [255, 255, 0],  # Yellow
        'arrow_turn': [255, 0, 0],  # Red
        'arrow_multi': [0, 255, 0],  # Lime
        'centre_line_solid': [0, 0, 255],  # Blue
        'lane_line_dashed': [128, 128, 0],  # Olive
        'lane_line_solid': [128, 0, 0],  # Maroon
        'transverse_give_way': [0, 128, 0],  # Green
        'hatched_markings': [0, 0, 128],  # Navy
        'crossing_zebra': [0, 128, 128],  # Teal

        'foliage': [113, 113, 113],
        'sign': [83, 83, 83],
        'pole': [82, 82, 82],
        'traffic_light': [81, 81, 81],
        'fence': [67, 67, 67],
        'bollard': [66, 66, 66],
        'bin': [85, 85, 85],
        'building': [97, 97, 97],
        'wall': [84, 84, 84],
        'car': [161, 161, 161],
        'human': [164, 164, 164],
        'cycle': [165, 165, 165],
        'unknown': [168, 168, 168],
        'unlabelled': [255, 255, 255],
        'other': [0, 0, 0]
}

    # remove lines of assets not in "asset_list"
    P_dict_temp = []
    for line in P_dict:
        for i in asset_list:
            j = line.asset_type
            if i == j:
                line.color = asset_list[i]
                P_dict_temp.append(line)
                continue

    P_dict = P_dict_temp

    pickle.dump(P_dict, open('../DATA/Temp/output.p', "wb"))
    print("Configuration completed")


main()
