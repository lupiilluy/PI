# Sistema de Gestão de Logística e Entregas

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0-green.svg?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57.svg?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Status](https://img.shields.io/badge/Status-Concluído-success)](https://github.com/)

## Instituição

[![Instituto Federal de Brasília](https://img.shields.io/badge/Instituição-IFB-red.svg?logo=read-the-docs&logoColor=white)](https://www.ifb.edu.br/)

## Desenvolvedora

**Ana Luiza Martins de Sousa**
*Projeto Integrador - Curso de Tecnologia em Sistemas para Internet (IFB)*

---

## Sumário

* [Visão Geral](#visão-geral)
* [Tecnologias Utilizadas](#tecnologias-utilizadas)
* [Estrutura do Projeto](#estrutura-do-projeto)
* [Funcionalidades e Rotas](#funcionalidades-e-rotas)
* [Configuração do Ambiente](#configuração-do-ambiente)

---

## Visão Geral

Este sistema foi desenvolvido para resolver problemas de gestão logística, centralizando o controle de entregas, motoristas, veículos e rotas. O objetivo é substituir controles manuais por uma aplicação web robusta que garante a integridade dos dados, impede sobrecarga de veículos e oferece rastreabilidade pública para clientes.

**Principais Soluções:**
* **Validação de Capacidade:** Algoritmo que impede que a soma das entregas exceda o limite do veículo.
* **Segurança (RBAC):** Motoristas acessam apenas suas próprias rotas; Gestores têm acesso total.
* **Transparência:** Clientes rastreiam encomendas via código único sem necessidade de login.

## Tecnologias Utilizadas

| Tecnologia | Versão | Descrição |
| :--- | :--- | :--- |
| **Python** | 3.12+ | Linguagem principal |
| **Django** | 5.x | Framework Web (MVT) |
| **SQLite** | 3 | Banco de Dados Relacional |
| **Poetry** | Latest | Gestão de dependências e ambiente virtual |
| **HTML5/CSS3** | N/A | Front-end e Templates Django |

## Estrutura do Projeto

A organização dos diretórios segue o padrão MVC (MVT no Django) para garantir escalabilidade e manutenção.

``` bash
sistema_logistica/
├── manage.py              # Script de gerenciamento do Django
├── pyproject.toml         # Configuração do Poetry
├── requirements.txt       # Lista de dependências (pip)
├── config/                # Configurações globais (settings, urls)
└── core/                  # Aplicação principal (Regras de Negócio)
    ├── models.py          # Tabelas (Motorista, Entrega, Veículo, Rota)
    ├── views.py           # Lógica das telas e controle de acesso
    ├── forms.py           # Formulários de edição
    ├── admin.py           # Configuração do Painel Admin
    └── templates/         # Arquivos HTML (Telas do sistema)

Funcionalidades e RotasO sistema opera com renderização de templates no servidor (Monolito).
Abaixo as principais funcionalidades e seus acessos:Funcionalidade,Rota (URL),Permissão,Descrição
Página Inicial,/,Pública,Tela de boas-vindas e escolha de perfil.
Dashboard,/funcionario/,Login Obrigatório,Lista entregas. Motorista vê apenas as suas; Admin vê tudo.
Rastreamento,/rastreamento/,Pública,Busca status de entrega por código (ex: CX-01).
Editar Entrega,/entrega/editar/<id>/,Login (Dono da Rota),"Permite alterar status para ""Entregue""."
Admin,/admin/,Superusuário,"Gestão completa de Motoristas, Veículos e Rotas.
```

## Configuração do Ambiente

Siga os passos abaixo para rodar o projeto na sua máquina local.

**Clone o repositório:**

``` bash
git clone [https://github.com/lupiilluy/PI.git](https://github.com/lupiilluy/PI.git)
cd PI/sistema_logistica
```
**Instale as dependências:**

``` bash

pip install -r requirements.txt
# Ou, se preferir Poetry: poetry install

```

**Configure o Banco de Dados:**

```` bash

poetry run python manage.py migrate

````

**Crie um Usuário Administrador:**

```` bash

poetry run python manage.py createsuperuser

````

**Inicie o Servidor:**

```` bash

poetry run python manage.py runserver

````

Acesse no navegador:Sistema: http://127.0.0.1:8000/
Painel Admin: http://127.0.0.1:8000/admin/

**Este arquivo faz parte da documentação do Projeto Integrador.**
