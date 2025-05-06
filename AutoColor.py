#　Based on the parts of the Part name separated by underscores (_), assign colors. 
# If the prefix (i.e., the part before the first underscore) is the same, 
# assign it the same color. 
# If the name contains two parts separated by underscores (e.g., OOO_OOO_XXX), 
# assign the first two parts the same color, and follow the necessary logic for color assignment. 
#　Specifically, if the name contains one underscore (e.g., OOO_XXX), set num_underscores = 1; 
# if the name contains two underscores (e.g., OOO_OOO_XXX), set num_underscores = 2, and so on.

import Adams

num_underscores = 2

color_list = [
    'RED', 'GREEN', 'BLUE', 'CYAN', 'MAGENTA', 'SKYBLUE', 'MIDNIGHT_BLUE', 'BLUE_GRAY', 'DARK_GRAY', 
    'SILVER', 'PEACH', 'MAIZE', 'Aquamarine', 'BlueViolet', 'Brown', 'CadetBlue', 'ClayRed', 'Coral', 
    'CornflowerBlue', 'DkGreen', 'DkOliveGreen', 'DkOrchid', 'DkSlateBlue', 'DkSlateGray', 'DkTurquoise',
    'DkYellow', 'DkRed', 'Firebrick', 'ForestGreen', 'Goldenrod', 'Gray', 'GreenYellow', 'Khaki', 'LtBlue', 
    'LtGray', 'LtKhaki', 'LtMagenta', 'LtSteelBlue', 'LimeGreen', 'Marine', 'Maroon', 'MedAquamarine', 'MedBlue', 
    'MedForest', 'MedGolden', 'MedOrchid', 'MedSeaGray', 'MedSlateBlue', 'MedSpring', 'MedTurquoise', 'MedViolet', 
    'MidnightBlue2', 'Navy', 'NearRed', 'NearWhite', 'NiceGreen', 'Orange', 'Orange2', 'Orchid', 'PaleGreen', 'Pink', 
    'Plum', 'Salmon', 'SeaGreen', 'Sienna', 'SlateBlue', 'SlateBlue2', 'SpringGreen', 'SteelBlue', 'Tan', 'Tan2', 
    'Thistle', 'Turquoise', 'Violet', 'VioletRed', 'VlMagenta', 'VlGray', 'Wheat', 'YellowGreen', 'YELLOW'
]


prefix_color_map = {}

def get_color_for_prefix(part_name, num_underscores=1):
    prefix = part_name.split('_')[:num_underscores]
    prefix_name = '_'.join(prefix)

    if prefix_name not in prefix_color_map:
        color = color_list[(len(prefix_color_map) % len(color_list))-1]
        prefix_color_map[prefix_name] = Adams.Colors[color]
    
    return prefix_color_map[prefix_name]

for model in Adams.Models.values():
    for part in model.Parts.values():
        color = get_color_for_prefix(part.name, num_underscores)

        for geometry in part.Geometries.values():
            geometry.color = color