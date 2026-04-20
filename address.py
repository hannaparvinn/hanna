import random
import string
fname=['amal','arjun','arun','binu','beena','beema','biju','catherine','diana','deepak','deepu',
       "sera","anu", "manu", "ziya", "ayshaa",'deepa','faizal','fathima','githin','githesh','gireesh','gopu','gopika','hari','hareesh',
       'harshith','hema','hemanth','jaya','jeeva','karthik','keerthi','karthika','kashi','leela',
       'manu','mohan','meenu','meera','noyal','navya','navneeth','nimiya','prakash','preeja','prejul',
       'pramod','roshan','rini','rimisha','rafi','sona','sana','sanu','susan','sanal','thomas','tom',
       'vinu','vimal','vihan','varun','wazeem','ziyad']
lname=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w']
place=['palarivattom','kaloor','edappally','kakkanad','north','south','menaka','fortkochi',
       'vytila','aluva','paravoor','vypin','thevara','kalamasery','thripunithura','thrissur',
       'cherai','vennala','vaduthala','pachalam','angamali','athani','pookkattupady','pallikara',
       'kadamakudy','varapuzha','kadavantha','erroor','thiruvankulam']

for i in range(50):
    first = random.choice(fname)
    last = random.choice(lname)
    fullname = f'{first} {last}'
    print(fullname)

    ph1 = random.randint(60000,99999)
    ph2 = random.randint(10000,99999)
    phone = f'+91 {ph1}-{ph2}'
    print(phone)

    hn = random.randint(1,999)
    loc = random.choice(place)
    address = f'Houseno: {hn} , {loc}\nKochi,kerala'
    print(address)

    n = random.randint(5,255)
    email = f'{first}{last}{n}@gmail.com'
    print(email)

    print('-------------------------------')



