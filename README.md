# Simulador de Ataque de Força Bruta (v1)

## Sobre o Projeto
Script em Python que simula ataques reais de quebra de senhas. Desenvolvido como parte dos meus estudos em segurança ofensiva (Red Team), o objetivo é demonstrar na prática o tempo, a mecânica e o custo computacional necessários para comprometer uma credencial, provando por que senhas fracas representam um risco crítico de segurança.

## Como Funciona
O script recebe uma senha definida pelo usuário que atuará como o "alvo". Em seguida, o sistema aplica métodos de ataque comuns para tentar descobri-la:

- **Ataque de Dicionário (Wordlist):** O script testa o alvo contra uma lista de senhas comuns, fracas e frequentemente vazadas (ex: `123456`, `password`, `admin`, `qwerty`).
- **Ataque de Força Bruta:** O sistema tenta adivinhar a senha testando exaustivamente combinações possíveis de caracteres.

Ao finalizar (ou durante a execução), o simulador exibe métricas de desempenho, incluindo o tempo total gasto na operação, a quantidade de tentativas realizadas e a velocidade do ataque (tentativas por segundo).

## Limitações Conhecidas
Como este é um projeto educacional construído para entender a lógica base de um ataque, o código possui limitações arquiteturais inerentes à linguagem e ao design da versão 1, documentadas abaixo:

1. **Comparação em Texto Claro (Plaintext):** O script compara a tentativa do ataque diretamente com a *string* da senha. Em um cenário real de invasão, o atacante não tem acesso ao texto claro, mas sim a um *hash* criptográfico (como MD5, SHA-256, bcrypt) extraído de um banco de dados, o que exige um processamento diferente.
2. **Gargalo de Desempenho (CPU vs GPU):** A rotina de força bruta roda usando a CPU e é limitada pelo GIL (Global Interpreter Lock) do Python. Ferramentas reais de mercado (como Hashcat ou John the Ripper) utilizam paralelismo e o poder de processamento massivo de placas de vídeo (GPUs) para testar bilhões de senhas por segundo.
3. **Gerenciamento de Memória na Wordlist:** Dependendo de como a leitura do arquivo da wordlist foi implementada, carregar um dicionário real de vazamentos (como a `rockyou.txt`, com mais de 14 milhões de senhas) de uma só vez para a memória RAM pode travar a aplicação. O ideal para grandes volumes é a leitura linha a linha (stream).
4. **Limitação de Comprimento:** Devido à natureza exponencial da força bruta na CPU, tentar quebrar senhas com mais de 6 ou 7 caracteres contendo letras e números pode levar dias ou anos no Python puro, inviabilizando testes complexos em tempo hábil.

## Projetos Relacionados
- **Analisador de Força de Senhas:** Avaliador de segurança de credenciais que identifica falhas de composição em senhas.
- **Detector de Login Suspeito:** Sistema que analisa logs para identificar tentativas de *brute force* e *credential stuffing*.

## Tecnologias
- Python (biblioteca padrão)
