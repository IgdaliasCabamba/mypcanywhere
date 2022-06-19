import faulthandler
import sys

sys.dont_write_bytecode = True
faulthandler.enable()

from threading import Timer
from ui import *
import core

class Main(App):
    def __init__(self, *args):
        super().__init__(*args, static_file_path={'res':core.routes["res"]})

    def main(self):
        self.registerd_keys = dict()
        self.registerd_pages = dict()

        self.running = True

        my_css_head = """
            <link rel="stylesheet" href="/res:bootstrap-5.1.3-dist/css/bootstrap.min.css"/>
            """
        
        my_js_head = """
            <script src="/res:bootstrap-5.1.3-dist/js/bootstrap.bundle.min.js"></script>
            """
        
        self.page.children['head'].add_child('mycss', my_css_head)
        self.page.children['head'].add_child('myjs', my_js_head)

        self.keyboard_widget = KeyBoard(width='100vw', height='100vh')
        self.mouse_widget = Mouse(width='100vw', height='100vh')
        self.home_widget = Home(width='100vw', height='100vh')
        self.status_widget = Status(width='100vw', height='100vh')
        
        self.menubar = AppMenuBar(width='100%', height='50px')

        self.main_container = gui.Container(width="100%", height = "100%", margin='0px auto', style={'display': 'block'})
        self.main_container.append([self.menubar, self.home_widget, self.status_widget, self.mouse_widget, self.keyboard_widget])
        self.main_container.add_child("footer",
        f"""
        <footer class="bg-light text-center text-lg-start">
        <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2);">
            Using @host:
            <span class="text-dark">{core.get_user_name()}</span>
            <span class="text-dark">{core.get_os()}</span>
            <span class="text-dark">{core.get_processor()}</span>
        </div>
        </footer>
        """)
        
        self.registerd_pages[self.menubar.mouse_page] = self.mouse_widget
        self.registerd_pages[self.menubar.home_page] = self.home_widget
        self.registerd_pages[self.menubar.keyboard_page] = self.keyboard_widget
        self.registerd_pages[self.menubar.status_page] = self.status_widget
        self.registerd_keys[self.keyboard_widget.btn_del] = "del"
        self.registerd_keys[self.keyboard_widget.btn_esc] = "esc"
        self.registerd_keys[self.keyboard_widget.btn_enter] = "enter"
        self.registerd_keys[self.keyboard_widget.btn_up] = "up"
        self.registerd_keys[self.keyboard_widget.btn_down] = "down"
        self.registerd_keys[self.keyboard_widget.btn_left] = "left"
        self.registerd_keys[self.keyboard_widget.btn_right] = "right"
        
        self.bind()
        self.update_app()
        self.update_home_info()
        self.set_page(self.home_widget)

        return self.main_container
    
    def on_close(self):
        self.running = False
        super().on_close()
    
    def update_app(self):
        self.update_status_info()
        if self.running:
            Timer(1, self.update_app).start()
    
    def bind(self):
        self.menubar.mouse_page.onclick.do(self.change_page)
        self.menubar.home_page.onclick.do(self.change_page)
        self.menubar.keyboard_page.onclick.do(self.change_page)
        self.menubar.status_page.onclick.do(self.change_page)
        
        self.home_widget.btn_update_data.onclick.do(self.update_home_info)
        
        self.mouse_widget.mouse_pad.onmousemove.do(self.move_cursor)
        self.mouse_widget.mouse_pad.ontouchmove.do(self.move_cursor)
        
        self.mouse_widget.left_button.onclick.do(core.press_left)
        self.mouse_widget.right_button.onclick.do(core.press_right)
    
        self.keyboard_widget.text_input.onkeyup.do(self.type_key)
        
        self.keyboard_widget.btn_esc.onclick.do(self.press_key)
        self.keyboard_widget.btn_del.onclick.do(self.press_key)
        self.keyboard_widget.btn_enter.onclick.do(self.press_key)
        
        self.keyboard_widget.btn_down.onclick.do(self.press_key)
        self.keyboard_widget.btn_up.onclick.do(self.press_key)
        self.keyboard_widget.btn_down.onclick.do(self.press_key)
        self.keyboard_widget.btn_left.onclick.do(self.press_key)

        self.keyboard_widget.btn_clear.onclick.do(self.clear_input_field)
    
    def press_key(self, obj):
        if obj in self.registerd_keys.keys():
            core.press_key(self.registerd_keys[obj])
    
    def type_key(self, obj, new_value, keycode):
        try:
            last_char = new_value[-1]
        except:pass
        core.type_key(last_char)
    
    def clear_input_field(self, obj):
        self.keyboard_widget.text_input.set_enabled(False)
        self.keyboard_widget.text_input.set_value(" ")
        self.keyboard_widget.text_input.set_enabled(True)
    
    def move_cursor(self, obj, x, y):
        core.move_mouse((int(float(x)),int(float(y))))
    
    def update_status_info(self):
        info = core.get_pc_info()
        self.status_widget.cpu_bar.set_value(int(info["cpu"]))
        self.status_widget.battery_bar.set_value(int(info["battery"].percent))
        self.status_widget.ram_bar.set_value(int(info["memory"].percent))

    def update_home_info(self, obj=None):
        info = core.get_location()
        self.home_widget.info_ip.add_child("data", f'<span class="badge bg-success">{info["ip"]}</span>')
        self.home_widget.info_city.add_child("data", f'<span class="badge bg-success">{info["city"]}</span>')
        self.home_widget.info_country.add_child("data", f'<span class="badge bg-success">{info["country"]}</span>')
        self.home_widget.info_latitude.add_child("data", f'<span class="badge bg-success">{info["latitude"]}</span>')
        self.home_widget.info_longitude.add_child("data", f'<span class="badge bg-success">{info["longitude"]}</span>')
    
    def set_page(self, page):
        for item in self.registerd_pages.values():
            item.style['display'] = 'none'
        page.style['display'] = 'block'
    
    def change_page(self, obj=None):
        if obj in self.registerd_pages.keys():
            widget = self.registerd_pages[obj]
            self.set_page(widget)

if __name__ == "__main__":
    start(Main, address='0.0.0.0', port=9000, start_browser=False, multiple_instance=True, enable_file_cache=False)