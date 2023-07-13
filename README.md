# CPFManager
<img src="https://visitor-badge.laobi.icu/badge?page_id=https://github.com/DevLucasLourenco/CPFManager"> 
Este código é responsável por gerenciar e verificar números de CPF (Cadastro de Pessoa Física) no formato brasileiro. Ela possui os seguintes atributos e métodos:

## Atributos
- `cpf` (string): Armazena o número de CPF gerado ou verificado.
- `cpf_log` (dict): Armazena um registro dos CPFs gerados ou verificados, juntamente com seu status.
## Métodos
- `gerar()`: Gera um número de CPF válido e atualiza os atributos cpf e cpf_log com as informações do CPF gerado.
- `verificar_cpf(item)`: Verifica se um número de CPF fornecido é válido. Retorna True se o CPF for válido e False caso contrário.

## Uso
#### Método `gerar()`
``` python
instancia_cpf = CPFManager()
instancia_cpf.gerar()
cpf_gerado = instancia_cpf.cpf

print(cpf_gerado)
```
> Retornará um CPF Válido, onde o índice 0 será o CPF sem pontuações, e o índice 1 com suas pontuações.
>> Ex.: 12345678912 e 123.456.789-12

#### Método `verificar_cpf()`
```python
print(f'A verificação do CPF {cpf_gerado[0]} retornou: {cpf.verificar_cpf(cpf_gerado[0])}')
print(f'A verificação do CPF {cpf_gerado[1]} retornou: {cpf.verificar_cpf(cpf_gerado[1])}')
```
> Um exemplo de output dessas duas linhas de comando, seria:
>> A verificação do CPF 12345678912 retornou: True
>> 
>> A verificação do CPF 123.456.789-12 retornou: True

> Caso retorne True, significa que o CPF é válido.

#### Atributo `cpf_log`
``` python
for i in range(8):
    cpf.gerar()

print(cpf.cpf_log)
```
> O atributo cpf_log é um dicionário que armazena os CPFs gerados ou verificados como chaves e seus status como valores. Isso permite o rastreamento dos CPFs que foram gerados ou verificados durante a execução do código.
>> Ex.:
```
{('35414966575', '354.149.665-75'): 'Verificado',
('41719412103', '417.194.121-03'): 'Gerado',
('15967019944', '159.670.199-44'): 'Gerado'}
```
