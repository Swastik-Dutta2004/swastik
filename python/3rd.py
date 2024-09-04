world_animals = ["Anaconda", "Platypus", "Red panda", "Beaver", "Killer whale", "Platypus", "Camel", "Polar bear", "King penguin", "Snow leopard", "Zebra", "Plains bison"]
world_biomes = ["Tropical Rainforest", "Temperate Forest", "Taiga", "Marine", "Freshwater", "Desert", "Arctic Tundra", "Antarctic Tundra", "Alpine Tundra", "Tropical Grassland", "Temperate Grassland"]
def check_item_in_list(item, list_name):
    return item in list_name

is_anaconda_in_animals = check_item_in_list("Anaconda", world_animals)
is_forest_in_biomes = check_item_in_list("Forest", world_biomes)

print(f"Is 'Anaconda' in world_animals? {is_anaconda_in_animals}")
print(f"Is 'Forest' in world_biomes? {is_forest_in_biomes}")
