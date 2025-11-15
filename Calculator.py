from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    def add_widgets(self, *widgets):
        for w in widgets:
            self.add_widget(w)

# Special keys can only be C, CE, D and =. All others will be treated as symbols or operands.
buttons = ["C","CE","D","/",
           "1","2","3","*",
           "4","5","6","-",
           "7","8","9","+",
           ".","0","%","="]

font_size = 25

class MyApp(App):
    def build(self):
        self.title = "CalculatorInKivy"
        layout = BoxLayout(orientation='vertical', padding=5)
        LayoutGrid = MyGridLayout(cols=4, size_hint=(1, .75))
        self.label = Label(text="",size_hint=(1, 0.25), font_size=40,valign="center", halign="right", text_size=(.40,.50))
        LayoutGrid.add_widgets(Button(text=str(buttons[0]),font_size=font_size,size_hint=(1/4, 1/5),on_press=self.operant),
                               Button(text=str(buttons[1]),font_size=font_size,size_hint=(1/4, 1/5),on_press=self.operant),
                               Button(text=str(buttons[2]),font_size=font_size,size_hint=(1/4, 1/5),on_press=self.operant),
                               Button(text=str(buttons[3]),font_size=font_size,size_hint=(1/4, 1/5),on_press=self.operant),
                               Button(text=str(buttons[4]),font_size=font_size,size_hint=(1/4, 1/5),on_press=self.operant),
                               Button(text=str(buttons[5]),font_size=font_size,size_hint=(1/4, 1/5),on_press=self.operant),
                               Button(text=str(buttons[6]),font_size=font_size,size_hint=(1/4, 1/5),on_press=self.operant),
                               Button(text=str(buttons[7]),font_size=font_size,size_hint=(1/4, 1/5),on_press=self.operant),
                               Button(text=str(buttons[8]),font_size=font_size,size_hint=(1/4, 1/5),on_press=self.operant),
                               Button(text=str(buttons[9]),font_size=font_size,size_hint=(1/4, 1/5),on_press=self.operant),
                               Button(text=str(buttons[10]),font_size=font_size,size_hint=(1/4, 1/5),on_press=self.operant),
                               Button(text=str(buttons[11]),font_size=font_size,size_hint=(1/4, 1/5),on_press=self.operant),
                               Button(text=str(buttons[12]),font_size=font_size,size_hint=(1/4, 1/5),on_press=self.operant),
                               Button(text=str(buttons[13]),font_size=font_size,size_hint=(1/4, 1/5),on_press=self.operant),
                               Button(text=str(buttons[14]),font_size=font_size,size_hint=(1/4, 1/5),on_press=self.operant),
                               Button(text=str(buttons[15]),font_size=font_size,size_hint=(1/4, 1/5),on_press=self.operant),
                               Button(text=str(buttons[16]),font_size=font_size,size_hint=(1/4, 1/5),on_press=self.operant),
                               Button(text=str(buttons[17]),font_size=font_size,size_hint=(1/4, 1/5),on_press=self.operant),
                               Button(text=str(buttons[18]),font_size=font_size,size_hint=(1/4, 1/5),on_press=self.operant),
                               Button(text=str(buttons[19]),font_size=font_size,size_hint=(1/4, 1/5),on_press=self.operant))

        self.label.bind(size=lambda inst, val: setattr(inst, "text_size", inst.size))
        layout.add_widget(self.label)
        layout.add_widget(LayoutGrid)

        return layout

    def operant(self,instance):
        if instance.text == "D":
            self.label.text = self.label.text[:-1]
        elif instance.text == "=":
            expr = self.label.text.replace(',', '.')
            try:
                self.label.text = str(eval(expr))
            except Exception:
                self.label.text = "Error"
        elif instance.text == "C":
            self.label.text = ""
        elif instance.text == "CE":
            expr = self.label.text
            for sep in ["/", "*", "-", "+"]:
                expr = expr.replace(sep, f" {sep} ")
            parts = expr.split()
            if parts:
                parts.pop()
                self.label.text = "".join(parts)
            else:
                self.label.text = ""
        else:
            self.label.text += instance.text

MyApp().run()