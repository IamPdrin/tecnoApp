# 📱 TecnoApp

O **TecnoApp** é um aplicativo mobile desenvolvido para a empresa **TecnoBombas**, especializada em manutenção de bombas hidráulicas, instalação de painéis eletrônicos e tubulações.  
O objetivo do projeto é digitalizar e modernizar a gestão de atendimentos e contratos, substituindo os métodos manuais de controle (papel e WhatsApp) por uma solução tecnológica eficiente e escalável.

---

## 🚩 Problema

Atualmente, a gestão da empresa é feita de forma manual em folhas de papel e cálculos no celular, o que gera:

- Risco de erros e perda de informações.  
- Dificuldade para acompanhar chamados e contratos.  
- Limitação no crescimento da empresa.  
- Atendimento restrito a WhatsApp e divulgação apenas no Instagram.  

---

## 💡 Solução

O **TecnoApp** propõe centralizar os processos em um aplicativo híbrido que inclui:

- **Administrador (empresário):**
  - Acompanhamento e gerenciamento de atendimentos.  
  - Checklists de chamados.  
  - Controle de contratos e clientes.  
  - Histórico de serviços e faturamento.  

- **Usuário (cliente):**
  - Solicitação de atendimentos.  
  - Acompanhamento em tempo real do status do serviço.  
  - Histórico de chamados realizados.  
  - Contato direto com o técnico.  

- **Machine Learning:**
  - Otimização de rotas de atendimentos (roteirização).  
  - Classificação automática de chamados urgentes.  

---

## 🎯 Público-Alvo

- **Clientes fixos**: condomínios e estabelecimentos que possuem contratos de manutenção.  
- **Clientes pontuais**: usuários que necessitam de serviços emergenciais.  
- **Administrador**: o empresário responsável pela TecnoBombas.  

---

## 🏗️ Arquitetura do Projeto

- **Mobile App**: [React Native](https://reactnative.dev/) + [Expo](https://expo.dev/)  
- **Backend**: [Node.js](https://nodejs.org/) + API RESTful  
- **Banco de Dados**: [Firebase Firestore](https://firebase.google.com/)  
- **Autenticação**: [Firebase Auth](https://firebase.google.com/products/auth)  
- **Machine Learning**: algoritmo de roteirização e classificação de urgência.  

**Fluxo Básico do Sistema:**  
Usuário solicita atendimento → API processa → ML sugere ordem/prioridade → Administrador gerencia → Usuário acompanha no app.

---

## 🖼️ Prototipação (UX/UI)

👉 **Em desenvolvimento** – Telas sendo modeladas no Figma.  
Sugestão de telas:  
- Login / Cadastro  
- Dashboard do Administrador (lista de atendimentos)  
- Solicitação de Atendimento (Usuário)  
- Histórico de Serviços  

---

## 🤖 Machine Learning no Projeto

O ML será utilizado em duas frentes:  

1. **Roteirização** – sugerindo ordem eficiente dos atendimentos baseada em localização dos clientes.  
2. **Classificação de Urgência** – análise de palavras-chave para priorizar chamados críticos.  

---

## 📌 Status Atual

- Estrutura inicial do projeto definida.  
- Configuração do Firebase em andamento.  
- Protótipos e primeiras telas em desenvolvimento.  

---

## 📈 Roadmap

- **Etapa 1**: Prototipação e telas principais (Figma + React Native).  
- **Etapa 2**: Implementação do backend e integração com Firebase.  
- **Etapa 3**: Inserção dos algoritmos de Machine Learning.  
- **Etapa 4**: Testes Beta com a empresa TecnoBombas.  

---

## 🧑‍💻 Tecnologias Utilizadas

- **Frontend:** React Native, Expo  
- **Backend:** Node.js, Express  
- **Banco de Dados:** Firebase Firestore  
- **Autenticação:** Firebase Auth  
- **Machine Learning:** Python/Node.js (a definir para classificação e roteirização)  

---

## 🚀 Como Executar o Projeto

> ⚠️ Em desenvolvimento – instruções iniciais de execução.  

1. Clone este repositório:
   ```bash
   git clone https://github.com/SEU-USUARIO/TecnoApp.git
   cd TecnoApp
   ```

2. Instale as dependências:
   ```bash
   npm install
   ```

3. Configure o Firebase:
   - Crie um projeto no [Firebase Console](https://console.firebase.google.com/).  
   - Adicione as credenciais no arquivo `firebase.ts`.

4. Execute o app:
   ```bash
   npx expo start
   ```

---

## 📞 Contato

**Desenvolvedor:** Pedro Henrique Bomfim Wolski  
**Cliente:** TecnoBombas (Nelson de Andrade Ennes do Valle)  
**Local:** Praia Grande – SP  

---
