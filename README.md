# **Desafio de Projeto**

## **Sistema Bancário com Python**
Nível: Básico

Conteúdo: Conceitos Básicos

Linguagem: Python

----
### **DESAFIO**

**Objetivo geral**

Criar um sistema bancário simples com as operações: 
* Sacar
* Depositar
* Visualizar extrato

---

**Operações**

* Operação de depósito

Deve ser possível depositar valores positivos para a conta bancaria. A v1 do projeto trabalha apenas com 1 usuário, não sendo necessário identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

* Operação de saque

O sistema deve permitir realizar 3 saques diários com imite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação extrato.

* Operação de extrato

Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.

Os valores devem ser exibidos utilizando o formato R$ xxx.xx

*Exemplos*

1500.45 = R$ 1500.45

---
