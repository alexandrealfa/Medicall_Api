# Medicall API RESTFUL
​
Medicall é um sistema de gerenciamente de hospitais particulares.
​
## Métodos
​
Requisições para a API devem seguir os padrões:
​
| Método | Descrição                                    |
| ------ | -------------------------------------------- |
| GET    | Retorna informações de um ou mais registros. |
| POST   | Utilizado para criar um novo registro.       |
| PATCH  | Atualiza dados de um registro.               |
| DELETE | Remove um registro do sistema.               |
​
## Respostas
​
| Código | Descrição                                                          |
| ------ | ------------------------------------------------------------------ |
| 200    | Requisição executada com sucesso (success).                        |
| 400    | Erros de validação ou os campos informados não existem no sistema. |
| 401    | Dados de acesso inválidos.                                         |
| 404    | Registro pesquisado não encontrado (Not found).                    |
​
## Sobre a API
​
Medicall API conta com 3 tipos de usuários:
​
- Pacientes
- Médicos
- Administrador
​
# Os pacientes
​
### REGISTER - [POST] - "/patient"
​
O paciente deve se cadastrar para ter acesso as informações.
​
- **Request**
  - Body
​
```json
{
  "firstname": "John",
  "lastname": "Doe",
  "phone": "41 9999-9999",
  "email": "john@email.com",
  "password": "john123"
}
```
​
- **Response**
  - Body
​
```json
{
  "message": "success created",
  "data": {
    "id": 1,
    "firstname": "John",
    "lastname": "Doe",
    "phone": "41 9999-9999",
    "email": "john@email.com",
    "episodes_list": []
  }
}
```
​
### LOGIN - [POST] - "/login"
​
O paciente precisa logar em sua conta para ter acesso ao seu histórico de consultas.
​
- **Request**
  - Body
​
```json
{
  "email": "john@email.com",
  "password": "john123"
}
```
​
- **Response**
  - Body
​
```json
{
  "message": "sucess",
  "data": {
    "id": 1,
    "firstname": "John",
    "lastname": "Doe",
    "created_at": "2021-04-14 23:38:24.617771",
    "phone": "41 9999-9999",
    "email": "john@email.com",
    "episodes_list": []
  },
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxODUxOTY4OSwianRpIjoiZTlhNGIyZjMtM2M1Ny00ZmM1LWE5ZTItYTJmNGVjZWJlYjIzIiwibmJmIjoxNjE4NTE5Njg5LCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoyLCJleHAiOjE2MTkxMjQ0ODl9.WT3ySMn9K-Qyk41O9ZLMcdbUpia73YOSdK92uU8Il1A"
}
```
​
### UPDATE - [PATCH] - "/patient"
​
O paciente deve estar logado para atualizar seus dados.
​
- **Request**
  - Body
​
```json
{
  "phone": "41 0000-0000"
}
```
​
- **Response**
  - Body
​
```json
{
  "message": "success updated",
  "data": {
    "id": 1,
    "firstname": "John",
    "lastname": "Doe",
    "phone": "41 0000-0000",
    "email": "john@email.com"
  }
}
```
​
### DELETE - [DELETE] - "/patient"
​
O paciente deve estar logado para dedsativar sua conta.
​
- **Request**
​
  - curl -X DELETE 'http://localhost:5000/patient ' -H 'Authorization: Bearer <TOKEN>'
​
- **Response**
  - Body
​
```json
{
  "message": "patient 1 was disabled"
}
```
​
# Os médicos
​
### REGISTER - [POST] - "/doctor"
​
O doutor deve se cadastrar para ter acesso as informações.
​
- **Request**
  - Body
​
```json
{
  "firstname": "John",
  "lastname": "Doe",
  "crm": "015432/PR",
  "specialty": "Pediatria",
  "phone": "41 9999-9999",
  "email": "john@email.com",
  "password": "john123"
}
```
​
- **Response**
  - Body
​
```json
{
  "message": "success created",
  "data": {
    "id": 1,
    "firstname": "John",
    "lastname": "Doe",
    "crm": "015432/PR",
    "specialty": "Pediatria",
    "phone": "41 9999-9999",
    "email": "john@email.com",
    "episodes_list": []
  }
}
```
​
### LOGIN - [POST] - "/login"
​
O doutor precisa logar em sua conta para ter acesso ao seu histórico de consultas.
​
- **Request**
  - Body
​
```json
{
  "email": "john@email.com",
  "password": "john123"
}
```
​
- **Response**
  - Body
​
```json
{
  "message": "sucess",
  "data": {
    "id": 1,
    "firstname": "John",
    "lastname": "Doe",
    "crm": "015432/PR",
    "specialty": "Pediatria",
    "created_at": "2021-04-14 23:38:24.617771",
    "phone": "41 9999-9999",
    "email": "john@email.com",
    "episodes_list": []
  },
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxODUxOTY4OSwianRpIjoiZTlhNGIyZjMtM2M1Ny00ZmM1LWE5ZTItYTJmNGVjZWJlYjIzIiwibmJmIjoxNjE4NTE5Njg5LCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoyLCJleHAiOjE2MTkxMjQ0ODl9.WT3ySMn9K-Qyk41O9ZLMcdbUpia73YOSdK92uU8Il1A"
}
```
​
### UPDATE - [PATCH] - "/doctor"
​
O doutor deve estar logado para atualizar seus dados.
​
- **Request**
  - Body
​
```json
{
  "phone": "41 0000-0000"
}
```
​
- **Response**
  - Body
​
```json
{
  "message": "success updated",
  "data": {
    "id": 1,
    "firstname": "John",
    "lastname": "Doe",
    "phone": "41 0000-0000",
    "crm": "015432/PR",
    "specialty": "Pediatria",
    "email": "john@email.com"
  }
}
```
​
### DELETE - [DELETE] - "/doctor"
​
O doutor deve estar logado para desativar sua conta.
​
- **Request**
​
  - curl -X DELETE 'http://localhost:5000/doctor ' -H 'Authorization: Bearer <TOKEN>'
​
- **Response**
  - Body
​
```json
{
  "message": "doctor 1 was disabled"
}
```
​
# Os administradores
​
### REGISTER - [POST] - "/root"
​
O adiministrador deve se cadastrar para ter acesso as informações.
​
- **Request**
  - Body
​
```json
{
  "firstname": "Admin",
  "lastname": "Geral",
  "phone": "41 9999-9999",
  "email": "admin@email.com",
  "password": "admin123"
}
```
​
- **Response**
  - Body
​
```json
{
  "message": "success created",
  "data": {
    "phone": "41 9999-9999",
    "email": "admin@email.com",
    "created_at": "2021-04-22 16:20:14.057767",
    "lastname": "Geral",
    "id": 1,
    "firstname": "Admin"
  }
}
```
​
### LOGIN - [POST] - "/login"
​
O Administrador precisa estar logado para ter todos acessos.
​
- **Request**
  - Body
​
```json
{
  "email": "admin@email.com",
  "password": "admin123"
}
```
​
- **Response**
  - Body
​
```json
{
  "message": "sucess",
  "data": {
    "phone": "41 9999-9999",
    "email": "admin@email.com",
    "created_at": "2021-04-22 16:20:14.057767",
    "lastname": "Geral",
    "id": 1,
    "firstname": "Admin"
  },
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxODUxOTY4OSwianRpIjoiZTlhNGIyZjMtM2M1Ny00ZmM1LWE5ZTItYTJmNGVjZWJlYjIzIiwibmJmIjoxNjE4NTE5Njg5LCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoyLCJleHAiOjE2MTkxMjQ0ODl9.WT3ySMn9K-Qyk41O9ZLMcdbUpia73YOSdK92uU8Il1A"
}
```
​
### UPDATE - [PATCH] - "/root"
​
O administrador deve estar logado para atualizar seus dados.
​
- **Request**
  - Body
​
```json
{
  "phone": "41 0000-0000"
}
```
​
- **Response**
  - Body
​
```json
{
  "message": "success updated",
  "data": {
    "phone": "41 0000-0000",
    "email": "admin@email.com",
    "created_at": "2021-04-22 16:20:14.057767",
    "lastname": "Geral",
    "id": 1,
    "firstname": "Admin"
  }
}
```
​
### DELETE - [DELETE] - "/doctor"
​
O administrador deve estar logado para desativar sua conta.
​
- **Request**
​
  - curl -X DELETE 'http://localhost:5000/root ' -H 'Authorization: Bearer <TOKEN>'
​
- **Response**
  - Body
​
```json
{
  "message": "super user 1 was disabled"
}
```