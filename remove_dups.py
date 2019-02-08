file = "playlists_export.csv"
out_file = "clean_" + "playlists_export.csv"

clean_list = []

with open(file, "r") as file: 
    for line in file:
        clean_list.append(line)

clean_list = set(clean_list)


file = open(out_file,"w+")

for item in clean_list:
    file.write(item)

file.close()