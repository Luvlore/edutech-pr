endereco = 'Rua das Flores 72, apartamento 1002, Rio de Janeiro, RJ, 23440-120'

import re # regular expressions -- RegEx

# 5 digitos + hífen (opicional) + 3 digitos

padrao = re.compile('[0-9]{5}[-]{0,1}[0-9]{3}')

busca = padrao.search(endereco) # match
if busca:
    cep = busca.group()
    print(cep)
