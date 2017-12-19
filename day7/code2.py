'''
--- Part Two ---

The programs explain the situation: they can't get down. Rather, they could get down, if they weren't expending all of their energy trying to keep the tower balanced. Apparently, one program has the wrong weight, and until it's fixed, they're stuck here.

For any program holding a disc, each program standing on that disc forms a sub-tower. Each of those sub-towers are supposed to be the same weight, or the disc itself isn't balanced. The weight of a tower is the sum of the weights of the programs in that tower.

In the example above, this means that for ugml's disc to be balanced, gyxo, ebii, and jptl must all have the same weight, and they do: 61.

However, for tknk to be balanced, each of the programs standing on its disc and all programs above it must each match. This means that the following sums must all be the same:

ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251
padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243
fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243
As you can see, tknk's disc is unbalanced: ugml's stack is heavier than the other two. Even though the nodes above ugml are balanced, ugml itself is too heavy: it needs to be 8 units lighter for its stack to weigh 243 and keep the towers balanced. If this change were made, its weight would be 60.

Given that exactly one program is the wrong weight, what would its weight need to be to balance the entire tower?
'''
import json
import re
f = open("./inputs/day7","r")

towers = []


# reading input in a list of towers
for line in f:
    tower = {}
    line = line.split()
    tower["aa_name"] = line[0]
    match = re.search('[0-9]+',line[1]) # extract the weight from the parenthesis
    weight = (str(match.group()))
    tower["aa_weight"] = int(weight)
    if len(line) > 2:
        tower["children"] = []
        for i in range(3, len(line)):
            child_name = line[i].split(',')[0] # remove the coma from the name
            tower["children"].append(child_name)

    towers.append(tower)

# arranging the towers in a tree

def create_tree(tree,root):
    #print(tree)
    #print(json.dumps(towers, indent=4, sort_keys=True))
    for tower in towers:
        if tower["aa_name"] == root:
            #print(root)
            tree["aa_name"] = root
            tree["aa_weight"] = tower["aa_weight"]
            towers.remove(tower)
            tree["aa_children_weight"] = 0
            if "children" in tower:
                #print(root)
                tree["children"] = []
                for tower_child in tower["children"]:
                    child = {}
                    #child["name"] = tower_children
                    child_name = tower_child
                    #print(tower_children)
                    child = create_tree(child,child_name)
                    tree["children"].append(child)

    return tree

def search_tree(tree):
    #print(tree["aa_name"])
    if "children" in tree:
        for i in tree["children"]:  
            #print(i["aa_name"])
            tree["aa_children_weight"] += search_tree(i)
            #print(tree["aa_children_weight"])
        return int(tree["aa_children_weight"]) + tree["aa_weight"]
    #print(tree["weight"])
    else:
        return int(tree["aa_weight"])

def check_tree(tree):
    if "children" in tree:
        subtower_weight_list = []
        for i in tree["children"]:
            check_tree(i)
            subtower_weight_list.append((i["aa_weight"] + i["aa_children_weight"]))
        #subtower_weight_list = list(set(subtower_weight_list))
        subtower_weight_list = sorted(subtower_weight_list)
        bb = "false"
        #print(subtower_weight_list)
        if subtower_weight_list[len(subtower_weight_list) - 1] != subtower_weight_list[len(subtower_weight_list) - 2]:
            unbalanced = subtower_weight_list[len(subtower_weight_list) - 1]
            balanced = subtower_weight_list[len(subtower_weight_list) - 2]
            bb = "true"
        elif subtower_weight_list[0] != subtower_weight_list[1]:
            unbalanced = subtower_weight_list[0]
            balanced = subtower_weight_list[1]
            bb = "true"
        if (bb == "true"):
            for i in tree["children"]:
                if (i["aa_weight"] + i["aa_children_weight"]) == unbalanced:
                    ww = i["aa_weight"]
                    #print(ww)
                    #print(i["aa_name"])
                    #print(balanced)
                    #print(unbalanced)
                    if balanced > unbalanced:
                        print(ww + abs(balanced-unbalanced))
                        return ww + abs(balanced-unbalanced)
                    else:
                        print(ww - abs(balanced-unbalanced))
                        return ww - abs(balanced-unbalanced)

def check_tree2(tree):
    if "children" in tree:
        subtower_weight_list = []
        for i in tree["children"]:
            subtower_weight_list.append(i["aa_children_weight"] + i["aa_weight"])
            print(i["aa_name"])
        #subtower_weight_list = sorted(subtower_weight_list)
        print(subtower_weight_list)

        
           
        
                
            
    #print(tree["weight"])
    #return int(tree["weight"])


#root = "tknk" # obtained from running the test example from Part1
root = "mwzaxaj" #obtained from running input code from Part1
#root = "xegshds"
tree = {}
tree = create_tree(tree,root)
#children_balanced = "yes"
search_tree(tree)
check_tree(tree) # the first printed number is the highes unbalanced tower

print(json.dumps(towers, indent=4, sort_keys=True))
print(json.dumps(tree, indent=4, sort_keys=True))