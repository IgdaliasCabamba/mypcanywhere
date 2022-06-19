from typing import Union
import remi.gui as gui
from remi import start, App
from core import XDPI, YDPI

class WidgetController:
    def __init__(self, *args, **kargs):
        pass
    
    def show_widgets(self, widgets_to_show:Union[gui.Widget, list], widgets_to_hide:Union[gui.Widget, list], display:str="block") -> None:
        if isinstance(widgets_to_hide, list):
            for widget_to_hide in widgets_to_hide:
                widget_to_hide.style["display"] = "none"
        else:
            widgets_to_hide.style["display"] = "none"

        if isinstance(widgets_to_show, list):
            for widget_to_show in widgets_to_show:
                widget_to_show.style["display"] = display
        else:
            widgets_to_show.style["display"] = display
        
    def hide_widget(self, widget:gui.Widget):
        widget.style["display"] = "none"
    
    def show_widget(self, widget:gui.Widget, display:str="block"):
        widget.style["display"] = display

class Mouse(gui.VBox, WidgetController):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.init_ui()
    
    def init_ui(self):
        self.hbox_buttons = gui.HBox()
        self.mouse_pad = gui.Button()
        self.mouse_pad.set_size(XDPI, YDPI)
        self.left_button = gui.Button(text="<")        
        self.right_button = gui.Button(text=">")
        
        self.add_class("box-container mouse-container text-center")
        self.hbox_buttons.add_class("horizontal-div")
        self.mouse_pad.add_class("mouse-touch")
        self.left_button.add_class("mouse-button btn btn-primary")
        self.right_button.add_class("mouse-button btn btn-secondary")

        self.hbox_buttons.append([self.left_button, self.right_button])
        self.append([self.mouse_pad, self.hbox_buttons])

class KeyBoard(gui.VBox, WidgetController):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.init_ui()
    
    def init_ui(self):
        self.hbox_keys_group1 = gui.HBox()
        self.hbox_keys_group2 = gui.HBox()

        self.text_input = gui.TextInput()
        
        self.btn_enter = gui.Button(text = "Enter")
        self.btn_del = gui.Button(text = "Delete")
        self.btn_esc = gui.Button(text = "Esc")
        self.btn_clear = gui.Button(text = "CLEAR")

        self.btn_right = gui.Button(text = ">")
        self.btn_left = gui.Button(text = "<")
        self.btn_down = gui.Button(text = "-")
        self.btn_up = gui.Button(text = "+")

        self.hbox_keys_group1.append([self.btn_esc, self.btn_enter, self.btn_del, self.btn_clear])
        self.hbox_keys_group2.append([self.btn_left, self.btn_right, self.btn_up, self.btn_down])

        self.add_class("box-container")
        self.text_input.add_class("form-control")
        self.text_input.add_class("keyboard-input")
        self.text_input.attributes["placeholder"]="Press any key"

        self.btn_esc.add_class("btn btn-secondary")
        self.btn_del.add_class("btn btn-secondary")
        self.btn_enter.add_class("btn btn-primary")
        self.btn_clear.add_class("btn btn-danger")
        self.btn_up.add_class("btn btn-secondary my-1")
        self.btn_down.add_class("btn btn-secondary my-1")
        self.btn_left.add_class("btn btn-secondary my-1")
        self.btn_right.add_class("btn btn-secondary my-1")
        self.hbox_keys_group1.add_class("container")
        self.hbox_keys_group2.add_class("container")


        self.append([self.text_input, self.hbox_keys_group1, self.hbox_keys_group2])

class Status(gui.VBox, WidgetController):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.init_ui()
    
    def init_ui(self):
        self.hbox_ram = gui.HBox()
        self.hbox_battery = gui.HBox()
        self.hbox_cpu = gui.HBox()
        self.hbox_disk = gui.HBox()

        self.ram_desc = gui.Label('RAM', width=50, height=30, margin='10px')
        self.battery_desc = gui.Label('Battery', width=50, height=30, margin='10px')
        self.cpu_desc = gui.Label('CPU', width=50, height=30, margin='10px')
        self.disk_desc = gui.Label('Disk', width=50, height=30, margin='10px')

        self.ram_bar = gui.Progress(1, 100, width=200, height=10)
        self.battery_bar = gui.Progress(1, 100, width=200, height=10)
        self.cpu_bar = gui.Progress(1, 100, width=200, height=10)
        self.disk_bar = gui.Progress(1, 100, width=200, height=10)

        self.ram_bar.add_class("progress-bar bg-info")
        self.battery_bar.add_class("progress-bar bg-info")
        self.cpu_bar.add_class("progress-bar bg-info")
        self.add_class("box-container")

        self.hbox_ram.append([self.ram_desc, self.ram_bar])
        self.hbox_battery.append([self.battery_desc, self.battery_bar])
        self.hbox_cpu.append([self.cpu_desc, self.cpu_bar])
        self.hbox_disk.append([self.disk_desc, self.disk_bar])
        self.append([self.hbox_ram, self.hbox_battery, self.hbox_cpu])

class Home(gui.VBox, WidgetController):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.init_ui()
    
    def init_ui(self):
        self.hbox_buttons = gui.HBox()
        self.vbox_container = gui.VBox()

        self.info_ip = gui.Button(text='Ip Address: ')
        self.info_city = gui.Button(text='City: ')
        self.info_country = gui.Button(text='Country: ')
        self.info_latitude = gui.Button(text='Latitude: ')
        self.info_longitude = gui.Button(text='Longitude: ')

        self.lock_button = gui.Button(text = "Lock")
        self.turn_off_button = gui.Button(text = "Turn Off")
        self.btn_update_data = gui.Button(text = "Update")

        self.info_ip.add_class("btn btn-outline-info my-2")
        self.info_city.add_class("btn btn-outline-info my-2")
        self.info_country.add_class("btn btn-outline-info my-2")
        self.info_latitude.add_class("btn btn-outline-info my-2")
        self.info_longitude.add_class("btn btn-outline-info my-2")

        self.lock_button.add_class("btn btn-secondary mx-2")
        self.turn_off_button.add_class("btn btn-danger mx-2")
        self.btn_update_data.add_class("btn btn-primary")
        self.vbox_container.add_class("container")
        self.hbox_buttons.add_class("container")
        self.add_class("box-container")

        self.hbox_buttons.append([self.lock_button, self.turn_off_button])
        self.vbox_container.append([self.hbox_buttons, self.info_ip, self.info_country, self.info_city, self.info_latitude, self.info_longitude, self.btn_update_data])
        self.append(self.vbox_container)

class AppMenuBar(gui.MenuBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_ui()
    
    def init_ui(self):
        self.menu = gui.Menu(width='100%', height='50px')
        
        self.home_page = gui.MenuItem('Home', width=100, height=30)
        self.mouse_page = gui.MenuItem('Mouse', width=100, height=30)
        self.keyboard_page = gui.MenuItem('KeyBoard', width=100, height=30)
        self.status_page = gui.MenuItem('Status', width=100, height=30)

        self.home_page.add_class("nav-item nav-link")
        self.mouse_page.add_class("nav-item nav-link")
        self.keyboard_page.add_class("nav-item nav-link")
        self.status_page.add_class("nav-item nav-link")
        self.menu.add_class("nav justify-content-center")
        self.add_class("navbar navbar-dark bg-dark")
        
        self.append(self.menu)
        self.menu.append([self.home_page, self.mouse_page, self.keyboard_page, self.status_page])
        