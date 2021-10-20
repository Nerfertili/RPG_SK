from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import sqlite3 as sq
import json

Builder.load_file('tela.kv')

class MainMenu(ScreenManager):
       def __init__(self, **kwargs):    # isso é só para deixar definido o tamanho da tela
            super().__init__(**kwargs)
            Window.size = (1366,768)

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
    edit_pressed =False
    def __init__(self, **kwargs):    # isso é só para deixar definido o tamanho da tela
        super().__init__(**kwargs)
        Window.size = (1366,768)

    def p_hist(self):
        self.parent.current = 'history'
    
    def p_spells(self):
        self.parent.current = "spells"

    def edit(self):
        if self.edit_pressed==False:
            self.i_acrdex = TextInput(pos_hint={'x': (self.ids.acr_dex.pos[0]/1366)-0.02, 'y':self.ids.acr_dex.pos[1]/768 },size_hint=(self.ids.acr_dex.size[0]/1366,self.ids.acr_dex.size[1]/768),font_size=10,multiline=False)
            self.i_aniwis = TextInput(pos_hint={'x': (self.ids.ani_wis.pos[0]/1366)-0.02, 'y':self.ids.ani_wis.pos[1]/768 },size_hint=(self.ids.ani_wis.size[0]/1366,self.ids.ani_wis.size[1]/768),font_size=10,multiline=False)
            self.i_arcint = TextInput(pos_hint={'x': (self.ids.arc_int.pos[0]/1366)-0.02, 'y':self.ids.arc_int.pos[1]/768 },size_hint=(self.ids.arc_int.size[0]/1366,self.ids.arc_int.size[1]/768),font_size=10,multiline=False)
            self.i_athstr = TextInput(pos_hint={'x': (self.ids.ath_str.pos[0]/1366)-0.02, 'y':self.ids.ath_str.pos[1]/768 },size_hint=(self.ids.ath_str.size[0]/1366,self.ids.ath_str.size[1]/768),font_size=10,multiline=False)
            self.i_deccha = TextInput(pos_hint={'x': (self.ids.dec_cha.pos[0]/1366)-0.02, 'y':self.ids.dec_cha.pos[1]/768 },size_hint=(self.ids.dec_cha.size[0]/1366,self.ids.dec_cha.size[1]/768),font_size=10,multiline=False)
            self.i_hisint = TextInput(pos_hint={'x': (self.ids.his_int.pos[0]/1366)-0.02, 'y':self.ids.his_int.pos[1]/768 },size_hint=(self.ids.his_int.size[0]/1366,self.ids.his_int.size[1]/768),font_size=10,multiline=False)
            self.i_inswis = TextInput(pos_hint={'x': (self.ids.ins_wis.pos[0]/1366)-0.02, 'y':self.ids.ins_wis.pos[1]/768 },size_hint=(self.ids.ins_wis.size[0]/1366,self.ids.ins_wis.size[1]/768),font_size=10,multiline=False)
            self.i_intcha = TextInput(pos_hint={'x': (self.ids.int_cha.pos[0]/1366)-0.02, 'y':self.ids.int_cha.pos[1]/768 },size_hint=(self.ids.int_cha.size[0]/1366,self.ids.int_cha.size[1]/768),font_size=10,multiline=False)
            self.i_invint = TextInput(pos_hint={'x': (self.ids.inv_int.pos[0]/1366)-0.02, 'y':self.ids.inv_int.pos[1]/768 },size_hint=(self.ids.inv_int.size[0]/1366,self.ids.inv_int.size[1]/768),font_size=10,multiline=False)
            self.i_medwis = TextInput(pos_hint={'x': (self.ids.med_wis.pos[0]/1366)-0.02, 'y':self.ids.med_wis.pos[1]/768 },size_hint=(self.ids.med_wis.size[0]/1366,self.ids.med_wis.size[1]/768),font_size=10,multiline=False)
            self.i_natint = TextInput(pos_hint={'x': (self.ids.nat_int.pos[0]/1366)-0.02, 'y':self.ids.nat_int.pos[1]/768 },size_hint=(self.ids.nat_int.size[0]/1366,self.ids.nat_int.size[1]/768),font_size=10,multiline=False)
            self.i_perwis = TextInput(pos_hint={'x': (self.ids.per_wis.pos[0]/1366)-0.02, 'y':self.ids.per_wis.pos[1]/768 },size_hint=(self.ids.per_wis.size[0]/1366,self.ids.per_wis.size[1]/768),font_size=10,multiline=False)
            self.i_percha = TextInput(pos_hint={'x': (self.ids.per_cha.pos[0]/1366)-0.02, 'y':self.ids.per_cha.pos[1]/768 },size_hint=(self.ids.per_cha.size[0]/1366,self.ids.per_cha.size[1]/768),font_size=10,multiline=False)
            self.i_perscha = TextInput(pos_hint={'x': (self.ids.pers_cha.pos[0]/1366)-0.02, 'y':self.ids.pers_cha.pos[1]/768 },size_hint=(self.ids.pers_cha.size[0]/1366,self.ids.pers_cha.size[1]/768),font_size=10,multiline=False)
            self.i_relint = TextInput(pos_hint={'x': (self.ids.rel_int.pos[0]/1366)-0.02, 'y':self.ids.rel_int.pos[1]/768 },size_hint=(self.ids.rel_int.size[0]/1366,self.ids.rel_int.size[1]/768),font_size=10,multiline=False)
            self.i_sohdex = TextInput(pos_hint={'x': (self.ids.soh_dex.pos[0]/1366)-0.02, 'y':self.ids.soh_dex.pos[1]/768 },size_hint=(self.ids.soh_dex.size[0]/1366,self.ids.soh_dex.size[1]/768),font_size=10,multiline=False)
            self.i_stedex = TextInput(pos_hint={'x': (self.ids.ste_dex.pos[0]/1366)-0.02, 'y':self.ids.ste_dex.pos[1]/768 },size_hint=(self.ids.ste_dex.size[0]/1366,self.ids.ste_dex.size[1]/768),font_size=10,multiline=False)
            self.i_surwis = TextInput(pos_hint={'x': (self.ids.sur_wis.pos[0]/1366)-0.02, 'y':self.ids.sur_wis.pos[1]/768 },size_hint=(self.ids.sur_wis.size[0]/1366,self.ids.sur_wis.size[1]/768),font_size=10,multiline=False)

            self.i_sstr = TextInput(pos_hint={'x': (self.ids.s_str.pos[0]/1366)-0.02, 'y':self.ids.s_str.pos[1]/768 },size_hint=(self.ids.s_str.size[0]/1366,self.ids.s_str.size[1]/768),font_size=10,multiline=False)
            self.i_sdex = TextInput(pos_hint={'x': (self.ids.s_dex.pos[0]/1366)-0.02, 'y':self.ids.s_dex.pos[1]/768 },size_hint=(self.ids.s_dex.size[0]/1366,self.ids.s_dex.size[1]/768),font_size=10,multiline=False)
            self.i_scon = TextInput(pos_hint={'x': (self.ids.s_con.pos[0]/1366)-0.02, 'y':self.ids.s_con.pos[1]/768 },size_hint=(self.ids.s_con.size[0]/1366,self.ids.s_con.size[1]/768),font_size=10,multiline=False)
            self.i_sint = TextInput(pos_hint={'x': (self.ids.s_int.pos[0]/1366)-0.02, 'y':self.ids.s_int.pos[1]/768 },size_hint=(self.ids.s_int.size[0]/1366,self.ids.s_int.size[1]/768),font_size=10,multiline=False)
            self.i_swis = TextInput(pos_hint={'x': (self.ids.s_wis.pos[0]/1366)-0.02, 'y':self.ids.s_wis.pos[1]/768 },size_hint=(self.ids.s_wis.size[0]/1366,self.ids.s_wis.size[1]/768),font_size=10,multiline=False)
            self.i_scha = TextInput(pos_hint={'x': (self.ids.s_cha.pos[0]/1366)-0.02, 'y':self.ids.s_cha.pos[1]/768 },size_hint=(self.ids.s_cha.size[0]/1366,self.ids.s_cha.size[1]/768),font_size=10,multiline=False)

            self.i_s1 = TextInput(pos_hint={'x': (self.ids.s_1.pos[0]/1366), 'y':self.ids.s_1.pos[1]/768 },size_hint=(self.ids.s_1.size[0]/1366,self.ids.s_1.size[1]/768),font_size=10,multiline=False)
            self.i_s2 = TextInput(pos_hint={'x': (self.ids.s_2.pos[0]/1366), 'y':self.ids.s_2.pos[1]/768 },size_hint=(self.ids.s_2.size[0]/1366,self.ids.s_2.size[1]/768),font_size=10,multiline=False)
            self.i_s3 = TextInput(pos_hint={'x': (self.ids.s_3.pos[0]/1366), 'y':self.ids.s_3.pos[1]/768 },size_hint=(self.ids.s_3.size[0]/1366,self.ids.s_3.size[1]/768),font_size=10,multiline=False)
            self.i_s4 = TextInput(pos_hint={'x': (self.ids.s_4.pos[0]/1366), 'y':self.ids.s_4.pos[1]/768 },size_hint=(self.ids.s_4.size[0]/1366,self.ids.s_4.size[1]/768),font_size=10,multiline=False)
            self.i_s5 = TextInput(pos_hint={'x': (self.ids.s_5.pos[0]/1366), 'y':self.ids.s_5.pos[1]/768 },size_hint=(self.ids.s_5.size[0]/1366,self.ids.s_5.size[1]/768),font_size=10,multiline=False)
            self.i_s6 = TextInput(pos_hint={'x': (self.ids.s_6.pos[0]/1366), 'y':self.ids.s_6.pos[1]/768 },size_hint=(self.ids.s_6.size[0]/1366,self.ids.s_6.size[1]/768),font_size=10,multiline=False)
            self.i_s7 = TextInput(pos_hint={'x': (self.ids.s_7.pos[0]/1366), 'y':self.ids.s_7.pos[1]/768 },size_hint=(self.ids.s_7.size[0]/1366,self.ids.s_7.size[1]/768),font_size=10,multiline=False)

            self.i_f1 = TextInput(pos_hint={'x': (self.ids.f_1.pos[0]/1366), 'y':self.ids.f_1.pos[1]/768 },size_hint=(self.ids.f_1.size[0]/1366,self.ids.f_1.size[1]/768),font_size=10,multiline=False)
            self.i_f2 = TextInput(pos_hint={'x': (self.ids.f_2.pos[0]/1366), 'y':self.ids.f_2.pos[1]/768 },size_hint=(self.ids.f_2.size[0]/1366,self.ids.f_2.size[1]/768),font_size=10,multiline=False)
            self.i_d1 = TextInput(pos_hint={'x': (self.ids.d_1.pos[0]/1366), 'y':self.ids.d_1.pos[1]/768 },size_hint=(self.ids.d_1.size[0]/1366,self.ids.d_1.size[1]/768),font_size=10,multiline=False)
            self.i_d2 = TextInput(pos_hint={'x': (self.ids.d_2.pos[0]/1366), 'y':self.ids.d_2.pos[1]/768 },size_hint=(self.ids.d_2.size[0]/1366,self.ids.d_2.size[1]/768),font_size=10,multiline=False)
            self.i_c1 = TextInput(pos_hint={'x': (self.ids.c_1.pos[0]/1366), 'y':self.ids.c_1.pos[1]/768 },size_hint=(self.ids.c_1.size[0]/1366,self.ids.c_1.size[1]/768),font_size=10,multiline=False)
            self.i_c2 = TextInput(pos_hint={'x': (self.ids.c_2.pos[0]/1366), 'y':self.ids.c_2.pos[1]/768 },size_hint=(self.ids.c_2.size[0]/1366,self.ids.c_2.size[1]/768),font_size=10,multiline=False)
            self.i_i1 = TextInput(pos_hint={'x': (self.ids.i_1.pos[0]/1366), 'y':self.ids.i_1.pos[1]/768 },size_hint=(self.ids.i_1.size[0]/1366,self.ids.i_1.size[1]/768),font_size=10,multiline=False)
            self.i_i2 = TextInput(pos_hint={'x': (self.ids.i_2.pos[0]/1366), 'y':self.ids.i_2.pos[1]/768 },size_hint=(self.ids.i_2.size[0]/1366,self.ids.i_2.size[1]/768),font_size=10,multiline=False)
            self.i_sa1 = TextInput(pos_hint={'x': (self.ids.sa_1.pos[0]/1366), 'y':self.ids.sa_1.pos[1]/768 },size_hint=(self.ids.sa_1.size[0]/1366,self.ids.sa_1.size[1]/768),font_size=10,multiline=False)
            self.i_sa2 = TextInput(pos_hint={'x': (self.ids.sa_2.pos[0]/1366), 'y':self.ids.sa_2.pos[1]/768 },size_hint=(self.ids.sa_2.size[0]/1366,self.ids.sa_2.size[1]/768),font_size=10,multiline=False)
            self.i_ca1 = TextInput(pos_hint={'x': (self.ids.ca_1.pos[0]/1366), 'y':self.ids.ca_1.pos[1]/768 },size_hint=(self.ids.ca_1.size[0]/1366,self.ids.ca_1.size[1]/768),font_size=10,multiline=False)
            self.i_ca2 = TextInput(pos_hint={'x': (self.ids.ca_2.pos[0]/1366), 'y':self.ids.ca_2.pos[1]/768 },size_hint=(self.ids.ca_2.size[0]/1366,self.ids.ca_2.size[1]/768),font_size=10,multiline=False)

            self.i_prof = TextInput(pos_hint={'x': (self.ids.prof.pos[0]/1366), 'y':self.ids.prof.pos[1]/768 },size_hint=(self.ids.prof.size[0]/1366,self.ids.prof.size[1]/768),font_size=15,multiline=False)
            self.add_widget(self.i_prof)

            self.i_pasive_wis = TextInput(pos_hint={'x': (self.ids.pasive_wis.pos[0]/1366), 'y':self.ids.pasive_wis.pos[1]/768 },size_hint=(self.ids.pasive_wis.size[0]/1366,self.ids.pasive_wis.size[1]/768),font_size=15,multiline=False)
            self.add_widget(self.i_pasive_wis)

            self.i_iniciative = TextInput(pos_hint={'x': (self.ids.iniciative.pos[0]/1366), 'y':self.ids.iniciative.pos[1]/768 },size_hint=(self.ids.iniciative.size[0]/1366,self.ids.iniciative.size[1]/768),font_size=15,multiline=False)
            self.add_widget(self.i_iniciative)

            self.i_speed = TextInput(pos_hint={'x': (self.ids.speed.pos[0]/1366), 'y':self.ids.speed.pos[1]/768 },size_hint=(self.ids.speed.size[0]/1366,self.ids.speed.size[1]/768),font_size=15,multiline=False)
            self.add_widget(self.i_speed)

            self.i_level= TextInput(pos_hint={'x': (self.ids.level.pos[0]/1366), 'y':self.ids.level.pos[1]/768 },size_hint=(self.ids.level.size[0]/1366,self.ids.level.size[1]/768),font_size=15,multiline=False)
            self.add_widget(self.i_level)

            self.i_exp= TextInput(pos_hint={'x': (self.ids.exp.pos[0]/1366), 'y':self.ids.exp.pos[1]/768 },size_hint=(self.ids.exp.size[0]/1366,self.ids.exp.size[1]/768),font_size=15,multiline=False)
            self.add_widget(self.i_exp)

            self.i_ot1 = TextInput(pos_hint={'x': (self.ids.ot_1.pos[0]/1366), 'y':self.ids.ot_1.pos[1]/768 },size_hint=(self.ids.ot_1.size[0]/1366,self.ids.ot_1.size[1]/768),font_size=10,multiline=False)
            self.i_ot2 = TextInput(pos_hint={'x': (self.ids.ot_2.pos[0]/1366), 'y':self.ids.ot_2.pos[1]/768 },size_hint=(self.ids.ot_2.size[0]/1366,self.ids.ot_2.size[1]/768),font_size=10,multiline=False)
            self.i_ot3 = TextInput(pos_hint={'x': (self.ids.ot_3.pos[0]/1366), 'y':self.ids.ot_3.pos[1]/768 },size_hint=(self.ids.ot_3.size[0]/1366,self.ids.ot_3.size[1]/768),font_size=10,multiline=False)
            self.i_ot4 = TextInput(pos_hint={'x': (self.ids.ot_4.pos[0]/1366), 'y':self.ids.ot_4.pos[1]/768 },size_hint=(self.ids.ot_4.size[0]/1366,self.ids.ot_4.size[1]/768),font_size=10,multiline=False)
            self.i_ot5 = TextInput(pos_hint={'x': (self.ids.ot_5.pos[0]/1366), 'y':self.ids.ot_5.pos[1]/768 },size_hint=(self.ids.ot_5.size[0]/1366,self.ids.ot_5.size[1]/768),font_size=10,multiline=False)
            self.i_ot6 = TextInput(pos_hint={'x': (self.ids.ot_6.pos[0]/1366), 'y':self.ids.ot_6.pos[1]/768 },size_hint=(self.ids.ot_6.size[0]/1366,self.ids.ot_6.size[1]/768),font_size=10,multiline=False)
            self.i_ot7 = TextInput(pos_hint={'x': (self.ids.ot_7.pos[0]/1366), 'y':self.ids.ot_7.pos[1]/768 },size_hint=(self.ids.ot_7.size[0]/1366,self.ids.ot_7.size[1]/768),font_size=10,multiline=False)

            self.i_orientation= TextInput(pos_hint={'x': (self.ids.orientation.pos[0]/1366), 'y':self.ids.orientation.pos[1]/768 },size_hint=(self.ids.orientation.size[0]/1366,self.ids.orientation.size[1]/768),font_size=15,multiline=False)
            self.add_widget(self.i_orientation)

            self.i_class= TextInput(pos_hint={'x': (self.ids.class_.pos[0]/1366), 'y':self.ids.class_.pos[1]/768 },size_hint=(self.ids.class_.size[0]/1366,self.ids.class_.size[1]/768),font_size=15,multiline=False)
            self.add_widget(self.i_class)

            self.i_inspiration= TextInput(pos_hint={'x': (self.ids.inspiration.pos[0]/1366), 'y':self.ids.inspiration.pos[1]/768 },size_hint=(self.ids.inspiration.size[0]/1366,self.ids.inspiration.size[1]/768),font_size=15,multiline=False)
            self.add_widget(self.i_inspiration)

            self.i_armor2= TextInput(pos_hint={'x': (self.ids.armor2.pos[0]/1366), 'y':self.ids.armor2.pos[1]/768 },size_hint=(self.ids.armor2.size[0]/1366,self.ids.armor2.size[1]/768),font_size=15,multiline=False)
            self.i_armor1= TextInput(pos_hint={'x': (self.ids.armor1.pos[0]/1366), 'y':self.ids.armor1.pos[1]/768 },size_hint=(self.ids.armor1.size[0]/1366,self.ids.armor1.size[1]/768),font_size=15,multiline=False)
            self.add_widget(self.i_armor2)
            self.add_widget(self.i_armor1)

            self.i_wep1 = TextInput(pos_hint={'x': (self.ids.wep1.pos[0]/1366), 'y':self.ids.wep1.pos[1]/768 },size_hint=(self.ids.wep1.size[0]/1366,self.ids.wep1.size[1]/768),font_size=10,multiline=False)
            self.i_wep1bon = TextInput(pos_hint={'x': (self.ids.wep1bon.pos[0]/1366), 'y':self.ids.wep1bon.pos[1]/768 },size_hint=(self.ids.wep1bon.size[0]/1366,self.ids.wep1bon.size[1]/768),font_size=10,multiline=False)
            self.i_wep1dan = TextInput(pos_hint={'x': (self.ids.wep1dan.pos[0]/1366), 'y':self.ids.wep1dan.pos[1]/768 },size_hint=(self.ids.wep1dan.size[0]/1366,self.ids.wep1dan.size[1]/768),font_size=10,multiline=False)
            self.i_wep2 = TextInput(pos_hint={'x': (self.ids.wep2.pos[0]/1366), 'y':self.ids.wep2.pos[1]/768 },size_hint=(self.ids.wep2.size[0]/1366,self.ids.wep2.size[1]/768),font_size=10,multiline=False)
            self.i_wep2bon = TextInput(pos_hint={'x': (self.ids.wep2bon.pos[0]/1366), 'y':self.ids.wep2bon.pos[1]/768 },size_hint=(self.ids.wep2bon.size[0]/1366,self.ids.wep2bon.size[1]/768),font_size=10,multiline=False)
            self.i_wep2dan = TextInput(pos_hint={'x': (self.ids.wep2dan.pos[0]/1366), 'y':self.ids.wep2dan.pos[1]/768 },size_hint=(self.ids.wep2dan.size[0]/1366,self.ids.wep2dan.size[1]/768),font_size=10,multiline=False)
            self.i_wep3= TextInput(pos_hint={'x': (self.ids.wep3.pos[0]/1366), 'y':self.ids.wep3.pos[1]/768 },size_hint=(self.ids.wep3.size[0]/1366,self.ids.wep3.size[1]/768),font_size=10,multiline=False)
            self.i_wep3bon = TextInput(pos_hint={'x': (self.ids.wep3bon.pos[0]/1366), 'y':self.ids.wep3bon.pos[1]/768 },size_hint=(self.ids.wep3bon.size[0]/1366,self.ids.wep3bon.size[1]/768),font_size=10,multiline=False)
            self.i_wep3dan = TextInput(pos_hint={'x': (self.ids.wep3dan.pos[0]/1366), 'y':self.ids.wep3dan.pos[1]/768 },size_hint=(self.ids.wep3dan.size[0]/1366,self.ids.wep3dan.size[1]/768),font_size=10,multiline=False)


            
            self.add_widget(self.i_wep1)
            self.add_widget(self.i_wep1bon)
            self.add_widget(self.i_wep1dan)
            self.add_widget(self.i_wep2)
            self.add_widget(self.i_wep2bon)
            self.add_widget(self.i_wep2dan)
            self.add_widget(self.i_wep3)
            self.add_widget(self.i_wep3bon)
            self.add_widget(self.i_wep3dan)

        
            self.add_widget(self.i_ot1)
            self.add_widget(self.i_ot2)
            self.add_widget(self.i_ot3)
            self.add_widget(self.i_ot4)
            self.add_widget(self.i_ot5)
            self.add_widget(self.i_ot6)
            self.add_widget(self.i_ot7)

            self.add_widget(self.i_f1)
            self.add_widget(self.i_f2)
            self.add_widget(self.i_d1)
            self.add_widget(self.i_d2)
            self.add_widget(self.i_c1)
            self.add_widget(self.i_c2)
            self.add_widget(self.i_i1)
            self.add_widget(self.i_i2)
            self.add_widget(self.i_sa1)
            self.add_widget(self.i_sa2)
            self.add_widget(self.i_ca1)
            self.add_widget(self.i_ca2)

            self.add_widget(self.i_s1)
            self.add_widget(self.i_s2)
            self.add_widget(self.i_s3)
            self.add_widget(self.i_s4)
            self.add_widget(self.i_s5)
            self.add_widget(self.i_s6)
            self.add_widget(self.i_s7)

            self.add_widget(self.i_sstr)
            self.add_widget(self.i_sdex)
            self.add_widget(self.i_scon)
            self.add_widget(self.i_sint)
            self.add_widget(self.i_swis)
            self.add_widget(self.i_scha)

            self.add_widget(self.i_acrdex)
            self.add_widget(self.i_aniwis)
            self.add_widget(self.i_arcint)
            self.add_widget(self.i_athstr)
            self.add_widget(self.i_deccha)
            self.add_widget(self.i_hisint)
            self.add_widget(self.i_inswis)
            self.add_widget(self.i_intcha)
            self.add_widget(self.i_invint)
            self.add_widget(self.i_medwis)
            self.add_widget(self.i_natint)
            self.add_widget(self.i_perwis)
            self.add_widget(self.i_percha)
            self.add_widget(self.i_perscha)
            self.add_widget(self.i_relint)
            self.add_widget(self.i_sohdex)
            self.add_widget(self.i_stedex)
            self.add_widget(self.i_surwis)
            self.edit_pressed = True
    
    def save(self):
        self.remove_widget(self.i_acrdex)
        self.remove_widget(self.i_aniwis)
        self.remove_widget(self.i_arcint)
        self.remove_widget(self.i_athstr)
        self.remove_widget(self.i_deccha)
        self.remove_widget(self.i_hisint)
        self.remove_widget(self.i_inswis)
        self.remove_widget(self.i_intcha)
        self.remove_widget(self.i_invint)
        self.remove_widget(self.i_medwis)
        self.remove_widget(self.i_natint)
        self.remove_widget(self.i_perwis)
        self.remove_widget(self.i_percha)
        self.remove_widget(self.i_perscha)
        self.remove_widget(self.i_relint)
        self.remove_widget(self.i_sohdex)
        self.remove_widget(self.i_stedex)
        self.remove_widget(self.i_surwis)

        self.remove_widget(self.i_sstr)
        self.remove_widget(self.i_sdex)
        self.remove_widget(self.i_scon)
        self.remove_widget(self.i_sint)
        self.remove_widget(self.i_swis)
        self.remove_widget(self.i_scha)

        self.remove_widget(self.i_f1)
        self.remove_widget(self.i_f2)
        self.remove_widget(self.i_d1)
        self.remove_widget(self.i_d2)
        self.remove_widget(self.i_c1)
        self.remove_widget(self.i_c2)
        self.remove_widget(self.i_i1)
        self.remove_widget(self.i_i2)
        self.remove_widget(self.i_sa1)
        self.remove_widget(self.i_sa2)
        self.remove_widget(self.i_ca1)
        self.remove_widget(self.i_ca2)

        self.remove_widget(self.i_s1)
        self.remove_widget(self.i_s2)
        self.remove_widget(self.i_s3)
        self.remove_widget(self.i_s4)
        self.remove_widget(self.i_s5)
        self.remove_widget(self.i_s6)
        self.remove_widget(self.i_s7)

        self.remove_widget(self.i_prof)

        self.remove_widget(self.i_pasive_wis)

        self.remove_widget(self.i_iniciative)

        self.remove_widget(self.i_speed)

        self.remove_widget(self.i_level)

        self.remove_widget(self.i_exp)

        self.remove_widget(self.i_ot1)
        self.remove_widget(self.i_ot2)
        self.remove_widget(self.i_ot3)
        self.remove_widget(self.i_ot4)
        self.remove_widget(self.i_ot5)
        self.remove_widget(self.i_ot6)
        self.remove_widget(self.i_ot7)

        self.remove_widget(self.i_orientation)

        self.remove_widget(self.i_class)

        self.remove_widget(self.i_inspiration)

        self.remove_widget(self.i_armor2)
        self.remove_widget(self.i_armor1)

        self.remove_widget(self.i_wep1)
        self.remove_widget(self.i_wep1bon)
        self.remove_widget(self.i_wep1dan)
        self.remove_widget(self.i_wep2)
        self.remove_widget(self.i_wep2bon)
        self.remove_widget(self.i_wep2dan)
        self.remove_widget(self.i_wep3)
        self.remove_widget(self.i_wep3bon)
        self.remove_widget(self.i_wep3dan)

        self.edit_pressed=False
    def sup_atk(self,text):
        conn = sq.connect('PERSONAGENS.db')
        cursor = conn.cursor()
        print(json.dumps(text))
        cursor.execute('insert into Characters (SupWep) values (?)',(json.dumps(text),))
        conn.commit()
        conn.close()

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