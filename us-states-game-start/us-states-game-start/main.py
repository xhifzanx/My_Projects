import turtle
import pandas
from names_on_maps import Names
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
missing_states = []
filled_states = []
#def get_mouse_click_coor(x, y):
#    print(x, y)
#turtle.onscreenclick(get_mouse_click_coor)

#print(answer_state)

# coordinates of turtle
x = pandas.read_csv("50_states.csv")["x"].to_list()
y = pandas.read_csv("50_states.csv")["y"].to_list()


map_name = Names()



i = 0
data = pandas.read_csv("50_states.csv")
state_names = data["state"].to_list()

def game_over():
    for state in state_names:
        if state not in filled_states:
            missing_states.append(state)

game_on = True
while game_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    for names in state_names:
        if names.lower() == answer_state.lower():
            index_no = state_names.index(names)
            map_name.goto(x=x[index_no], y=y[index_no])
            map_name.write(names)
            filled_states.append(names)
        if i > 49:
            game_on = False
        if answer_state.lower() == "exit":
            game_on = False
            game_over()

missing_data = pandas.DataFrame(missing_states)
missing_in_csv = missing_data.to_csv("missing_states.csv")







turtle.mainloop()