# Desafio: Simulando um Ransomware com Python

Este projeto foi desenvolvido como um laboratório prático para fins puramente educacionais e de estudo em cibersegurança, simulando a lógica de funcionamento estrutural de um ransomware de criptografia.

## 🛠️ Tecnologias Utilizadas
* **Python 3**
* **pyaes** (Biblioteca para criptografia AES em modo CTR)

## 📁 Estrutura do Projeto
* `encrypter.py`: Script responsável por ler um arquivo de texto, apagar o original e gerar uma versão criptografada com a extensão `.ransomwaretroll`.
* `decrypter.py`: Script responsável por reverter o processo, descriptografando o arquivo `.ransomwaretroll` e restaurando o arquivo de texto original.
* `teste.txt`: Arquivo de texto puro utilizado como alvo para a validação dos testes locais.

## 🚀 Como Executar o Projeto
1. Certifique-se de ter o Python instalado e a biblioteca `pyaes` configurada:
   ```bash
   pip install pyaes
   ```
2. Para realizar a criptografia do arquivo de teste, execute:
   ```bash
   python encrypter.py
   ```
3. Para reverter o processo e recuperar o arquivo original, execute:
   ```bash
   python decrypter.py
   ```

## ⚠️ Isenção de Responsabilidade
Este código foi criado estritamente para o entendimento teórico de ameaças cibernéticas e conformidade com desafios de plataformas de ensino (como a DIO). O uso dessas ferramentas em ambientes sem autorização prévia é ilegal.

## 📸 Demonstração Prática

### Execução do Script de Criptografia
![Tela do Encrypter](Imagens%20do%20projeto/NOME_DA_SUA_IMAGEM_1.png)

### Execução do Script de Descriptografia
![Tela do Decrypter](Imagens%20do%20projeto/NOME_DA_SUA_IMAGEM_2.png)
