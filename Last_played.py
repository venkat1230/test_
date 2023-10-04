lastplayed = 6 #got the item from get request
Played_list = [1,2,3]
if lastplayed in Played_list:
    exit()
else : 
	Played_list.append(lastplayed)
	if 	len(Played_list) > 3 :
            Played_list.pop(0)

print(Played_list)

print(len(Played_list))
