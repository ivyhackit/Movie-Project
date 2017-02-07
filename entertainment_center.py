import media
#importing information from media file
import fresh_tomatoes
#importing information from fresh_tomatoes

eName = "Enough"
eDes = "A brave woman"
ePic = "https://upload.wikimedia.org/wikipedia/en/8/8b/Enoughposter.jpg"
eLink = "https://www.youtube.com/watch?v=j3LVthzm88g"
enough_story = media.Movie(eName, eDes, ePic, eLink)

mName = "Mulan"
mDes = "A brave woman who saves China"
mPic = "https://images-na.ssl-images-amazon.com/images/I/415YeOTGoVL.jpg"
mLink = "https://www.youtube.com/watch?v=MsAniqGowKE"
mulan_story = media.Movie(mName, mDes, mPic, mLink)


iName = "Inception"
iDes = "A movie about implating thoughts in people's mind through dreams"
iPic = "https://images-na.ssl-images-amazon.com/images/I/61Ug%2BK8o5FL.jpg"
iLink = "https://www.youtube.com/watch?v=66TuSJo4dZM"
i_story = media.Movie(iName, iDes, iPic, iLink)


cName = "Catch me if you can"
cDes = "A boy who builds scams as a flight attendent"
cPic = "http://www.impawards.com/2002/posters/catch_me_if_you_can.jpg"
cLink = "https://www.youtube.com/watch?v=hFj3OXVL_wQ"
catch_me_story = media.Movie(cName, cDes, cPic, cLink)

csName = "The Count of Monte Cristo"
csDes = "A simple man who seeks revenge"
csPic = "/home/hackit/Desktop/Move Time/41HhEG3Dz1L.jpg"
csLink = "https://www.youtube.com/watch?v=gzRSVl8UewM"
count_story = media.Movie(csName, csDes, csPic, csLink)

#passing movies into array for fresh_tomatoes 
movies = [enough_story, mulan_story, i_story, catch_me_story, count_story]
fresh_tomatoes.open_movies_page(movies)

