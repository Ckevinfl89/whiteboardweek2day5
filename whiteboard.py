# Pair of gloves
# Winter is coming, you must prepare your ski holidays. The objective of this kata is to determine the number of pair of gloves you can constitute from the gloves you have in your drawer.

# Given an array describing the color of each glove, return the number of pairs you can constitute, assuming that only gloves of the same color can form pairs.

# Examples:
# input = ["red", "green", "red", "blue", "blue"]
# result = 2 (1 red pair + 1 blue pair)

# input = ["red", "red", "red", "red", "red", "red"]
# result = 3 (3 red pairs)

def solution(dummy_list):
    running_count = 0
    colors_count= {}
    glove_colors = set(dummy_list)
    for color in glove_colors:
        counted_gloves = dummy_list.count(color)
        colors_count[color] = counted_gloves

    for i, color in enumerate(colors_count):
        running_count += colors_count[color] // 2 
         
    return running_count    

