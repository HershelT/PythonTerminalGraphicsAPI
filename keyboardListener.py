from pynput import keyboard

import sys
# Define a key listener
class MyKeyListener:
    def __init__(self, key_actions={}):
        self.keys_pressed = set()
        self.key_actions = key_actions
        self.user_input= None
    def on_press(self, key):
        self.keys_pressed.add(str(key))

    def on_release(self, key):
        self.keys_pressed.discard(str(key))

    def is_pressed(self, key):
        return str(key) in self.keys_pressed

    # define what keys can be pressed
    #do the entire alphabet from a-z
    def is_a_pressed(self):
        return "'a'" in self.keys_pressed
    def is_b_pressed(self):
        return "'b'" in self.keys_pressed
    def is_c_pressed(self):
        return "'c'" in self.keys_pressed
    def is_d_pressed(self):
        return "'d'" in self.keys_pressed
    def is_e_pressed(self):
        return "'e'" in self.keys_pressed
    def is_f_pressed(self):
        return "'f'" in self.keys_pressed
    def is_g_pressed(self):
        return "'g'" in self.keys_pressed
    def is_h_pressed(self):
        return "'h'" in self.keys_pressed
    def is_i_pressed(self): 
        return "'i'" in self.keys_pressed
    def is_j_pressed(self):
        return "'j'" in self.keys_pressed
    def is_k_pressed(self):
        return "'k'" in self.keys_pressed
    def is_l_pressed(self):
        return "'l'" in self.keys_pressed
    def is_m_pressed(self):
        return "'m'" in self.keys_pressed
    def is_n_pressed(self):
        return "'n'" in self.keys_pressed
    def is_o_pressed(self):
        return "'o'" in self.keys_pressed
    def is_p_pressed(self):
        return "'p'" in self.keys_pressed
    def is_q_pressed(self):
        return "'q'" in self.keys_pressed
    def is_r_pressed(self):
        return "'r'" in self.keys_pressed
    def is_s_pressed(self):
        return "'s'" in self.keys_pressed
    def is_t_pressed(self):
        return "'t'" in self.keys_pressed
    def is_u_pressed(self):
        return "'u'" in self.keys_pressed
    def is_v_pressed(self):
        return "'v'" in self.keys_pressed
    def is_w_pressed(self):
        return "'w'" in self.keys_pressed
    def is_x_pressed(self):
        return "'x'" in self.keys_pressed
    def is_y_pressed(self):
        return "'y'" in self.keys_pressed
    def is_z_pressed(self):
        return "'z'" in self.keys_pressed
    
    #do the numbers from 0-9
    def is_0_pressed(self):
        return "'0'" in self.keys_pressed
    def is_1_pressed(self):
        return "'1'" in self.keys_pressed
    def is_2_pressed(self):
        return "'2'" in self.keys_pressed
    def is_3_pressed(self):
        return "'3'" in self.keys_pressed
    def is_4_pressed(self):
        return "'4'" in self.keys_pressed
    def is_5_pressed(self):
        return "'5'" in self.keys_pressed
    def is_6_pressed(self):
        return "'6'" in self.keys_pressed
    def is_7_pressed(self):
        return "'7'" in self.keys_pressed
    def is_8_pressed(self):
        return "'8'" in self.keys_pressed
    def is_9_pressed(self):
        return "'9'" in self.keys_pressed
    
    
    
    #Non keyboard charcters like enter 
    def is_left_arrow_pressed(self):
        return "Key.left" in self.keys_pressed
    def is_right_arrow_pressed(self):
        return "Key.right" in self.keys_pressed
    def is_up_arrow_pressed(self):
        return "Key.up" in self.keys_pressed
    def is_down_arrow_pressed(self):
        return "Key.down" in self.keys_pressed
    def is_backspace_pressed(self):
        return "Key.backspace" in self.keys_pressed
    def is_enter_pressed(self):
        return "Key.enter" in self.keys_pressed
    def is_tab_pressed(self):
        return "Key.tab" in self.keys_pressed
    def is_space_pressed(self):
        return "Key.space" in self.keys_pressed
    def is_esc_pressed(self):
        if "Key.esc" in self.keys_pressed:
            print("You have exited the program")
            sys.stdout.write("\033[?25h" + "\033[0m")
            sys.exit()
    
    
    def check_keys(self):
        for key in list(self.keys_pressed):  # Create a copy of self.keys_pressed
            if key in self.key_actions:
                self.key_actions[key]()
        self.is_esc_pressed()

# Key_Listener = MyKeyListener()
# Listener = keyboard.Listener(
#     on_press=Key_Listener.on_press,
#     on_release=Key_Listener.on_release)

# #Use to call the key listener set something equal to it to get the keyboard
# def startKeyboard():
#     Key_Listener = MyKeyListener()
#     Listener = keyboard.Listener(
#         on_press=Key_Listener.on_press,
#         on_release=Key_Listener.on_release)
#     Listener.start()
#     # Key_Listener = MyKeyListener()
#     # Listener = keyboard.Listener(
#     #     on_press=Key_Listener.on_press,
#     #     on_release=Key_Listener.on_release)
#     # Listener.start()
#     # return [key_listener, listener]

# #Stops the current keybard 
# def stopKeyboard():
#     Listener.stop()
#     # del Listener

# startKeyboard()
#example
# if Key_Listener.is_1_pressed():
#     print("1")

#when getting keyboard input type in:
    # key_listener = MyKeyListener()
    #         listener = keyboard.Listener(
    #             on_press=key_listener.on_press,
    #             on_release=key_listener.on_release)