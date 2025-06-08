# 🔔 Sistema de Alerta Sensorial com Arduino - Projeto de Reciclagem

Este projeto foi desenvolvido como parte de um trabalho técnico para um **galpão de reciclagem**, visando aumentar a segurança de trabalhadores e visitantes no local.

## 🎯 Objetivo

O objetivo principal é implementar um **sistema de alerta sensorial** utilizando:

- **Arduino Uno**
- **Sensor Ultrassônico HC-SR04**
- **Buzzer**

O sistema detecta quando uma pessoa ou objeto entra em uma área perigosa ou restrita, pré-definida por uma distância mínima. Ao detectar essa aproximação, o **buzzer é ativado** com um som alto, servindo como alerta para evitar acidentes ou invasões em áreas sensíveis.

## ⚙️ Tecnologias e Componentes

- **Arduino Uno![Powerful Esboo](https://github.com/user-attachments/assets/a01a1ee8-8f6f-4dce-9aa8-f0c3d8584e3c)
**![WhatsApp Image 2025-06-08 at 18 22 29](https://github.com/user-attachments/assets/2c0bd408-413e-4f70-9017-e937b43e7181)

- **Sensor Ultrassônico HC-SR04**
- **Módulo Buzzer**
- **Python**
- **Tkinter (Interface gráfica)**
- **PySerial (Comunicação com Arduino)**
![Uploading Powerful Esboo.png…]()

## 🧠 Funcionamento

1. O Arduino monitora constantemente a distância usando o sensor ultrassônico.
2. Quando algo se aproxima a uma distância inferior ao limite configurado, o Arduino envia um alerta via porta serial.
3. Um script Python interpreta essa informação e, opcionalmente, exibe logs ou mensagens na tela.
4. O buzzer é ativado diretamente pelo Arduino como alerta sonoro.

## 👥 Participantes

- **Thompson**
- **Bhernardo**
- **Caio**
