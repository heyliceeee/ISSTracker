# ISS Overhead Notifier

Este projeto monitoriza em tempo real a posição da Estação Espacial Internacional e identifica quando ela passa sobre a localização do utilizador durante a noite. Quando ambas as condições se verificam, é enviado um alerta por email a informar que a ISS está visível no céu.





## 🎯 Objetivo

Criar um sistema autónomo que:
- verifica continuamente a posição atual da ISS  
- determina se esta se encontra dentro de um raio de proximidade definido  
- confirma se é noite no local do utilizador  
- envia uma notificação por email quando a ISS está visível

## 🌍 Funcionalidade Principal

- Consulta periódica de APIs públicas para obter:
  - posição atual da ISS  
  - horários de nascer e pôr do sol  
- Avaliação automática das condições necessárias para visibilidade  
- Envio de um email de alerta sempre que a ISS passa sobre o utilizador durante a noite  
- Funcionamento contínuo, sem necessidade de intervenção manual  

## 📡 APIs Utilizadas

- **ISS Now API** — fornece a posição atual da Estação Espacial Internacional  
- **Sunrise‑Sunset API** — disponibiliza horários de nascer e pôr do sol para qualquer coordenada  

## ✉️ Notificação por Email

Quando a ISS está suficientemente próxima e é noite, o sistema envia automaticamente uma mensagem com o aviso de visibilidade. O objetivo é permitir que o utilizador olhe para o céu no momento certo.

## 🧭 Casos de Utilização

- Observação astronómica casual  
- Alertas educativos para escolas ou clubes de ciência  
- Demonstração prática de automação com APIs e notificações  
- Projetos de monitorização em tempo real  
