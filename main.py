from kivy.app import App
from kivy.lang import Builder
from kivy.logger import BOLD_SEQ
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout

Builder.load_file('tela.kv')

class MainMenu(ScreenManager):
       #def __init__(self, **kwargs):    # isso é só para deixar definido o tamanho da tela
        #super().__init__(**kwargs)
        #Window.size = (1366,768)
    pass

class HistoryPage(Screen):

    def __init__(self, **kwargs):    # isso é só para deixar definido o tamanho da tela
        super().__init__(**kwargs)
        Window.size = (1366,768)
    
    def p_main(self):
        self.parent.current = "first"

    class Treasure(BoxLayout):
        pass
    class AddFeat(BoxLayout):
        pass
    class Backstory(BoxLayout):
        pass
    class Allies(BoxLayout):
        pass
    class Organizations(BoxLayout):
        pass

class SpellsPage(Screen):

    def __init__(self, **kwargs):    # isso é só para deixar definido o tamanho da tela
        super().__init__(**kwargs)
        Window.size = (1366,768)
    
    def p_main(self):
        self.parent.current = "first"
    
    class Cantrips(FloatLayout):
        pass
    class Level1(FloatLayout):
        pass
    class Level2(FloatLayout):
        pass
    class Level3(FloatLayout):
        pass
    class Level4(FloatLayout):
        pass 
    class Level5(FloatLayout):
        pass
    class Level6(FloatLayout):
        pass
    class Level7(FloatLayout):
        pass
    class Level8(FloatLayout):
        pass
    class Level9(FloatLayout):
        pass


class FirstPage(Screen):
    def __init__(self, **kwargs):    # isso é só para deixar definido o tamanho da tela
        super().__init__(**kwargs)
        Window.size = (1366,768)

    def p_hist(self):
        self.parent.current = 'history'
    
    def p_spells(self):
        self.parent.current = "spells"
    
    class GoldGrid(FloatLayout):
        pass
    class BagGrid(BoxLayout):
        pass
    class WeaponsGrid(BoxLayout):
        pass
    class SpeedGrid(BoxLayout):
        pass
    class SavingThrowsGrid(BoxLayout):
        pass
    class SkillsGrid(BoxLayout):
        pass
    class SpellsGrid(BoxLayout):
        pass
    class HabilityGrid(BoxLayout):
        pass
    class ProficiencyGrid(BoxLayout):
        pass
    class PassWisGrid(BoxLayout):
        pass
    class IniciativeGrid(BoxLayout):
        pass
    class LifeGrid(BoxLayout):
        pass
    class LevelGrid(BoxLayout):
        pass
    class XpGrid(BoxLayout):
        pass
    class DathSaveGrid(BoxLayout):
        pass
    class OtProfGrid(BoxLayout):
        pass
    class SupAtkGrid(BoxLayout):
        pass
    class NameGrid(BoxLayout):
        pass
    class OrientationGrid(BoxLayout):
        pass
    class RaceGrid(BoxLayout):
        pass
    class ClassGrid(BoxLayout):
        pass
    class InpirationGrid(BoxLayout):
        pass
    class ArmorGrid(BoxLayout):
        pass
    class CharGrid (BoxLayout):
        pass

class TestApp(App):
    def build(self):
        # Create the screen manager
        screenManager = MainMenu()
        return screenManager

if __name__ == '__main__':
    TestApp().run()