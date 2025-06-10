import sys
import os
module_path = os.path.abspath('modulos_e_pacotes')
sys.path.append(module_path)

from modulos_e_pacotes.biblioteca_contas.pacote_titulares.modulo_titular import Titular
from datetime import date

t1 = Titular('Diego', '123', date(1991, 8, 6))
print(t1.nome_titular)
print(t1.cpf)
print(t1.data_nascimento)
