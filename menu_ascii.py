import sys
from datetime import date
import wxPython

from asciimatics.widgets import Layout, Frame, Label, Button, Divider
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, StopApplication, NextScene
import dados.conexao as conexao
import telas.cad_pessoas as cad_pessoas

class TelaPrincipal(Frame):

    def __init__(self, screen, conn):
        super(TelaPrincipal, self).__init__(screen,
                                            int(screen.height - 2),
                                            int(screen.width - 4),
                                            title='Menu Principal')
        self.conn = conn
        # Formata data atual para exibição
        data_atual = str('Data: {}/{}/{}'.format(date.today().day, date.today().month, date.today().year))
        # Cria layout para mostrar cabeçalho
        lay_cabecalho = Layout([80, 20])
        self.add_layout(lay_cabecalho)
        lay_cabecalho.add_widget(Label('ERP Caseiro - Menu Principal'), 0)
        lay_cabecalho.add_widget(Label(data_atual), 1)
        lay_cabecalho.add_widget(Label(self.conn.mensagem), 0)
        # Cria layout para dividir cabeçalho do corpo
        lay_divider_1 = Layout([100])
        self.add_layout(lay_divider_1)
        lay_divider_1.add_widget(Divider())
        # Cria layout do corpo do menu
        lay_corpo = Layout([25, 25, 25, 25])
        self.add_layout(lay_corpo)
        lay_corpo.add_widget(Button('Cadastro', on_click=self._mcadastro), 0)
        lay_corpo.add_widget(Button('Sair', on_click=self._sair), 3)
        self.fix()

    def _sair(self):
        self.conn._fechar()
        raise StopApplication('Sistema encerrado')

    def _mcadastro(self):
        raise NextScene('mcadastro')


class TelaCadastro(Frame):

    def __init__(self, screen):
        super(TelaCadastro, self).__init__(screen,
                                           int(screen.height - 2),
                                           int(screen.width - 4),
                                           title='Cadastros')
        # Formata data atual para exibição
        data_atual = str('Data: {}/{}/{}'.format(date.today().day, date.today().month, date.today().year))
        # Cria layout para mostrar cabeçalho
        lay_cabecalho = Layout([80, 20])
        self.add_layout(lay_cabecalho)
        lay_cabecalho.add_widget(Label('ERP Caseiro - Cadastros'), 0)
        lay_cabecalho.add_widget(Label(data_atual), 1)
        lay_cabecalho.add_widget(Label(''), 0)
        # Cria layout para dividir cabeçalho do corpo
        lay_divider_1 = Layout([100])
        self.add_layout(lay_divider_1)
        lay_divider_1.add_widget(Divider())
        # Cria layout do corpo do menu
        lay_corpo = Layout([25, 25, 25, 25])
        self.add_layout(lay_corpo)
        lay_corpo.add_widget(Button('Pessoas', on_click=self._cad_pessoas), 0)
        lay_corpo.add_widget(Button('Voltar', on_click=self._retorna), 3)
        self.fix()

    def _cad_pessoas(self):
        raise NextScene('cad_pessoas')

    def _retorna(self):
        raise NextScene('menu')



def sistema(screen, scene):
    # Cria cenário com tela principal
    scenes = [Scene([TelaPrincipal(screen, conn)], -1, name='menu')]
    # Adiciona demais telas do sistema
    scenes.append(Scene([TelaCadastro(screen)], -1, name='mcadastro'))
    scenes.append(Scene([cad_pessoas.CadPessoas(screen)], -1, name='cad_pessoas'))
    screen.play(scenes, stop_on_resize=True, start_scene=scene)


conn = conexao.Dados()
last_scene = None
while True:
    try:
        Screen.wrapper(sistema, catch_interrupt=False, arguments=[last_scene])
        print('*' * 30)
        print('**    Sistema encerrado!    **')
        print('*' * 30)
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene

