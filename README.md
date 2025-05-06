#　Based on the parts of the Part name separated by underscores (_), assign colors. 
# If the prefix (i.e., the part before the first underscore) is the same, 
# assign it the same color. 
# If the name contains two parts separated by underscores (e.g., OOO_OOO_XXX), 
# assign the first two parts the same color, and follow the necessary logic for color assignment. 
#　Specifically, if the name contains one underscore (e.g., OOO_XXX), set num_underscores = 1; 
# if the name contains two underscores (e.g., OOO_OOO_XXX), set num_underscores = 2, and so on.
