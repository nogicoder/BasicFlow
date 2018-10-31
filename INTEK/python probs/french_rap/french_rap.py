def french_rap(csv):
    song_list = []
    dic = {}
    try:
        file = open(csv, "r")
        a = file.readline().strip()
        while a != "":
            b = a.split(",")
            dic[b[1]] = []
            song_list.append(b)
            a = file.readline().strip()
        for song in song_list:
            for singer in dic.keys():
                if song[1] == singer:
                    dic[singer].append(song[0])
        return dic
    except FileNotFoundError:
        return 'File does not exist'


print(french_rap("csasdv.csv"))
