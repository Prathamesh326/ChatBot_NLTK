

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from datetime import datetime



bot = ChatBot('Buddy', storage_adapter='chatterbot.storage.SQLStorageAdapter', database_uri='sqlite:///database.sqlite3')

trainer = ListTrainer(bot)

trainer.train([
'Hi',
    'Hello',

# fees structure

'FE fee structure',
    'Tuition Fee :99380 ',
'Direct SE Fee Structure',
    'Tuition Fee :99380'
'First Year Engineering Admission',
    'DOCUMENTS REQUIRED AT THE TIME OF SECURING ADMISSION TO F.E. AT CAP LEVEL ORIGINAL + ONE SET OF SELF ATTESTED DOCUMENTS ONLY',
'Upcoming Events',
    ' this event is on Day/Month ',
'About us',
    'contact',
    'College@mail',
'Scolarships',
    'Rajarshi Chhatrapati Shahu Maharaj Shikshan Shulkh Shishyavrutti Yojna(EBC)',
'Departments',

    'Computer Engineering|'
    'Computer Science and Engineering (Data Science)|'
    'Information Technology|'
    'Artificial Intelligence and Data Science|'
    'Mechanical Engineering|'
    'Electronics and Telecommunication Engineering|'
    'Civil Engineering|'
    'Instrumentation Engineering|'
    'First Year Engineering|'
,
'Academic calendar',
    'Academic calendar FE 2021-22',
'Teaching Learning Proccess',
    'In today’s time teacher’s role is not limited only to teaching but one has to play the role of mentor, guide, philosopher, friend, guardian and most importantly facilitator. ',
'Research Home',
    'Motivate Faculty members to undergo research projects sponsored by agencies such as AICTE,DST, University of Mumbai , industries etc',
'Patents',
    'Faculty of the department of Computer Engineering',
'Facilities',
    'Library'
    'Gymkhana'
    'Councelling cell',
'Student life at college',
    'Extra-curricular activity',
    'Students councill'
    'Sports committee'
    'Nss'
    ,
'co-curricular activity',
    'IEEE',
'committee',
    'College Devlopment Committee',
    'IQAC'
    'Statutory Committee'
    ,
'Placement',
    'To provide necessary support for implementing the mandate of providing excellent career opportunities for the students.',
'Training',
    'Scheduling of pre-placement training programs in conjunction with academic schedule',
'How are you',
'I am good, Thank you!',
'What is your mobile number',
'You can reach at me on +1(617)-309-6090',
'Can I have your email ID?',
'Sure. Its  ',
'India',
'How dare you?',
'Pardon me ',
'Okay Thanks',
'No Problem! Have a Good Day!'
])


name = input("Enter Your Name: ")

now = datetime.now()
today = now.strftime("%A")
time = now.strftime("%H:%M:%S")

print("Hi, I am Bot!!")
print(f"Today is {today}, current time is {time} ")
print("Let me know how can I help you?")

while True:
    request=input(name+':')
    if request == 'Bye' or request == 'bye':
        print('Bot: Bye')
        break
    else:
        response = bot.get_response(request)
        print('Bot:', response)