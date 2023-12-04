from forest import Forest
from tree import Tree

file = 'map.txt'
amazon = Forest()

forest_dimenstions = amazon.get_dimensions(file)
blank_forest = amazon.make_empty_forest(forest_dimenstions)        
forest_of_trees = amazon.fill_with_trees(file, blank_forest)
# blank_forest_for_heights = amazon.make_empty_forest(forest_dimenstions)
# forest_of_heights = amazon.fill_with_heights(file, blank_forest_for_heights)
max_score = 0
for row in forest_of_trees:
    for tree in row:
        left = tree.rec_left(tree.y_coord, tree.x_coord, forest_of_trees)
        right =  tree.rec_right(tree.y_coord, tree.x_coord, forest_of_trees)
        up = tree.rec_up(tree.y_coord, tree.x_coord, forest_of_trees)
        down= tree.rec_down(tree.y_coord, tree.x_coord, forest_of_trees)
        score = left * right* up * down
        if score > max_score:
            max_score = score
        # print(f"y is {tree.y_coord} x is {tree.x_coord}  score is {tree.scenic_score} height is {tree.height}")
# print(forest_of_trees)
print(max_score)





# for row in forest_of_trees:
#     amazon.add_line_to_rows(row)
#     tallest_tree = -1
#     for tree in row:
#         if tree.height > tallest_tree:
#             tree.spotted = True
#             tallest_tree = tree.height
        
# for row in forest_of_trees:
#     tallest_tree = -1
#     for tree in reversed(row):
#         if tree.height > tallest_tree:
#             tree.spotted = True
#             tallest_tree = tree.height


# flipped_grid = [list(column) for column in zip(*forest_of_trees)]

# for row in flipped_grid:
#     amazon.add_line_to_col(row)
#     tallest_tree = -1
#     for tree in row:
#         if tree.height > tallest_tree:
#             tree.spotted = True
#             tallest_tree = tree.height

# for row in flipped_grid:
#     tallest_tree = -1
#     for tree in reversed(row):
#         if tree.height > tallest_tree:
#             tree.spotted = True
#             tallest_tree = tree.height

# counter = 0
# for row in forest_of_trees:
#     for tree in row:
#         if tree.spotted == True:
#             counter +=1

# print(counter)
# print(amazon.rows)
# print(amazon.columns)