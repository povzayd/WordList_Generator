# Word
A Simple Tool To Generate Character Specific Wordlist For Wpa2 Handshake. 
In this code I am using the example of the Airtel routers that are too common around me.For Airtel Routers I have came across till date I have seen only three specific Password patterns. 
1) Airtel_Zerotouch named routers all have the password      'Airtel@123'
2) Airtel_xxxxxxxxxx(where x is there phone no.) 
 there password has 2 specific patterns
  a) airxxxxx  b) air@xxxxx
In this case these x's have nothing to do with there cell phone number's
3) If users change there passwords manually. 
In this case you can't attack with the default credentials  that I mentioned in the above two cases. 




This tool is just for the case number two i.e to generate some character specific word list. 
This tool is completely written in python. 
The Code 
"""
def generate_numbers_with_prefix(prefix, start, end):#f(n) 
"""pass.txt is the file name in which wordlist will be stored you can change it accordingly"""
    with open('pass.txt', 'w') as file: 
        for num in range(start, end + 1):
            formatted_num = f"{prefix}{num:05}"
            file.write(formatted_num + '\n')

generate_numbers_with_prefix("air", 0,99999)

""" Since in this case I generated the wordlist in the form of airxxxxx (where x is some whole number from 0-9) 
the wordlist would start generating as air00001 till air99999. We are getting 5 digits after air due to the code in 4th line {num:05}.If we change it to {num:03} we would get responses like air000 to air999. That means if you want to generate some other character specific wordlist like those used by Tenda Routers aaaaxxxx (where a is any alpha bit and x is any whole number), you can do that too. But keep in mind that this tenda case would lead to the generation of 26*26*26*26*10*10*10*10 possible combinations (456,976,0000) which is huge. So if you are using this tool on your phone so use carefully & first calculate the possible combinations. 
In case of airxxxxx & air@xxxxx the possible combinations are limited to 99999 as it's the last 5 digit number & the prefix is static, that means it will only take some kilobytes from your storage. 
I hope you understand what I was trying to convey & check your calculations twice before generating a wordlist. Otherwise Your Device Might Crash. 