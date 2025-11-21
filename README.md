# Estudo e Aplicação de Padrões de Projeto - Parte 2: Loja Virtual

## Descrição do Projeto

Este projeto consiste em uma aplicação simplificada em **Python** que simula um **Sistema de Catálogo e Processamento de Produtos de uma Loja Virtual**. 

O objetivo é demonstrar a aplicação prática e justificada de **quatro Padrões de Projeto (Design Patterns)**, cobrindo todas as 3 categorias: Criacional, Estrutural e Comportamental.

O foco do sistema é em flexibilidade arquitetural, manutenibilidade e escalabilidade, implementando as seguintes funcionalidades principais:
* Gerenciamento de Catálogo (Singleton).
* Criação flexível de diferentes tipos de produtos (Builder).
* Acesso otimizado e seguro aos dados do produto (Proxy).
* Adição de regras de precificação e desconto sem alterar classes de produto (Visitor).

---

## Padrões de Projeto Implementados

Abaixo estão os 4 padrões utilizados e os arquivos onde eles são encontrados:

| Padrão | Categoria | Descrição da Aplicação no Projeto | Arquivo Principal |
| :--- | :--- | :--- | :--- |
| **1. Singleton** | Criacional | Garante uma única instância global para o **Catálogo de Produtos** em memória. | `singleton_catalog.py` |
| **2. Builder** | Criacional | Permite a construção passo a passo de objetos de **Produto** complexos (Físicos e Digitais). | `builder_product.py` |
| **3. Proxy** | Estrutural | Controla o acesso à recuperação de dados, adicionando lógica de **Cache** e **Segurança** (Token). | `proxy_product_access.py` |
| **4. Visitor** | Comportamental | Permite adicionar **regras de precificação/desconto** sem modificar as classes base dos produtos. | `visitor_pricing_rules.py` |

---

## Requisitos e Execução do Código

### 1. Requisitos do Sistema

O projeto é baseado em bibliotecas padrão e não requer dependências externas.

| Categoria | Detalhes | Módulos Padrão Utilizados |
| :--- | :--- | :--- |
| **Linguagem** | Python 3.6 ou superior. | `abc`, `typing` |
| **Thread Safety** | Usado no Singleton para garantir unicidade em multi-thread. | `threading` |
| **Simulação** | Usado no Proxy para simular latência de rede. | `time` |

### 2. Instruções de Execução

O arquivo principal que executa as demonstrações de todos os padrões é o `main.py`.

1.  **Organização dos Arquivos:** Certifique-se de que todos os arquivos (incluindo `main.py`, `singleton_catalog.py`, `builder_product.py`, `proxy_product_access.py`, e `visitor_pricing_rules.py`) estejam no **mesmo diretório**.
2.  **Execução:** Abra o terminal (Prompt de Comando, PowerShell ou Terminal) no diretório do projeto e execute o comando:

```bash
python main.py