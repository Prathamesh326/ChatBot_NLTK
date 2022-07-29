import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"Fees Structure",
        ["Tution Fees : xxx",]
    ],
    [
        r"which branches can i apply for ?",
        ["This are the courses in our college:"
         "CSE(DS),AIDS,IT,Computer Engineering,Civil,Mech,Extc",]
],
    [
        r"Is there any contact available?",
        ["You can contact us by xyz@gmail.com or 022 xxx xx xx03",]
    ],
    [
        r"Location of the college",
        ["It is near Vasai Road Station.",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","How can I help you?:)",]
    ],
[
        r"Is it a private college or government college?",
        ["It is a Government College.",]
    ],
    [
        r"What is the name of college?",
        ["Vidyavardhini College of Engineering.",]
    ],
    [
        r"How many seats are available for Computer Branch?",
        ["There are 120 seats available for Computer Branch same for IT Mech Extc and Civil,CSE and AI 60.",]
    ],
    [
        r"What are more facilities available inside college?",
        ['There is playground,gymkhana,multiple laboratories with computers available,Seminar halls and much more things.',]
    ],
    [
        r"What functions are organized in college?",
        ['Functions organized are Zeal,Hackathon,sport competitions,Indoor games and much more.']
    ],
     [
        r"What are the extra-curricular activities in the college?",
        ['Students council,Sports Committee,Literati,NSS']
    ],
    [
        r"What are the Co-curricular activities in the college?",
        ['IEE,SAE,CSI,HACKATHON']
    ],
     [
        r"Tell me about the committees available in the collge",
        ['IQAC,College Devlopment Committee,Statutory Committee,Internal Complaint Committee']
    ],
]
def chat():
    print("Hi! I am a chatbot created by Prathamesh Shinde.")
    chat = Chat(pairs, reflections)
    chat.converse()
#initiate the conversation
if __name__ == "__main__":
    chat()