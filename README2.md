So if you are going to use dlink.py make sure that you have 1 gigs of space available & 
it'll take some time depending on your machine.
That script (dlink.py) will generate numbers from 00000000 to 99999999. This is because 
most dlink routers only use a combination of numbers as there password. 
So just capture a handshake & run this code & give it to aircrack-ng & 
it's done (if you are lucky enough). 
Also this script won't generate a solo big file containing numbers from 00000000 to 99999999
but instead it will generate it in small chunks of millions this means you would get 100 files. 
This is good for old machines & old machine users are advised to take breaks between each million. 
But if you are having a good machine (but not that good ) you can simply write 10 million in places 
of 1 million in the code.          👇
      """with open(f"file{i//1000000}.txt", "w") as file:
            for j in range(i, i + step):
                file.write(str(j) + "\n")
                                     👇
create_txt_files(0, 100000000, 1000000)
"""
