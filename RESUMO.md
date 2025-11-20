Estudo Teórico dos Padrões de Projeto
A aplicação de exemplo simula um sistema simplificado de Loja Virtual e incorpora os seguintes quatro padrões de projeto: Singleton, Builder, Proxy e Visitor.

Padrão Singleton (Criacional)
O padrão Singleton tem o propósito de garantir que uma classe tenha apenas uma instância e fornecer um ponto de acesso global para ela. Ele é ideal para recursos compartilhados, como o Catálogo de Produtos em Memória (simulado por ConcreteSingleton1 e ConcreteSingleton2), para manter a consistência de dados e evitar desperdício de memória. Sua estrutura é caracterizada por um construtor interno (o método __new__ em Python) e o uso de um Lock de Thread (threading.Lock), crucial para garantir que a única instância seja criada de forma segura mesmo em ambientes com múltiplas threads.

Padrão Builder (Criacional)
O padrão Builder permite construir objetos complexos passo a passo, separando a lógica de construção da representação final do objeto. Isso é útil quando a criação de um objeto, como um Produto na loja virtual, envolve muitas etapas opcionais ou quando o mesmo processo de construção precisa produzir diferentes tipos de produtos (ex: Produto Físico ConcreteProduct1 e Produto Digital ConcreteProduct2). O padrão utiliza uma interface AbstractBuilder que define as etapas de montagem, garantindo que o código cliente seja mais limpo e flexível, e evitando o problema do "construtor telescópico".

Padrão Proxy (Estrutural)
O padrão Proxy atua como um substituto ou intermediário para outro objeto (o Sujeito Real), controlando o acesso a ele. O objetivo é adicionar funcionalidades de controle, otimização ou segurança sem modificar o código do objeto original. O Proxy implementa a mesma interface do Sujeito Real (AbstractSubject) e adiciona lógicas como caching (otimização de acesso a produtos, como visto em Proxy1 e Proxy2) e verificação de segurança (controle de acesso por token, como visto em Proxy2). Essa separação de responsabilidades melhora a performance e a arquitetura do sistema, mantendo os Sujeitos Reais focados apenas na recuperação de dados.

Padrão Visitor (Comportamental)
O padrão Visitor permite adicionar novas operações (algoritmos) a uma estrutura de objetos existente (Elementos) sem modificar as classes desses elementos. Ele é aplicado quando se tem uma estrutura de objetos estável (como a hierarquia de Produtos) e a necessidade de adicionar muitas operações variáveis (como diferentes regras de precificação e cálculo de descontos, implementadas em ConcreteVisitor1 e ConcreteVisitor2). As novas regras são encapsuladas nas classes de Visitantes, mantendo a classe do produto limpa e em conformidade com o Princípio Aberto/Fechado (OCP).

Justificativas Detalhadas para a Aplicação dos Padrões
1. Singleton (Arquivo: singleton_guru.py)
O Singleton resolve a necessidade de um Catálogo de Produtos em Memória ser um recurso global e único. Foi escolhido para garantir que todos os módulos acessem exatamente a mesma fonte de dados do catálogo. Sem o padrão, o código seria pior por exigir o gerenciamento manual e inseguro da instância do catálogo, levando a inconsistências de dados e uso ineficiente de memória. O benefício é a consistência e o ponto de acesso centralizado ao estado do catálogo.

2. Builder (Arquivo: builder_guru.py)
O Builder resolve a complexidade na criação de Produtos na Loja Virtual, que possuem muitos atributos e diferentes tipos (Físico/Digital). Foi escolhido para padronizar e simplificar as etapas de construção. Sem o Builder, o código seria pior com o uso do "construtor telescópico" (muitos argumentos) ou com a necessidade de lógica de inicialização duplicada. O benefício é a legibilidade, manutenibilidade e a flexibilidade para adicionar novos tipos de produtos no futuro.

3. Proxy (Arquivo: proxy_guru.py)
O Proxy resolve a necessidade de adicionar lógica de valor agregado como caching e controle de acesso à recuperação de produtos (RealSubject). Foi escolhido para otimizar a performance (com cache em chamadas repetidas) e proteger dados sensíveis (com verificação de token). Sem o Proxy, o código seria pior por ter a lógica de cache e segurança implementada diretamente nos RealSubjects, violando o Princípio da Responsabilidade Única (SRP).

4. Visitor (Arquivo: visitor_guru.py)
O Visitor resolve o problema de adicionar operações variáveis (como regras de precificação e descontos) à classe estável de Produto. Foi escolhido porque as regras de negócio de e-commerce mudam frequentemente. Sem o Visitor, o código seria pior ao ter que modificar constantemente a classe ProductElement para cada nova regra de desconto ou imposto, violando o Princípio Aberto/Fechado (OCP). O benefício é a extensibilidade das regras e a manutenção de classes limpas.

Requisitos e Execução do Código
Requisitos do Sistema
O código está escrito em Python e utiliza apenas bibliotecas padrão.

Linguagem: Python 3.6+

Módulos:

abc (Abstract Base Classes)

typing (Suporte a type hinting)

threading (Usado no Singleton para garantir thread-safety)

time (Usado no Proxy para simular latência)

collections (Usado no Proxy, implícito no Dict)

#Como Rodar o Código:
O arquivo principal que orquestra as demonstrações de todos os padrões é o main.py.

Pré-requisito: Certifique-se de ter o Python 3.6 ou superior instalado no seu sistema.

Organização dos Arquivos: Todos os arquivos (main.py, singleton_guru.py, builder_guru.py, proxy_guru.py, visitor_guru.py) devem estar no mesmo diretório.

Execução: Abra o terminal (Prompt de Comando, PowerShell ou Terminal) no diretório onde os arquivos estão salvos e execute o seguinte comando:

Bash

python main.py
Saída Esperada: O script irá imprimir sequencialmente o output de demonstração de cada padrão (Singleton, Builder, Proxy e Visitor), comprovando o funcionamento e as propriedades de cada um (ex: a mesma instância para Singleton, o cache para Proxy).
