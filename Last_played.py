lastplayed = 6 #get the song id from post request of played_song
Played_list = [1,2,3]
if lastplayed in Played_list:
    exit()
else : 
	Played_list.append(lastplayed)
	if 	len(Played_list) > 3 :
            Played_list.pop(0)

print(Played_list)

print(len(Played_list))
