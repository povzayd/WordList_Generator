Generates all possible combinations ranging 
from 'airxxxxx','air@xxxxx','Airxxxxx','Air@xxxxx'
'AIRxxxxx', 'AIR@xxxxx'

You can add your own possible combinations 
by calling the function again & adding your request. 
E.g I want to make a password list that contains
my name followed by numbers from 00000 to 99999
so at the end I'll just add
generate_numbers_with_prefix("zayd", 0,99999)
The output will be 'zayd00000'-'zayd99999'. 
But what if I want the output as zayd123 or zayd5555 or zayd1
for that you would have to change the number at the line 
formatted_num = f"{prefix}{num:0x}"
In place of x what ever number you enter the combinations 
will be formed from that value. For example you enter 3 in 
place of x now the combinations will be zayd000 to zayd999 only. 
For 4 it will be zayd0000 to zayd9999 and so on. 
Check out my other socials. Byyyyyyyyy
            
