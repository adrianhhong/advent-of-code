import copy

all = open("input.txt").read().split('\n')
instructions = {}
# {a: "%", inv: "&"}
types = {}

for l in all:
    input, output = l.split(" -> ")
    if input[0] in "%&":
        types[input[1::]] = input[0]
        instructions[input[1::]] = output.split(", ")
    else:
        types[input] = None
        instructions[input] = output.split(", ")

module_state = dict.fromkeys(instructions.keys(), "off")
module_most_recent_pulse_sent = dict.fromkeys(instructions.keys(), 0)

step_queue = []
# [lows, highs]
count = [0, 0]

def get_inputs_to_module(module):
    inputs = []
    for k, v in instructions.items():
        if module in v:
            inputs.append(k)
    return inputs

def send_high(old_destination, ordered_new_destinations, new_module_most_recent_pulse_sent):
    count[1] += len(ordered_new_destinations)
    new_module_most_recent_pulse_sent[old_destination] = 1
    return list(map(lambda x: (old_destination, 1, x), ordered_new_destinations))


def send_low(old_destination, ordered_new_destinations, new_module_most_recent_pulse_sent):
    count[0] += len(ordered_new_destinations)
    new_module_most_recent_pulse_sent[old_destination] = 0
    return list(map(lambda x: (old_destination, 0, x), ordered_new_destinations))

            
for press in range(1000):
    step_queue.append(("button", 0, "broadcaster"))
    count[0] += 1
    

    while step_queue:
        new_step = []
        new_module_most_recent_pulse_sent = copy.deepcopy(module_most_recent_pulse_sent)

        for step in step_queue:

            (source, signal, destination) = step

            if destination not in types:
                continue

            new_destinations = instructions[destination]
            
            if destination == "broadcaster":
                # update module_most_recent_pulse_sent
                new_module_most_recent_pulse_sent["broadcaster"] = signal
                # update counts
                count[signal] += len(instructions[destination])
                # update new_step 
                # always update sending to conjunction (&) modules first since it will get ordering correct
                new_step.extend(list(map(lambda x: ("broadcaster", signal, x), new_destinations)))
            else:
                if types[destination] == "%":
                    if signal == 0:
                        if module_state[destination] == "off":
                            new_step.extend(send_high(destination, new_destinations, new_module_most_recent_pulse_sent))
                            module_state[destination] = "on"  
                        else:
                            new_step.extend(send_low(destination, new_destinations, new_module_most_recent_pulse_sent))
                            module_state[destination] = "off"
                elif types[destination] == "&":
                    inputs = get_inputs_to_module(destination)
                    new_module_most_recent_pulse_sent[source] = signal
                    module_most_recent_pulse_sent[source] = signal
                    if any([i for i in inputs if module_most_recent_pulse_sent[i] == 0]): # if any are 0
                        new_step.extend(send_high(destination, new_destinations, new_module_most_recent_pulse_sent))
                    else:
                        new_step.extend(send_low(destination, new_destinations, new_module_most_recent_pulse_sent))
            
        module_most_recent_pulse_sent = new_module_most_recent_pulse_sent
        step_queue = new_step
    

print(count)
print(count[0] * count[1])
