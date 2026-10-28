# 📘 Atividade: Testes Automatizados em Python com pytest

## 🎯 Objetivo

Aprenda a usar pytest para verificar funções Python e detectar comportamentos inesperados. Você praticará assertions, testes parametrizados e validação de exceções.

## 📝 Tarefas

### 🛠️ Escrever e executar testes básicos

#### Descrição
Instale pytest e execute o teste inicial em `test_starter_code.py`. Para este primeiro exercício, as funções e os testes ficam no mesmo arquivo para manter o foco nos conceitos de teste.

#### Requisitos
O programa concluído deve:

- Instalar pytest com `python -m pip install pytest`.
- Executar os testes a partir desta pasta com `python -m pytest -q`.
- Adicionar um teste que confirme que `is_even` retorna `False` para um número ímpar.
- Usar `assert` para verificar os resultados esperados.

### 🛠️ Testar vários casos com parametrização

#### Descrição
Amplie a cobertura de `calculate_average` usando `pytest.mark.parametrize` para verificar diferentes listas de números.

#### Requisitos
O programa concluído deve:

- Testar pelo menos três entradas, incluindo uma lista com vários números e uma lista com um único número.
- Comparar cada resultado com a média esperada.
- Executar todos os casos parametrizados com pytest.

### 🛠️ Verificar entradas inválidas

#### Descrição
Teste o comportamento de `calculate_average` quando a lista está vazia, usando o suporte do pytest para exceções.

#### Requisitos
O programa concluído deve:

- Usar `pytest.raises` para confirmar que uma lista vazia causa `ValueError`.
- Verificar se a mensagem da exceção explica que a lista não pode estar vazia.
- Manter todos os testes aprovados ao executar `python -m pytest -q`.