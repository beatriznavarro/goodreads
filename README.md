# ETA 2022.2 - B - Testes Mobile - Projeto de Automação para Goodreads📚✨

## Descrição do Projeto
Este projeto tem como objetivo automatizar o aplicativo Goodreads utilizando Python, Appium e Unittest. Goodreads é uma plataforma online dedicada a amantes de livros, fornecendo recursos como avaliações, resenhas, listas de leitura e interação com outros leitores.

## Tecnologias Utilizadas
- **Python:** Linguagem de programação principal do projeto.
- **Appium:** Framework de automação para testes mobile.
- **Unittest:** Framework de testes unitários em Python.

## Estrutura do Projeto
O projeto segue a arquitetura de Page Objects, organizando o código de forma modular e facilitando a manutenção. Cada página do aplicativo Goodreads é representada por uma classe específica, contendo métodos para interagir com os elementos da página.

## Pré-requisitos
Para executar os testes com sucesso, o usuário deve ter uma conta no Goodreads e estar logado no aplicativo.

## Instruções para Execução
1. **Configuração do Ambiente:**
   - Certifique-se de ter o Python instalado em seu sistema.
   - Instale as dependências necessárias usando o gerenciador de pacotes pip:
     ```
     pip install -r requirements.txt
     ```

2. **Configuração do Appium:**
   - Instale o Appium em sua máquina.
   - Configure as capacidades necessárias no arquivo de configuração do Appium.

3. **Execução dos Testes:**
   - Execute os testes usando o seguinte comando dentro da pasta tests:
     ```
     python test_goodreads.py
     ```

## Observações
- É fundamental manter uma conta válida no Goodreads para a execução dos testes, uma vez que as funcionalidades requerem um usuário autenticado.

## Referências
- [Goodreads](https://www.goodreads.com/): Saiba mais sobre a plataforma Goodreads.

## Vídeo da automação executando: [Exemplo de execução](doc/execucao1712.mp4)
