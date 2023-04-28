# turtle run 게임
import turtle as t
import random
t.register_shape("가오나시.gif")

# 적 거북이 생성
te = t.Turtle()
te.shape("가오나시.gif")
te.color('red')
te.speed(0)
te.up()
te.goto(0, 200)

# 먹이 생성
tf = t.Turtle()
tf.shape('circle')
tf.color('green')
tf.speed(0)
tf.up()
tf.goto(0, -200)


def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)

def start():
    global playing
    if playing == False:
        playing = True
        t.clear()
        play()

def message(m1, m2):
    t.clear()
    t.goto(0, 100)
    t.write(m1, False, "center", ("", 20))
    t.goto(0, -100)
    t.write(m2, False, "center", ("", 15))
    t.home()

def play():
    global score
    global playing
    # 적 거북이와 닿지 않으면 게임 유지
    # 적 거북이와 닿으면 게임 종료
    if t.distance(te) < 12:
        #t.ontimer(play, 100)  #0.1초간격으로 계속 play 호출
        text = "Score: " + str(score)
        message("Game Over", text)
        playing = False
        score = 0

    t.forward(10)
    te.forward(5)
    # 주인공 거북이가 먹이에 닿으면 점수가 올라감
    if t.distance(tf) < 12:
        score += 1
        t.write(score) # 점수 출력
        start_x = random.randint(-230, 230)
        start_y = random.randint(-230, 230)
        tf.goto(start_x, start_y)

    if playing:
        t.ontimer(play, 100)

    # 적거북이가 주인공 거북이의 위치를 쫒아옴
    # 방향을 알아채는데 약 20% 확률을 적용
    if random.randint(1, 5) == 3:
        ang = te.towards(t.pos())
        te.setheading(ang)

    speed = score + 5
    if speed > 15:
        speed = 15
    te.forward(speed)

    # 주인공 거북이가 먹이에 닿으면 먹이가 새 위치에서 랜덤하게 나타남
    if t.distance(tf) < 12:
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        tf.goto(x, y)


# 주인공 거북이
t.shape('turtle')
t.setup(500, 500) #width, height
t.bgcolor('orange')
t.color('white')
t.speed(0)
t.up()

# 점수와 게임 스위치 변수
score = 0
playing = False

t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(start, 'space')
t.listen()
play()
message("Turtle Run", "[Space]")

t.mainloop()


