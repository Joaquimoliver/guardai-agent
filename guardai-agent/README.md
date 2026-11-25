# 🛡️ GuardAI: agente de cibersegurança e análise de vulnerabilidades

Especialização do [DIO Agent](https://github.com/digitalinnovationone/dio-agent) que transforma o agente num mentor de segurança. Em vez de responder direto, ele **entende o contexto, avalia impacto, probabilidade e severidade e orienta a correção**, como um profissional de segurança faria.

Nenhum modelo foi treinado: o agente aprende só pelo que está escrito nos arquivos (skill, conhecimento e persona).

## 🎯 A especialização e o porquê

O foco é **AppSec e segurança defensiva**. Um chat comum, quando perguntado sobre um servidor exposto, costuma despejar comandos. Mas o risco depende do contexto: um servidor de laboratório sem dados e um servidor de produção com dados de clientes são casos bem diferentes. O GuardAI foi ensinado a **perguntar antes de agir**, a trabalhar **só com laboratório próprio** e a focar em **defender**, não em atacar.

## 🗂️ O que foi criado ou alterado

| Arquivo | Tipo | O que é |
|---------|------|---------|
| [`skills/vulnerability-analysis/SKILL.md`](skills/vulnerability-analysis/SKILL.md) | novo | A skill: o roteiro que o agente segue (escopo, contexto, falha, explicação, risco, correção, validação, relatório) |
| [`skills/vulnerability-analysis/README.md`](skills/vulnerability-analysis/README.md) | novo | Explica a skill para pessoas |
| [`agent/knowledge/security-basics.md`](agent/knowledge/security-basics.md) | novo | Vulnerabilidade, ameaça, risco, tríade CIA, matriz de severidade e boas práticas |
| [`agent/persona.md`](agent/persona.md) | alterado | Nova seção "Postura em segurança" |
| [`AGENTS.md`](AGENTS.md) | alterado | Skill na tabela, conhecimento na lista e seção "Segurança" |
| [`lab/app.py`](lab/app.py) | novo | Login propositalmente vulnerável a SQL Injection (laboratório) |
| [`lab/app_seguro.py`](lab/app_seguro.py) | novo | Versão corrigida: consulta parametrizada e senha com hash |
| [`lab/test_login.py`](lab/test_login.py) | novo | Teste que mostra a falha e a mitigação |
| [`docs/cenarios-de-teste.md`](docs/cenarios-de-teste.md) | novo | Roteiro de testes do agente |
| [`docs/evidencias/`](docs/evidencias/README.md) | novo | Prints dos testes |

## ▶️ Como rodar o agente

1. Instale o **Hermes** pela [documentação oficial](https://hermes-agent.nousresearch.com/docs).
2. Baixe este repositório:
   ```
   git clone https://github.com/SEU-USUARIO/guardai-agent.git
   cd guardai-agent
   ```
3. **Abra o terminal na pasta do projeto** (a que tem o `AGENTS.md`) e rode `hermes`. Aberto em outro lugar, ele não encontra os arquivos.
4. Converse. Exemplos:
   - "Atue como especialista em AppSec. Analise o `lab/app.py`, encontre a falha, explique a exploração, cite a técnica do MITRE ATT&CK e reescreva o código."
   - "Tenho um servidor Ubuntu de laboratório exposto na internet. Como deixo mais seguro?"

Para ver o laboratório sem o agente: `python lab/test_login.py`.

## 🧪 Como testei

O roteiro completo está em [`docs/cenarios-de-teste.md`](docs/cenarios-de-teste.md): código vulnerável, validação da correção, servidor Ubuntu de laboratório, recusa de alvo de terceiros e comparação com chat genérico. Todos os testes usam apenas código e ambientes de laboratório meus.

## 🚀 Melhoria escolhida: saída padronizada

Toda análise termina no mesmo formato (alvo, vulnerabilidade, impacto, probabilidade, severidade, correção, validação), com a severidade vinda de uma matriz impacto x probabilidade. Assim dá para **comparar casos diferentes** e priorizar o que corrigir primeiro.

## 📸 Evidências

Prints da análise do `app.py`, das perguntas de contexto e da comparação com o chat genérico ficam em [`docs/evidencias/`](docs/evidencias/README.md).

## ⚠️ Aviso

O `lab/app.py` é inseguro de propósito. Use só para estudo, em ambiente próprio. Não teste técnicas de ataque em sistemas de terceiros.

## 🙌 Créditos

Baseado no [DIO Agent](https://github.com/digitalinnovationone/dio-agent), da DIO. Projeto do desafio GuardAI.
