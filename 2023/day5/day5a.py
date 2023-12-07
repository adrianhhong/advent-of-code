seeds = [11, 312415190, 1034820096, 106131293, 682397438, 30365957, 2858337556, 1183890307, 665754577, 13162298, 2687187253, 74991378, 1782124901, 3190497, 208902075, 226221606, 4116455504, 87808390, 2403629707, 66592398]
mappings = {}
mapping_names = ("seed_to_soil" , "soil_to_fertilizer" , "fertilizer_to_water" , "water_to_light" , "light_to_temperature" , "temperature_to_humidity" , "humidity_to_location")

destinations = list(map(lambda x: [x], seeds))

for mapping_name in mapping_names:
    mappings[mapping_name] = {"dest_start": [], "source_start": [], "range_length": []}

for mapping_name in mapping_names:
    with open(f'{mapping_name}.txt') as input:
        for line in input:
            mappings[mapping_name]["dest_start"].append(int(line.split()[0]))
            mappings[mapping_name]["source_start"].append(int(line.split()[1]))
            mappings[mapping_name]["range_length"].append(int(line.split()[2]))


for mapping_ind, mapping_name in enumerate(mapping_names):
    for seed_ind, seed in enumerate(destinations):
        found_mapping = False
        # for each mapping starting with seed_to_soil
        for i, mapping_line in enumerate(mappings[mapping_name]["source_start"]):
            # print(destinations)
            if destinations[seed_ind][mapping_ind] >= mapping_line and destinations[seed_ind][mapping_ind] < mapping_line + mappings[mapping_name]["range_length"][i]:
                # bingo we found our mapping
                destinations[seed_ind].append(mappings[mapping_name]["dest_start"][i] + (destinations[seed_ind][mapping_ind] - mapping_line))
                found_mapping = True
            # continue # found our mapping dont need to look anymore
        if not found_mapping:
            destinations[seed_ind].append(destinations[seed_ind][mapping_ind])

        


# print(mappings["seed_to_soil"])
print(destinations)

locations = list(map(lambda x: x[-1], destinations))
print(locations)
print(min(locations))