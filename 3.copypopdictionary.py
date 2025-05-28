# copy dictionary

teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"sepseresep",
    "cuy":"surucuy"
}

friends = teman_teman

print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

teman_teman["cup"]="ucup si keren"
print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

# pop dictionary
dataasep = friends.pop("sep")
print(f"data asep = {dataasep}\n")
print(f"friends = {friends}\n")

# popitem dictionary (yang terakhir aja)
dataterakhir = friends.popitem()
print(f"data terakhir = {dataterakhir}\n")
print(f"friends = {friends}\n")
