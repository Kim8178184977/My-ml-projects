import re
# this module is used to search some specific paterns or this in the string with the help of meta and special sequence
mystr=(r"Street:  Barkat Ali Nagar, Chawl-1, WadalaCity:   MumbaiState/province/area:    MaharashtraPhone number  02224169398Zip code  400037Country calling code  +91Country  IndiaStreet:  Shop No 5, Sukh Aangan, St Road, SoparaCity:   MumbaiState/province/area:    MaharashtraPhone number  02502416874Zip code  401203Country calling code  +91Country  IndiaStreet:  4, Chandrabaug Apartments, Nagvekar Marg, Near Tata Press, PrabhadeviCity:   MumbaiState/province/area:    MaharashtraPhone number  02230426638Zip code  400025Country calling code  +91Country  IndiaStreet:  4,1st Floor, 237/243, Bharat Mkt,barar House, A Rehman Street, MandviCity:   MumbaiState/province/area:    MaharashtraPhone number  02223436013Zip code  400003Country calling code  +91Country  IndiaStreet:  1257,9mn,k.n.extn,trvnird,yespurbl, YeshwantpurCity:   BangaloreState/province/area:    KarnatakaPhone number  23472671Zip code  560022Country calling code  +91Country  IndiaStreet:  Ambedkar Chowk, Rati Villa, Shivaji Path, Gokhale Rd, Ambedkar Chowk, Thane(w)City:   MumbaiState/province/area:    MaharashtraPhone number  02225434433Zip code  400601Country calling code  +91Country  India")
# search_list = re.findall('Street',mystr)# this function finds the word or string then make a string of those words
# print(search_list)
# search = re.search('m',mystr)#this function is the most useful searching a sting inside a string with the help of the meta and special sequence
# print(search)
# print(mystr[52:53])
# split_list = re.split('code',mystr)# this function skips those srting which is given to it and then return a list
# print(split_list)
# replase=re.sub('\s','😎',mystr)#this function replace a string with the given string
# print(replase)
# use of meta sequence
meta=re.compile("^S.*a$")
matches = meta.finditer(mystr)
for match in matches:
    print(match)
#special sequence
special = re.compile('\AStreet')
matches= special.finditer(mystr)
for match in matches:
    print(match)