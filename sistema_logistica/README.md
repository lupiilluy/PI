# Sistema de Gestão de Logística e Entregas

Sistema desenvolvido em Django para gestão de frotas, motoristas e entregas, com funcionalidade de rastreamento público para clientes.

## 📋 Funcionalidades

* **Gestão de Entregas:** Cadastro, edição e listagem.
* **Controle de Frota:** Gestão de motoristas e veículos.
* **Planejamento de Rotas:** Validação automática de capacidade de carga (impede sobrecarga do veículo).
* **Segurança:**
    * Admin: Acesso total.
    * Motorista: Acesso apenas às suas próprias rotas/entregas.
* **Área do Cliente:** Rastreamento público via código de encomenda.

## 🚀 Como Rodar o Projeto

### Pré-requisitos
* Python 3.10+
* Pip (Gerenciador de pacotes)

### Instalação

1.  Clone o repositório ou baixe a pasta.
2.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
    *(Ou use `poetry install` se tiver o Poetry)*

3.  Configure o Banco de Dados:
    ```bash
    python manage.py migrate
    ```

4.  Crie um Superusuário (Gestor):
    ```bash
    python manage.py createsuperuser
    ```

5.  Inicie o Servidor:
    ```bash
    python manage.py runserver
    ```

6.  Acesse:
    * **Home:** http://127.0.0.1:8000/
    * **Painel Admin:** http://127.0.0.1:8000/admin/

## 👤 Perfis de Acesso

* **Administrador:** Acesso via `/admin`. Pode cadastrar Motoristas, Veículos e Rotas.
* **Motorista:** Deve ser vinculado a um Usuário no Painel Admin. Ao logar na Home, vê apenas suas entregas.
* **Cliente:** Acessa `/rastreamento/` e digita o código da entrega (ex: CX-01).

---
Projeto Integrador - Ana Luiza Martins de Sousa

Método,URL (Rota),Descrição,Permissão
GET,/,Página Inicial (Escolha de Perfil),Pública
GET,/funcionario/,Lista de entregas (Dashboard),"Login Obrigatório (Motorista vê as dele, Admin vê tudo)"
GET,/entrega/editar/{id}/,Formulário de edição de status,Login Obrigatório (Dono da rota ou Admin)
POST,/entrega/editar/{id}/,Salva a alteração do status,Login Obrigatório
GET,/rastreamento/,Busca de entrega por código,Pública (Cliente)
GET,/admin/,Painel de Gestão Completa,Apenas Superusuário