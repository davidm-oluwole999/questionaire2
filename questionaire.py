import pgzrun, random, time

TITLE= "WELCOME TO QUESTIONAIRE!"

WIDTH= 900
HEIGHT= 700

marquee_box= Rect(0,0,WIDTH,80)
question_box= Rect(0,0,710,150)
answer_box1= Rect(0,0,310,150)
answer_box2= Rect(0,0,310,150)
answer_box3= Rect(0,0,310,150)
answer_box4= Rect(0,0,310,150)
timer_box= Rect(0,0,150,150)
skip_box= Rect(0,0,150,300)

score= 0
time_left=10
question_file= "questions.txt"
game_over= False
question= []

marquee_message= ""
questions= []
answer_boxes= [answer_box1 ,answer_box2, answer_box3, answer_box4]
question_count= 0
question_index= 0
marquee_box.move_ip(0, 0)
question_box.move_ip(20,100)
answer_box1.move_ip(20, 270)
answer_box2.move_ip(370, 270)
answer_box3.move_ip(20, 450)
answer_box4.move_ip(370, 450)
timer_box.move_ip(750, 100)
skip_box.move_ip(750, 270)

def draw():
    global marquee_message
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(marquee_box,"black")
    screen.draw.filled_rect(question_box,"yellow")
    screen.draw.filled_rect(timer_box,"orange")
    screen.draw.filled_rect(skip_box,"dark green")  
    for i in answer_boxes:
        screen.draw.filled_rect(i,"light blue")
    marquee_message= TITLE+ f"{question_index} of {question_count}"
    screen.draw.textbox(marquee_message, marquee_box, color= "white")
    screen.draw.textbox(str(time_left), timer_box, color= "white")
    screen.draw.textbox("skip", skip_box, color= "white", angle= 90)
    screen.draw.textbox(question[0].strip(), question_box, color= "white")
    index= 1
    for i in answer_boxes:
        screen.draw.textbox(question[index].strip(), i, color= "white")
        index= index+ 1

def read_next_question():
    global question_index
    question_index= question_index+ 1
    return questions.pop(0).split(",")

def games_over():
    global question, questions, time_left, game_over
    message= f"Game Over \n You got {score} questions correct!"
    question= [message, "-", "-", "-", "-", 5]
    time_left= 0
    game_over= True

def skip_question():
    global question, questions, time_left
    if questions and not game_over:
        question= read_next_question() 
        time_left= 10
    else:
        game_over()

def read_question_file():
    global question_count, questions
    q_file= open(question_file,"r")
    for question in q_file:
        questions.append(question)
        question_count= question_count+ 1
    q_file.close()

def correct_answer():
    global questions, question, time_left, score
    score= score+ 1
    if questions:
        question= read_next_question()
        time_left= 10
    else:
        games_over()

def on_mouse_down(pos):
    index= 1
    for p in answer_boxes:
        if p.collidepoint(pos):
            if index is int(question[5]):
              correct_answer()
            else:
                games_over()
        index += 1
    if skip_box.collidepoint(pos):
        skip_question()
    
def update_time_left():
    global time_left
    if time_left:
        time_left= time_left- 1
    else:
        games_over()

def move_marquee():
    marquee_box.x-= 2
    if marquee_box.right< 0:
        marquee_box.left= WIDTH
    
def update():
    move_marquee()

read_question_file()
question= read_next_question()
clock.schedule_interval(update_time_left, 1)










pgzrun.go()