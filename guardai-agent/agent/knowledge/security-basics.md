# Fundamentos de segurança

Base de conceitos para as análises do GuardAI. Leia quando a conversa envolver segurança.

## Conceitos-chave

- **Ativo**: o que tem valor e precisa de proteção (dados, serviço, servidor, reputação).
- **Vulnerabilidade**: uma fraqueza que pode ser explorada. Ex.: uma consulta SQL montada juntando texto digitado.
- **Ameaça**: quem ou o que pode explorar a fraqueza. Ex.: uma pessoa mal-intencionada, um malware.
- **Exploração (exploit)**: o ato ou a técnica que usa a vulnerabilidade.
- **Risco**: a chance de uma ameaça explorar uma vulnerabilidade e o dano que isso causa. Risco = probabilidade x impacto.
- **Controle**: o que reduz o risco (correção, configuração, processo, monitoramento).

Analogia: a porta com a fechadura quebrada é a vulnerabilidade, o ladrão é a ameaça, a casa é o ativo, e o risco é o quanto você tem a perder e a facilidade de entrarem.

## A tríade CIA

| Pilar | Pergunta | Exemplo de quebra |
|-------|----------|-------------------|
| Confidencialidade | Só quem pode vê os dados? | Vazamento de senhas ou de dados de clientes |
| Integridade | Os dados continuam corretos e sem alteração indevida? | Alguém altera um saldo ou apaga registros |
| Disponibilidade | O serviço está acessível quando preciso? | Servidor derrubado, dados sequestrados |

Ao avaliar impacto, pergunte qual dos três pilares é afetado e o quanto.

## Impacto, probabilidade e severidade

- **Impacto**: tamanho do dano se acontecer (Baixo, Médio, Alto).
- **Probabilidade**: facilidade e chance de acontecer, dado o contexto (Baixa, Média, Alta). Considere exposição, esforço do atacante e se já existe exploração conhecida.
- **Severidade**: o resultado do cruzamento.

| Probabilidade \ Impacto | Baixo | Médio | Alto |
|-------------------------|-------|-------|------|
| Baixa | Baixa | Baixa | Média |
| Média | Baixa | Média | Alta |
| Alta | Média | Alta | Crítica |

O contexto muda a nota. Um login com SQL Injection num app de estudo sem dados reais e isolado na máquina local tem severidade menor do que o mesmo código exposto na internet com dados de clientes.

CVSS é um sistema de pontuação usado pelo mercado para severidade. Para estudo, a matriz acima basta. Cite o CVSS só como referência e confirme valores na fonte oficial.

## Referências úteis

- **CWE**: catálogo de tipos de fraqueza (ex.: CWE-89, SQL Injection).
- **OWASP Top 10**: as categorias de risco mais comuns em aplicações web (ex.: Injection).
- **MITRE ATT&CK**: catálogo de técnicas de atacantes (ex.: T1190, Exploit Public-Facing Application).
- **CVE**: identificador de uma vulnerabilidade pública específica em um produto.

Em caso de dúvida sobre um identificador, consulte o site oficial em vez de confiar na memória.

## Boas práticas

- **Consultas parametrizadas** contra SQL Injection. Nunca monte SQL juntando entrada do usuário.
- **Valide e trate toda entrada** que vem de fora, no servidor.
- **Menor privilégio**: cada usuário, serviço e conta de banco com só o acesso de que precisa.
- **Defesa em profundidade**: várias camadas, para uma falha não derrubar tudo.
- **Senhas com hash lento e salt** (bcrypt, scrypt, Argon2 ou PBKDF2). Nunca em texto puro.
- **Segredos fora do código** (variáveis de ambiente, cofres de segredos). Nunca no repositório.
- **Atualize e aplique patches** de sistema e dependências.
- **Reduza a superfície**: desative o que não usa, feche portas desnecessárias, não exponha à internet sem necessidade.
- **Registre e monitore**: logs de login e de erros, alertas para tentativas estranhas.
- **Mensagens de erro genéricas** para o usuário, detalhes só no log.
- **Backups testados**, guardados fora do ambiente principal.
- **Autenticação forte**, com múltiplos fatores quando possível.
- **Segurança desde o início** no fluxo de desenvolvimento (DevSecOps): revisar cada alteração antes de ir para produção.

## Erros comuns de quem está começando

- Achar que "ninguém vai atacar um sistema pequeno". Varreduras automáticas encontram tudo que está exposto.
- Corrigir o sintoma e não a causa (ex.: filtrar aspas em vez de parametrizar).
- Confiar só em uma camada de proteção.
- Testar em sistemas de terceiros. Teste somente em ambiente próprio e autorizado.
