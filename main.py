# import kivy
import sqlite3
from kivy.app import App
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.screenmanager import ScreenManager,Screen
# from kivy.properties import StringProperty, NumericProperty - Possíveis comandos para identificar variáveis na linguagem kv
Window.clearcolor = get_color_from_hex("#FFFFFF")

class Gerenciador(ScreenManager):
    Window.size = (720,720)
    pass

class Login(Screen):

    def trylogin(self):

        path = r'C:\Users\guiso\OneDrive - Reverse IT\OneDrive\Call With Control\sqlite\teste.db'
        validate = ()
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        usuario = self.ids.usuario.text
        senha = self.ids.senha.text
        cursor.execute("""SELECT * FROM users""")
        for linha in cursor.fetchall():
            if usuario in linha:
                validate = linha
                break
        if validate == ():
            self.ids.validate.text = '[color=ff3333]Usuário não encontrado[/color]'
        else:
            if usuario == validate[1] and senha == validate[2]:
                if validate[4] == 0:
                    self.parent.current = 'home'
                    self.ids.validate.text = str(validate[3])
                else:
                    self.manager.get_screen('home_adm').ids.confirm_end_user.text = str(validate[3])
                    self.parent.current = 'home_adm'
                    self.ids.validate.text = str(validate[3])
            else:
                self.ids.validate.text = '[color=ff3333]Senha inválida[/color]'

    def quit(self):
        janela.stop()

class Home(Screen):

    def trocaenn1l1(self):
        self.manager.get_screen('global').ids.linha.text = 'ENN1 - L1'
        self.parent.current = 'global'

    def trocaenn1l2(self):
        self.manager.get_screen('global').ids.linha.text = 'ENN1 - L2'
        self.parent.current = 'global'

    def trocaenn2tubos(self):
        self.manager.get_screen('global').ids.linha.text = 'ENN2 - TUBOS'
        self.parent.current = 'global'

    def trocaenn2solda(self):
        self.manager.get_screen('global').ids.linha.text = 'ENN2 - SOLDA'
        self.parent.current = 'global'

    def trocaenn3pintura(self):
        self.manager.get_screen('global').ids.linha.text = 'ENN3 - PINTURA'
        self.parent.current = 'global'

    def trocaenn3jato(self):
        self.manager.get_screen('global').ids.linha.text = 'ENN3 - JATO'
        self.parent.current = 'global'

    def trocaenn4daf(self):
        self.manager.get_screen('global').ids.linha.text = 'ENN4 - DAF'
        self.parent.current = 'global'

    def logout(self):
        self.manager.get_screen('login').ids.validate.text = str('')
        self.manager.get_screen('login').ids.senha.text = str('')
        self.parent.current = 'login'

class Global(Screen):

    def puxalinha(self):
        linha = self.ids.linha.text #recebe a linha especificada
        return linha

    def manutencao(self):
        user_name = str(self.manager.get_screen('login').ids.validate.text)
        linha = str(Global.puxalinha(self))
        area = str(self.ids.manutencao.text)
        Global.confirm(self,linha,area,user_name)

    def qualitygate(self):
        user_name = str(self.manager.get_screen('login').ids.validate.text)
        linha = str(Global.puxalinha(self))
        area = str(self.ids.qualitygate.text)
        Global.confirm(self, linha, area,user_name)
        #Global.abrirchamado(self, linha, area, user_name)

    def logistica(self):
        user_name = str(self.manager.get_screen('login').ids.validate.text)
        linha = str(Global.puxalinha(self))
        area = str(self.ids.logistica.text)
        Global.confirm(self, linha, area,user_name)
        #Global.abrirchamado(self, linha, area, user_name)

    def engprocessos(self):
        user_name = str(self.manager.get_screen('login').ids.validate.text)
        linha = str(Global.puxalinha(self))
        area = str(self.ids.engprocessos.text)
        Global.confirm(self, linha, area,user_name)
        #Global.abrirchamado(self, linha, area, user_name)

    def confirm(self,linha,area,usuario):
        self.manager.get_screen('confirm').ids.confirmlinha.text = str(linha)
        self.manager.get_screen('confirm').ids.confirmarea.text = str(area)
        self.manager.get_screen('confirm').ids.confirmuser.text = str(usuario)
        self.parent.current = 'confirm'

class Confirm(Screen):

    def abrirchamado(self):
        from datetime import date
        from datetime import datetime
        path = r'C:\Users\guiso\OneDrive - Reverse IT\OneDrive\Call With Control\sqlite\teste.db'
        cont = []
        hora = str(datetime.now())
        hora = str(hora[11:19])
        data = date.today()
        databr = str(f'{data.day}/{data.month}/{data.year}')
        sqlite_insert_with_param = """INSERT INTO ticket (id, linha, area, data, hora, usuario, status) VALUES (?, ?, ?, ?, ?, ?, ?);"""
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM ticket""")
        for c in cursor.fetchall():
            cont.append(c[0])
        id = len(cont) + 1
        area = str(self.ids.confirmarea.text)
        linha = str(self.ids.confirmlinha.text)
        usuario = str(self.ids.confirmuser.text)
        quant = []  # Possibilidade de puxar apenas o id do bd para ficar mais rápido.
        tupla = (id, linha, area, databr, hora, usuario, 'Aberto')
        try:
            cursor.execute(sqlite_insert_with_param, tupla)
            conn.commit()
        except:
            self.ids.status.text = 'DB ERROR - Contact Support'
        finally:
            cursor.close()
            self.ids.status.text = (f'[color=ff2001]Ticket #{id} registrado com sucesso[/color]')


    def cancelar(self):
        self.ids.status.text = ''
        self.parent.current = 'global'


class Home_Adm(Screen):

    def logout(self):
        self.ids.ticket.text = ''
        self.ids.end_status.text = ''
        self.manager.get_screen('login').ids.validate.text = str('')
        self.manager.get_screen('login').ids.senha.text = str('')
        self.parent.current = 'login'

    def encerrar(self):
        from datetime import date
        from datetime import datetime
        path = r'C:\Users\guiso\OneDrive - Reverse IT\OneDrive\Call With Control\sqlite\teste.db'
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        val = 1
        try:
            ticket = int(self.ids.ticket.text)
        except:
            self.ids.end_status.text = (f'[color=ff2001]Valor inválido[/color]')
            val = 0
        if val == 1:
            db = ()
            for c in cursor.execute("""SELECT * FROM ticket"""):
                if c[0] == ticket:
                    db = c
            if db == ():
                self.ids.end_status.text = (f'[color=ff2001]Ticket ID #{ticket} não foi encontrado[/color]')
            else:
                if db[6] == 'Fechado':
                    self.ids.end_status.text = (f'[color=ff2001]Ticket ID #{ticket} já foi encerrado[/color]')
                else:
                    cursor.execute("""
                    UPDATE ticket
                    SET status = ?
                    WHERE id = ?""", ('Fechado', ticket))
                    conn.commit()
                    hora_agora = str(datetime.now())
                    hora_agora = str(hora_agora[11:19])
                    data_agora = date.today()
                    databr = str(f'{data_agora.day}/{data_agora.month}/{data_agora.year}')
                    sqlite_insert_with_param = """INSERT INTO closed
                     (id, linha, area, data, hora, usuario, data_fechamento, hora_fechamento, status)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"""
                    id = db[0]
                    linha = db[1]
                    area = db[2]
                    data = db[3]
                    hora = db[4]
                    usuario = db[5]
                    data_fechamento = databr
                    hora_fechamento = hora_agora
                    status = 'Fechado'
                    tupla = (id, linha, area, data, hora, usuario, data_fechamento, hora_fechamento, status)
                    try:
                        cursor.execute(sqlite_insert_with_param, tupla)
                        conn.commit()
                    except:
                        self.ids.end_status.text = (f'[color=ff2001]Data Base Error. Contact Support[/color]')
                    finally:
                        self.ids.end_status.text = (f'[color=ff2001]Ticket #{ticket} encerrado com sucesso[/color]')
                        cursor.close()

class ControlApp(App):
    def build(self):
        return Gerenciador()

janela = ControlApp()
janela.run()

