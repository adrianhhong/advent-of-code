(workflow_input, parts_input) = open("input.txt").read().split('\n\n')
workflow_input = workflow_input.split('\n')
parts_input = parts_input.split('\n')


workflows = {}
parts = []


for l in workflow_input:
    key, rest = l.split("{")
    vals_str = rest.split("}")[0]
    workflows[key] = vals_str.split(",")


for l in parts_input:
    rest = l[1:-1]
    all = rest.split(",")
    parts.append(list(map(lambda x: int(x[2:]), all)))


def parse_workflow(string):
    if ">" in string or "<" in string:
        category = string[0]
        comparison = string[1]
        num = int(string.split(string[1])[1].split(":")[0])
        destination = string.split(":")[1]
        return {"category": category, "comparison": comparison, "num": num, "destination": destination}
    else:
        return {"final_dest": string}

categories = ["x", "m", "a", "s"]

total = 0

def travel(current_workflow, x, m, a, s):
    if x[0] > x[1]:
        return 0
    if m[0] > m[1]:
        return 0
    if a[0] > a[1]:
        return 0
    if x[0] > x[1]:
        return 0
    
    # base case
    if current_workflow == "A":
        print(x,m,a,s)
        return (x[1] - x[0] + 1) * (m[1] - m[0] + 1) * (a[1] - a[0] + 1) * (s[1] - s[0] + 1)
    if current_workflow == "R":
        return 0

    w = workflows[current_workflow]

    mini_total = 0

    for step in w:
        p_step = parse_workflow(step)
        if "final_dest" not in p_step:
            if p_step["comparison"] == ">":
                if p_step["category"] == "x":
                    new_range = tuple((max(p_step["num"], x[0])+1, x[1]))
                    mini_total += travel(p_step["destination"], new_range, m, a, s)
                    x = tuple((x[0], min(p_step["num"], x[1])))
                elif p_step["category"] == "m":
                    new_range = tuple((max(p_step["num"], m[0])+1, m[1]))
                    mini_total += travel(p_step["destination"], x, new_range, a, s)
                    m = tuple((m[0], min(p_step["num"], m[1])))
                elif p_step["category"] == "a":
                    new_range = tuple((max(p_step["num"], a[0])+1, a[1]))
                    mini_total += travel(p_step["destination"], x, m, new_range, s)
                    a = tuple((a[0], min(p_step["num"], a[1])))
                elif p_step["category"] == "s":
                    new_range = tuple((max(p_step["num"], s[0])+1, s[1]))
                    mini_total += travel(p_step["destination"], x, m, a, new_range)
                    s = tuple((s[0], min(p_step["num"], s[1])))
            else:
                if p_step["category"] == "x":
                    new_range = tuple((x[0], min(p_step["num"], x[1]) - 1))
                    mini_total += travel(p_step["destination"], new_range, m, a, s)
                    x = tuple((max(p_step["num"], x[0]), x[1]))
                elif p_step["category"] == "m":
                    new_range = tuple((m[0], min(p_step["num"], m[1]) - 1))
                    mini_total += travel(p_step["destination"], x, new_range, a, s)
                    m = tuple((max(p_step["num"], m[0]), m[1]))
                elif p_step["category"] == "a":
                    new_range = tuple((a[0], min(p_step["num"], a[1]) - 1))
                    mini_total += travel(p_step["destination"], x, m, new_range, s)
                    a = tuple((max(p_step["num"], a[0]), a[1]))
                elif p_step["category"] == "s":
                    new_range = tuple((s[0], min(p_step["num"], s[1]) - 1))
                    mini_total += travel(p_step["destination"], x, m, a, new_range)
                    s = tuple((max(p_step["num"], s[0]), s[1]))
        else:
            # we are at final dest
            mini_total += travel(p_step["final_dest"], x, m, a, s)


    return mini_total

                    

print(travel("in", tuple((1, 4000)), tuple((1, 4000)), tuple((1, 4000)), tuple((1, 4000))))
