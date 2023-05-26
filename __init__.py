import random


class CPFManager:

    def __init__(self) -> None:
        self.cpf = ''
        self.cpf_log = {}
            
        
    def script(self, nove_digitos_cpf='') -> tuple:
        contador_regressivo_1 = 10
        resultado_digito_1 = 0
        for digito in nove_digitos_cpf:
            resultado_digito_1 += int(digito) * contador_regressivo_1
            contador_regressivo_1 -= 1
        digito_1 = (resultado_digito_1 * 10) % 11
        digito_1 = digito_1 if digito_1 <= 9 else 0

        dez_digitos = nove_digitos_cpf + str(digito_1)
        contador_regressivo_2 = 11

        resultado_digito_2 = 0
        for digito in dez_digitos:
            resultado_digito_2 += int(digito) * contador_regressivo_2
            contador_regressivo_2 -= 1
        digito_2 = (resultado_digito_2 * 10) % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0
        
        
        return nove_digitos_cpf, digito_1, digito_2


    def gerar(self) -> list:
        nove_digitos = ''
        for i in range(9):
            nove_digitos += str(random.randint(0,9))

        dados = self.script(nove_digitos)
        
        cpf_tratado = f'{dados[0]}{dados[1]}{dados[2]}'
        cpf_pontuado = '{}{}{}.{}{}{}.{}{}{}-{}{}'.format(*cpf_tratado)

        self.cpf = cpf_tratado, cpf_pontuado
        
        self.cpf_log.update({self.cpf : 'Gerado'})
    

    def verificar_cpf(self, item: str) -> bool:
        item = str(item)
        if len(item) == 11:
            cpf_enviado_usuario = str(item)    

        elif len(item) == 14:
            item = item.replace('.','').replace('-','')
            cpf_enviado_usuario = str(item)   

        nove_digitos = cpf_enviado_usuario[:9]
        dados = self.script(nove_digitos)
        
        cpf_tratado = f'{dados[0]}{dados[1]}{dados[2]}'
        
        if cpf_enviado_usuario == cpf_tratado:
            self.cpf_log.update({self.cpf : 'Verificado'})
            return True
        
        else:
            return False



if __name__ == '__main__':
    cpf = CPFManager()

    cpf.gerar()
    cpf_gerado = cpf.cpf
    
    print(cpf_gerado)

    print(f'A verificação do CPF {cpf_gerado[0]} retornou: {cpf.verificar_cpf(cpf_gerado[0])}')
    print(f'A verificação do CPF {cpf_gerado[1]} retornou: {cpf.verificar_cpf(cpf_gerado[1])}')
    
    
    for i in range(8):
        cpf.gerar()
    
    print(cpf.cpf_log)
    
