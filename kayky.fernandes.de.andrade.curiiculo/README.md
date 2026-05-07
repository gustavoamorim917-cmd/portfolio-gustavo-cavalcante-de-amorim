# 📊 Algoritmo de Auditoria de Dados

## 📝 Descrição do Projeto
Este projeto consiste em um sistema de auditoria automatizada desenvolvido em Python para a validação de fluxos financeiros e transações comerciais. O objetivo principal é monitorar vendas diárias, identificando discrepâncias e garantindo que as operações permaneçam dentro de limites de segurança controlados.

[cite_start]Desenvolvido por **Kayky Fernandes de Andrade** [cite: 19, 20][cite_start], estudante de **Engenharia de Software** na **Unicid** [cite: 25, 57][cite_start], o algoritmo aplica lógica de programação para a resolução de problemas de arquitetura de software e integridade de dados[cite: 26]. O sistema destaca-se por sua capacidade de adaptação em tempo real e sinalização de estados críticos para revisão gerencial.

![Figura 1: Representação do fluxo de auditoria e monitoramento de limites](http://googleusercontent.com/image_generation_content/0)
*Figura 1: Esquema visual do processamento de vendas e gatilhos de segurança.*

## 🚀 Tecnologias Utilizadas
* **Linguagem:** Python
* **Ferramentas:** Google Colab
* [cite_start]**Habilidades Aplicadas:** Programação de Computadores [cite: 43] [cite_start]e lógica de desenvolvimento de sistemas[cite: 25].

## 📊 Regras de Negócio e Aprendizados
O projeto implementa verificações essenciais para a saúde financeira de um negócio:
* **Gestão de Limite Global:** Utiliza variáveis globais para permitir que um gerente altere o `LIMITE_SEGURANCA` (inicialmente R$ 10.000,00) dinamicamente durante a execução.
* **Protocolo de Quarentena:** O sistema isola automaticamente os resultados ("SISTEMA EM QUARENTENA") caso a média das vendas diárias ultrapasse o teto de segurança.
* **Detecção de Anomalias (Outliers):** Aciona a flag "REVISÃO MANUAL" se qualquer venda individual for superior ao dobro da média, prevenindo falhas operacionais ou fraudes.
* **Tratamento de Dados:** Aplicação de casting rigoroso (`float`) e verificação de tipos para assegurar a precisão dos cálculos financeiros.

## 🔧 Como Executar
1. [cite_start]Clone o repositório em seu ambiente local.
2. Certifique-se de ter o interpretador Python configurado.
3. Execute o script principal:
   ```bash
   python algoritmo_de_auditoria_de_dados.py