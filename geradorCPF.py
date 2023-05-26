import random


class CPFManager:

    def __init__(self) -> None:
        self._nove_digitos = ''
        self._cpf_tratado = None
        self._cpf_pontuado = None
        self.cpf = None
        
        
    def script(self) -> tuple:
        
        contador_regressivo_1 = 10
        resultado_digito_1 = 0
        for digito in self._nove_digitos:
            resultado_digito_1 += int(digito) * contador_regressivo_1
            contador_regressivo_1 -= 1
        digito_1 = (resultado_digito_1 * 10) % 11
        digito_1 = digito_1 if digito_1 <= 9 else 0

        dez_digitos = self._nove_digitos + str(digito_1)
        contador_regressivo_2 = 11

        resultado_digito_2 = 0
        for digito in dez_digitos:
            resultado_digito_2 += int(digito) * contador_regressivo_2
            contador_regressivo_2 -= 1
        digito_2 = (resultado_digito_2 * 10) % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0

        return digito_1, digito_2


    def gerar(self) -> list:

        for i in range(9):
            self._nove_digitos += str(random.randint(0,9))

        dados = self.script()
        
        self._cpf_tratado = f'{self._nove_digitos}{dados[0]}{dados[1]}'
        self._cpf_pontuado = '{}{}{}.{}{}{}.{}{}{}-{}{}'.format(*self._cpf_tratado)

        self.cpf = self._cpf_tratado, self._cpf_pontuado
    

    def verificar_cpf(self, item: str) -> list:
        item = str(item)
        if len(item) == 11:
            cpf_enviado_usuario = str(item)    

        elif len(item) == 14:
            item = item.replace('.','').replace('-','')
            cpf_enviado_usuario = str(item)   

        self._nove_digitos = cpf_enviado_usuario[:9]
        dados = self.script()
        
        self._cpf_tratado = f'{self._nove_digitos}{dados[0]}{dados[1]}'
        if cpf_enviado_usuario == self._cpf_tratado:
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
