# Flask Docker App

Atividade da aula de Docker do professor Aécio Pires na Pós de Desenvolvimento Full Stack da Unipê, para o aluno Francisco Albuquerque.

## Como Usar

Certifique-se de ter o Docker instalado em sua máquina.

1. Clone este repositório:

    ```bash
    git clone https://github.com/facaj/flask-docker-app.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd aula_docker_pos_unipe
    ```

3. Construa a imagem Docker:

    ```bash
    docker build -t flask-docker-app .
    ```

4. Execute o contêiner Docker:

    ```bash
    docker run -p 5000:5000 flask-docker-app
    ```

5. Abra um navegador da web e acesse a seguinte URL:

    [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

Agora, você deve ver a página da web com as informações da aula.

