def find_common_participants(fg,sg, sep: str = ","):
    fset = set(fg.split(sep))
    sset = set(sg.split(sep))
    both = fset.intersection(sset)
    finlist = list(sorted(both))
    return finlist


participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

print(find_common_participants(participants_first_group, participants_second_group))
