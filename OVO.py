#Check to see if a music artist exists on your iphone

#Music Artist
rapper = 'Drake'
#Songs
drakeSongs = ['Digital Dash','Free Smoke','Fancy','Cameras','Tuscan Leather']

print('Enter the name of a Drake song: ')
songToBeChecked = input()
for song in drakeSongs:
    if song == songToBeChecked:
        print('Now Playing Drake: {}'.format(songToBeChecked))
        break
else:
    print("Song not Available")
