(workflow_input, parts_input) = open("input.txt").read().split('\n\n')
workflow_input = workflow_input.split('\n')
parts_input = parts_input.split('\n')


workflows = {}
parts = [] #{x=787,m=2655,a=1222,s=2876}


for l in workflow_input:
    key, rest = l.split("{")
    vals_str = rest.split("}")[0]
    workflows[key] = vals_str.split(",")


for l in parts_input:
    rest = l[1:-1]
    all = rest.split(",")
    parts.append(list(map(lambda x: int(x[2:]), all)))


def parse_workflow(string):
    print(string)
    if ">" in string or "<" in string:
        category = string[0]
        comparison = string[1]
        num = int(string.split(string[1])[1].split(":")[0])
        destination = string.split(":")[1]
        return [category, comparison, num, destination]
    else:
        return {"final_dest": string}

categories = ["x", "m", "a", "s"]

total = 0

for p in parts:
    current_workflow = "in"

    while current_workflow not in "AR":
        w = workflows[current_workflow]
        for step in w:
            p_step = parse_workflow(step)
            print(p_step)
            if "final_dest" not in p_step:
                part_cat_num = p[categories.index(p_step[0])]
                if p_step[1] == ">":
                    if part_cat_num > p_step[2]:
                        # it matches, go to next workflow
                        current_workflow = p_step[3]
                        break
                    else:
                        # it doesnt match, go to next step
                        continue
                else:

                    if part_cat_num < p_step[2]:
                        # it matches, go to next workflow
                        current_workflow = p_step[3]
                        break
                    else:
                        # it doesnt match, go to next step
                        continue
            else:
                # we are at final dest
                current_workflow = p_step["final_dest"]
    
    if current_workflow == "A":
        total += sum(p)
                    

print(total)


