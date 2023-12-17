input = open("input.txt").read().split(',')

total = 0

box_hash = {}

for step in input:
    step_total = 0
    symbol =""
    let = ""
    num = ""
    if "=" in step:
        symbol = "="
        let, num = step.split("=")
    else:
        symbol = "-"
        let, num = step.split("-")

    for c in let:
        step_total += ord(c)
        step_total *= 17
        step_total = step_total % 256

    if symbol == '=':
        val = {"label": let, "foc": num}
        if step_total not in box_hash:
            box_hash[step_total] = [val]
        elif step_total in box_hash:
            if not any(obj["label"] == let for obj in box_hash[step_total]):
                box_hash[step_total].append(val)
            else:
                for i, m in enumerate(box_hash[step_total]):
                    if m["label"] == let:
                        box_hash[step_total][i] = val
    if symbol == '-':
        if step_total in box_hash:
            for i, m in enumerate(box_hash[step_total]):
                if m["label"] == let:
                    del box_hash[step_total][i]

print(box_hash)

for box_num, box_cont in box_hash.items():
    if box_cont:
        for i, slot in enumerate(box_cont):
            total += (int(box_num)+1) * (i+1) * int(slot["foc"])


print(total)

