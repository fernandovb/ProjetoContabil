# -*- coding: utf-8 -*-

from _telas.desingner.tpfpes import TPFPES
from _regras.prm.rpfpes import RPFPES


class PFPES(TPFPES):

    def __init__(self, *args, **kwargs):
        super(PFPES, self).__init__(*args, **kwargs)
        self.lista = []
        self.pn_lista.Hide()
        self.pn_dados.Show()

    def ac_localizar(self, event):
        if self.bt_localizar.Label == 'Localizar':
            self.bt_localizar.Label = 'Preencher'
            self.pn_lista.Show()
            self.pn_dados.Hide()
            self.bt_confirmar.Enable(True)
            self.fc_busca()
        else:
            self.bt_localizar.Label = 'Localizar'
            self.bt_confirmar.Enable(False)
            self.pn_lista.Hide()
            self.pn_dados.Show()

    def ac_selecionar(self, event):
        self.pessoa = str(self.gd_resultado.GetCellValue(self.gd_resultado.GetGridCursorRow(), 0))

    def fc_busca(self):
        if self.gd_resultado.GetNumberRows() > 0:
            self.fc_limpa_tabela()
        busca = RPFPES(self.tc_codigo.Value,
                       self.tc_nome_formal.Value,
                       self.tc_nome_alternativo.Value,
                       self.tc_federal.Value)
        dados = busca.fc_buscar()
        if dados is not None:
            line = 0
            for i in dados:
                self.gd_resultado.AppendRows(1)
                self.gd_resultado.SetCellValue(line, 0, str(i[0]))
                self.gd_resultado.SetCellValue(line, 1, str(i[1]))
                self.gd_resultado.SetCellValue(line, 2, str(i[2]))
                self.gd_resultado.SetCellValue(line, 3, str(i[3]))
                line += 1

    def fc_limpa_tabela(self):
        for i in range(self.gd_resultado.GetNumberRows()):
            self.gd_resultado.DeleteRows()
