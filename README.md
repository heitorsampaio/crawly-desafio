## Como rodar?

Para rodar o crawler basta simplesmente rodar comando abaixo caso tenha o Docker instalado em sua maquina.

```bash
  docker run -it $(docker build -q .)
```

Caso não tenha o Docker instalado, pode executar o seguinte comando.

```bash
pip install -r requirements.txt
python main.py
```
