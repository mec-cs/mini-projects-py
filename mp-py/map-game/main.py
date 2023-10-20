import turtle, pandas, answer, time

wn = turtle.Screen()
wn.setup(width=800, height=600)
wn.title("U.S.A State Game")
wn.bgpic("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
correct_guess = []
remaining_states = []

game_run = True

while game_run:
    answ = wn.textinput(title=f"Guess the state, {len(correct_guess)}/{len(state_list)}", prompt="What's state name:")
    answ = answ.title()

    if answ == "Exit":
        for state in state_list:
            if state not in correct_guess:
                remaining_states.append(state)
        data = pandas.DataFrame(remaining_states)
        data.to_csv("learn_these_states.csv")
        break  # quit game

    # check part
    for state in state_list:
        if answ == state:
            state_word = answer.Answer(answ, int(data.x[data.state == answ]), int(data.y[data.state == answ]))
            correct_guess.append(answ)
    if len(correct_guess) == 50:  # if all states are given then end the game
        game_run = False

    time.sleep(3)

wn.exitonclick()
