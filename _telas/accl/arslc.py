# -*- coding: utf-8 -*-

import wx
from datetime import datetime
from _telas.desingner.tarslc import TARSLC
from _telas.accl.afcon import AFCON
import _regras.sys.ssglob as ssglob
from _regras.accl.rarslc import RARSLC, RARSLD


class ARSLC(TARSLC):
    acao = 0  # 0-Consultar, 1-Inlcuir, 2-Extornar

    def __init__(self, *args, **kwargs):
        super(ARSLC, self).__init__(*args, **kwargs)
        self.partidas = []
        self.condicao = 'irregular'
        self.tc_condicao.Value = self.condicao.upper()
        self.tb_slip.EnableTool(wx.ID_ADD, True)
        self.tb_slip.EnableTool(wx.ID_FIND, True)
        self.tb_slip.EnableTool(wx.ID_DELETE, False)
        self.tb_slip.EnableTool(wx.ID_SAVE, False)
        self.tb_slip.EnableTool(wx.ID_CANCEL, False)

    def ac_reg_adicionar(self, event):
        agora = datetime.today()
        self.acao = 0
        self.fc_desativa_campos_cabecalho()
        self.tc_dt_criacao.Value = agora.strftime('%Y-%m-%d')
        self.tc_dt_movimento.Value = agora.strftime('%Y-%m-%d')
        self.tc_empresa.Value = str(ssglob.SSGLOB.empresa)
        self.tc_periodo.Value = str(ssglob.SSGLOB.periodo)
        self.tc_exercicio.Value = str(ssglob.SSGLOB.exercicio)
        self.tc_usuario.Value = str(ssglob.SSGLOB.matricula)
        self.bt_part_adicionar.Enable(True)
        self.tb_slip.EnableTool(wx.ID_ADD, False)
        self.tb_slip.EnableTool(wx.ID_FIND, False)
        self.tb_slip.EnableTool(wx.ID_DELETE, False)
        self.tb_slip.EnableTool(wx.ID_SAVE, True)
        self.tb_slip.EnableTool(wx.ID_CANCEL, True)

    def ac_reg_consultar(self, event):
        self.acao = 1
        pass

    def ac_reg_estornar(self, event):
        self.acao = 2
        pass

    def ac_confirmar(self, event):
        if self.condicao == 'equalizado':
            confirma = RARSLC(acao=self.acao)
            confirma.partidas = self.partidas
            confirma.ac_gravar()
            if confirma.num_documento == 0:
                self.sb_slip.SetStatusText('Erro ao gravar o lançamento. Entre em contato com o administrador', 0)
            else:
                self.tc_num_documento.Value = str(confirma.num_documento)
                self.fc_desativa_campos_cabecalho()
                self.fc_part_desativa_campos()
                self.fc_part_desativa_botoes()
                self.tb_slip.EnableTool(wx.ID_ADD, True)
                self.tb_slip.EnableTool(wx.ID_FIND, True)
                self.tb_slip.EnableTool(wx.ID_DELETE, False)
                self.tb_slip.EnableTool(wx.ID_SAVE, False)
                self.tb_slip.EnableTool(wx.ID_CANCEL, False)
                self.sb_slip.SetStatusText(f'Registro {confirma.num_documento} gravado com sucesso!', 0)
        else:
            self.sb_slip.SetStatusText('Partidas não estão equalizadas!', 0)

    def ac_reg_cancelar(self, event):
        pass

    # Métodos de consulta para localização de informações

    def ac_cons_unidade(self, event):
        pass

    def ac_cons_conta(self, event):
        consulta = AFCON(self)
        if consulta.ShowModal() == wx.ID_OK:
            self.tc_conta_contabil.Value = str(
                consulta.gd_resultado.GetCellValue(consulta.gd_resultado.GetGridCursorRow(), 0))
        consulta.Destroy()

    def ac_cons_clucro(self, event):
        pass

    def fc_ativa_campos_cabecalho(self):
        self.tc_empresa.Enable(True)
        self.tc_num_documento.Enable(True)

    def fc_desativa_campos_cabecalho(self):
        self.tc_empresa.Enable(False)
        self.tc_num_documento.Enable(False)

    def fc_condicao(self):
        total = 0.00
        if len(self.partidas) > 0:
            for partida in self.partidas:
                total = total + partida.montante
            if total == 0.00:
                self.condicao = 'equalizado'
            else:
                self.condicao = 'irregular'
        else:
            self.condicao = 'irregular'
        self.tc_condicao.Value = self.condicao.upper()

    # Controles das partidas

    def ac_part_adicionar(self, event):
        self.fc_part_desativa_botoes()
        sequencia = 0
        if len(self.partidas) > 0:
            registros = []
            for partida in self.partidas:
                registros.append(partida.registro)
            sequencia = max(registros)
        self.tc_registro.Value = str(sequencia + 1)
        self.tc_situacao.Value = '0'
        self.tc_tipo_registro.Value = 'LM'
        self.tc_moeda.Value = 'BRL'
        self.pn_partidas.Hide()
        self.pn_detalhes.Show()
        self.fc_part_ativa_campos()

    def ac_part_consultar(self, event):
        self.fc_part_desativa_botoes()
        partida = self.partidas[self.gd_partidas.GetGridCursorRow()]
        self.tc_registro.Value = str(partida.registro)
        self.tc_situacao.Value = str(partida.situacao)
        self.tc_tipo_registro.Value = str(partida.tipo_registro)
        self.tc_unidade.Value = str(partida.unidade)
        self.cb_chave_registro.Value = str(partida.chave_registro)
        self.tc_conta_contabil.Value = str(partida.conta_contabil)
        self.tc_centro_lucro.Value = str(partida.centro_lucro)
        self.tc_descricao.Value = str(partida.descricao)
        self.tc_doc_referencia.Value = str(partida.doc_referencia)
        self.tc_doc_compensacao.Value = str(partida.doc_compensacao)
        self.tc_montante.Value = str(partida.montante)
        self.tc_moeda.Value = str(partida.moeda)
        self.pn_partidas.Hide()
        self.pn_detalhes.Show()

    def ac_part_cancelar(self, event):
        self.fc_part_ativa_botoes()
        self.pn_partidas.Show()
        self.pn_detalhes.Hide()
        self.fc_part_desativa_campos()
        self.fc_part_limpa_campos()

    def ac_part_confirmar(self, event):
        try:
            partida = RARSLD(registro=self.tc_registro.Value,
                             situacao=int(self.tc_situacao.Value),
                             tipo_registro=self.tc_tipo_registro.Value,
                             unidade=int(self.tc_unidade.Value),
                             chave_registro=str(self.cb_chave_registro.Value).upper(),
                             conta_contabil=self.tc_conta_contabil.Value,
                             centro_lucro=self.tc_centro_lucro.Value,
                             descricao=self.tc_descricao.Value,
                             doc_referencia=self.tc_doc_referencia.Value,
                             doc_compensacao=self.tc_doc_compensacao.Value,
                             montante=float(self.tc_montante.Value),
                             moeda=self.tc_moeda.Value)
            self.partidas.append(partida)
            self.fc_atualiza_grade()
            self.fc_part_ativa_botoes()
            self.pn_partidas.Show()
            self.pn_detalhes.Hide()
            self.fc_part_limpa_campos()
            self.fc_part_desativa_campos()
        except:
            self.sb_slip.SetStatusText('Falta preechimento de campos obrigatórios.', 0)

    def ac_part_excluir(self, event):
        partida = self.partidas[self.gd_partidas.GetGridCursorRow()]
        self.partidas.remove(partida)
        self.fc_atualiza_grade()
        self.sb_slip.SetStatusText('', 0)

    def fc_part_limpa_campos(self):
        self.tc_registro.Value = ''
        self.tc_situacao.Value = ''
        self.tc_tipo_registro.Value = ''
        self.tc_unidade.Value = ''
        self.cb_chave_registro.Value = ''
        self.tc_conta_contabil.Value = ''
        self.tc_centro_lucro.Value = ''
        self.tc_descricao.Value = ''
        self.tc_doc_referencia.Value = ''
        self.tc_doc_compensacao.Value = ''
        self.tc_montante.Value = ''
        self.tc_moeda.Value = ''
        self.sb_slip.SetStatusText('', 0)

    def fc_part_ativa_campos(self):
        self.tc_registro.Enable(True)
        self.tc_situacao.Enable(True)
        self.tc_tipo_registro.Enable(True)
        self.tc_unidade.Enable(True)
        self.cb_chave_registro.Enable(True)
        self.tc_conta_contabil.Enable(True)
        self.tc_centro_lucro.Enable(True)
        self.tc_descricao.Enable(True)
        self.tc_doc_referencia.Enable(True)
        self.tc_doc_compensacao.Enable(True)
        self.tc_montante.Enable(True)
        self.tc_moeda.Enable(True)

    def fc_part_desativa_campos(self):
        self.tc_registro.Enable(False)
        self.tc_situacao.Enable(False)
        self.tc_tipo_registro.Enable(False)
        self.tc_unidade.Enable(False)
        self.cb_chave_registro.Enable(False)
        self.tc_conta_contabil.Enable(False)
        self.tc_centro_lucro.Enable(False)
        self.tc_descricao.Enable(False)
        self.tc_doc_referencia.Enable(False)
        self.tc_doc_compensacao.Enable(False)
        self.tc_montante.Enable(False)
        self.tc_moeda.Enable(False)

    def fc_part_ativa_botoes(self):
        self.bt_part_adicionar.Enable(True)
        if self.gd_partidas.GetNumberRows() > 0:
            self.bt_part_consultar.Enable(True)
            self.bt_part_excluir.Enable(True)
        else:
            self.bt_part_consultar.Enable(False)
            self.bt_part_excluir.Enable(False)
        self.bt_part_confirmar.Enable(False)
        self.bt_part_cancelar.Enable(False)

    def fc_part_desativa_botoes(self):
        self.bt_part_adicionar.Enable(False)
        self.bt_part_consultar.Enable(False)
        self.bt_part_excluir.Enable(False)
        self.bt_part_confirmar.Enable(True)
        self.bt_part_cancelar.Enable(True)

    def fc_atualiza_grade(self):
        for linha in range(self.gd_partidas.GetNumberRows()):
            self.gd_partidas.DeleteRows()
        if len(self.partidas) > 0:
            linha = 0
            for partida in self.partidas:
                self.gd_partidas.AppendRows(1)
                self.gd_partidas.SetCellValue(linha, 0, str(partida.registro))
                self.gd_partidas.SetCellValue(linha, 1, str(partida.conta_contabil))
                self.gd_partidas.SetCellValue(linha, 2, str(partida.descricao))
                self.gd_partidas.SetCellValue(linha, 3, str(partida.montante))
                self.gd_partidas.SetCellValue(linha, 4, str(partida.moeda))
                linha += 1
        self.fc_condicao()
