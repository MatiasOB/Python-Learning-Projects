
import turtle
import pandas as pd

us_states = pd.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game, Type Exit if you dont remember anymore States and check Forgotten_states.csv")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_states = 0
states_already_choosen = []
playing = True

while playing:

    answer_state = screen.textinput(title=f"Guess the State, Score: {correct_states}/50",
                                    prompt="What's another state name?").title()

    if answer_state not in us_states["state"].tolist() and answer_state != "Exit":
        print("Please choose a valid State")
        continue

    if answer_state not in states_already_choosen and answer_state != "Exit":
        states_already_choosen.append(us_states[us_states["state"] == answer_state]["state"].values.tolist()[0])
        correct_states += 1
        x = us_states[us_states["state"] == answer_state]["x"].values.tolist()[0]
        y = us_states[us_states["state"] == answer_state]["y"].values.tolist()[0]
        pointer = turtle.Turtle()
        pointer.penup()
        pointer.goto(x, y)
        pointer.write(answer_state)
        continue

    elif correct_states == 50:
        print("Congratulations!, you have guessed all the states")
        playing = False
        break
    elif answer_state == "Exit":
        Missing_states = [x for x in us_states["state"].values.tolist() if x not in states_already_choosen]
        forgot = pd.DataFrame(Missing_states,columns=["STATES TO LEARN!"])
        forgot.to_csv("Forgotten_states.csv",index=False)
        playing = False
        break


    else:
        print("You have already chosen that State")
        continue


    turtle.mainloop()

# def get_mouse_click_coor(x,y):
#     print(x , y)

# turtle.onscreenclick(get_mouse_click_coor)
