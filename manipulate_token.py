import thorpy as tp



# def print_hello():
#     print("hello world.")

# def before_gui(): #add here the things to do each frame before blitting gui elements
#     screen.fill((250,)*3)

def alert_prison(screen):
    tp.init(screen, tp.theme_human) #bind screen to gui elements and set theme
    alert = tp.Alert("What a pity.\n", "You are in the prison.")
    alert.launch_alone(click_outside_cancel=True) #tune some options if you like
    print("User has chosen:", alert.choice) #here is how to recover user-chosen value

def manipulate_token(a_token, dice_point, screen):
    if a_token.is_arrested is False:
        a_token.location(dice_point)
        # other operations to do
    else:
        alert_prison(screen)
        # tp.call_before_gui(before_gui) #tells thorpy to call before_gui() before drawing gui.
        # other operations to do
