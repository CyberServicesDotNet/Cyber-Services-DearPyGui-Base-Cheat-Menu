import win32gui, win32con
from pynput import keyboard
import dearpygui.dearpygui as gui

def set_custom_theme():
      gui.add_theme(tag="base_theme")
      with gui.theme_component(parent="base_theme"):
       gui.add_theme_style(gui.mvStyleVar_WindowRounding, 8)
       gui.add_theme_style(gui.mvStyleVar_ChildRounding, 8)
       gui.add_theme_style(gui.mvStyleVar_FrameRounding, 8)
       gui.add_theme_style(gui.mvStyleVar_GrabRounding, 8)
       gui.add_theme_style(gui.mvStyleVar_TabRounding, 7)
       gui.add_theme_style(gui.mvStyleVar_ScrollbarSize, 10)
       
       gui.add_theme_color(gui.mvThemeCol_WindowBg, (0, 0, 0))
       gui.add_theme_color(gui.mvThemeCol_Text, (255, 255, 255))
       gui.add_theme_color(gui.mvThemeCol_TitleBgActive, (75, 0, 130))

       gui.add_theme_color(gui.mvThemeCol_FrameBg, (0, 0, 0))
       gui.add_theme_color(gui.mvThemeCol_FrameBgHovered, (30, 30, 30))
       gui.add_theme_color(gui.mvThemeCol_FrameBgActive, (0, 0, 0))

       gui.add_theme_color(gui.mvThemeCol_Header, (0, 0, 0))
       gui.add_theme_color(gui.mvThemeCol_HeaderActive, (75, 0, 130)) 
       gui.add_theme_color(gui.mvThemeCol_HeaderHovered, (15, 15, 15))

       gui.add_theme_color(gui.mvThemeCol_Tab, (15, 15, 15))
       gui.add_theme_color(gui.mvThemeCol_TabActive, (75, 0, 130))
       gui.add_theme_color(gui.mvThemeCol_TabHovered, (0, 0, 0))

       gui.add_theme_color(gui.mvCheckbox, (75, 0, 130))
       gui.add_theme_color(gui.mvThemeCol_CheckMark, (75, 0, 130))

       gui.add_theme_color(gui.mvThemeCol_Button, (0, 0, 0))
       gui.add_theme_color(gui.mvThemeCol_ButtonActive, (15, 15, 15))
       gui.add_theme_color(gui.mvThemeCol_ButtonHovered, (75, 0, 130))

       gui.add_theme_color(gui.mvThemeCol_SliderGrab, (75, 0, 130))
       gui.add_theme_color(gui.mvThemeCol_SliderGrabActive, (75, 0, 130))

       gui.add_theme_color(gui.mvThemeCol_ChildBg, (10, 10, 10))

gui.create_context()
set_custom_theme()
gui.setup_dearpygui()

hidden = False
width, height, channels, data = gui.load_image(file="CyberServices.png")
viewport = gui.create_viewport(title="Cyber Services DearPyGui Base Cheat Menu", width=400, height=400, decorated=False, resizable=False)

def exit():
  gui.destroy_context()

def cal_down(sender, data): #credits: https://www.unknowncheats.me/forum/valorant/600025-dearpygui-frameless-window.html
   global title_bar_drag
   if gui.is_mouse_button_down(0):
      x = data[0]
      y = data[1]
      if -2 <= y <=19:
       title_bar_drag = True
      else:
        title_bar_drag = False

def cal(sender, data): #credits: https://www.unknowncheats.me/forum/valorant/600025-dearpygui-frameless-window.html
   global title_bar_drag
   if title_bar_drag: #remove this line if you'd like to drag from anywhere on the gui.
    pos = gui.get_viewport_pos()
    x = data[1]
    y = data[2]
    final_x = pos[0] + x
    final_y = pos[1] + y
    gui.configure_viewport(viewport, x_pos=final_x, y_pos=final_y)

def KeyPress(key):
  global hidden 
  if hidden == False :
    if key == keyboard.Key.insert:
     hidden = True
     window = win32gui.GetForegroundWindow()
     win32gui.SetForegroundWindow(window)
     win32gui.ShowWindow(window, win32con.SW_HIDE)
  else:
    if hidden == True:
     if key == keyboard.Key.insert:
      hidden = False
      window = win32gui.GetForegroundWindow()
      win32gui.SetForegroundWindow(window)
      win32gui.ShowWindow(window, win32con.SW_SHOW)
  if key == keyboard.Key.delete:
    exit()

listener = keyboard.Listener(on_press=KeyPress)
listener.start()


with gui.texture_registry(show=True):
       gui.add_static_texture(width=width, height=height, default_value=data, tag="base_texture_tag")

with gui.window(label="Cyber Services DearPyGui Base Cheat Menu", height=400, width=400, no_collapse=True, no_close=True, no_move=True, no_resize=True, on_close=exit):  
    with gui.tab_bar():
     with gui.tab(label="Tab 1"):
       gui.add_text("Window 1")
       with gui.child_window(label="Child Window"): 
         gui.add_checkbox(label="CheckBox1")
         gui.add_checkbox(label="CheckBox2")
         gui.add_checkbox(label="CheckBox3")
         gui.add_separator()
         gui.add_button(label="Button1")
         gui.add_button(label="Button2")
         gui.add_button(label="Button3")
         gui.add_separator()
         gui.add_slider_int(label="Slider1 (Int)", default_value=20, min_value=1, max_value=100)
         gui.add_slider_float(label="Slider2 (Float)", default_value=20.000, min_value=1.000, max_value=100.000)

     items = ["Item1", "Item2", "Item3"]
     with gui.tab(label="Tab 2"):
      gui.add_text("Window 2")
      with gui.child_window(label="Child Window"): 
       gui.add_checkbox(label="CheckBox")
       gui.add_checkbox(label="CheckBox")
       gui.add_checkbox(label="CheckBox")
       gui.add_separator()
       gui.add_selectable(label="Select1")
       gui.add_selectable(label="Select2")
       gui.add_selectable(label="Select3")
       gui.add_separator()
       gui.add_combo(label="Combo",items=items)

     with gui.tab(label="Tab 3"):
       gui.add_text("Window 3")
       with gui.child_window(label="Child Window"): 
        gui.add_color_picker()

     with gui.tab(label="Tab 4"):
       gui.add_text("Window 4")
       with gui.child_window(label="Child Window"):
        gui.add_text("Join our discord server if you have any questions!\nhttps://discord.gg/32vRvTtD3W")
        gui.add_image(texture_tag="base_texture_tag")

    with gui.handler_registry():
       gui.add_mouse_drag_handler(0, callback=cal)
       gui.add_mouse_move_handler(callback=cal_down)

    gui.bind_theme("base_theme")
    gui.show_viewport()
    gui.start_dearpygui()
    gui.destroy_context()
