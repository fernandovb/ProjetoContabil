# -*- coding: utf-8 -*-

from _dados.prm.dplpes import DPLPES
import utilidades.federal as federal


class RPLPES:
    status_familiar = {1: 'SOLTEIRO', 2: 'CASADO', 3: 'EM UNIÃO ESTÁVEL', 4: 'DIVORCICADO', 5: 'VIUVO'}

    def __init__(self, codigo):
        pessoa = DPLPES(codigo)
        self.codigo = codigo
        self.nome_formal = str(pessoa.nome_formal).upper()
        self.atividade = str(pessoa.atividade).lower()
        self.nacionalidade = str(pessoa.nacionalidade).lower()
        self.est_civil = str(self.status_familiar[pessoa.est_civil]).lower()
        self.federal = federal.formata_cadastro(str(pessoa.federal))
        self.estadual = pessoa.estadual
        self.org_emissor = str(pessoa.org_emissor).upper()
