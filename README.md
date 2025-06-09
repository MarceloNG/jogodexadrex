# Jogodexadrex

Um jogo de xadrez simples para dois jogadores no mesmo computador.

## Requisitos

Instale as dependências utilizando:

```bash
pip install -r requirements.txt
```

## Como jogar

Execute o arquivo `main.py` com Python:

```bash
python main.py
```

Uma janela será aberta com o tabuleiro de xadrez. Clique em uma peça e em seguida
na casa de destino para realizar um movimento. As regras são validadas pela
biblioteca `python-chess`.

Se existirem imagens de peças na pasta `assets` com nomes como `wp.png` para o
peão branco e `bk.png` para o rei preto, elas serão utilizadas. Caso contrário,
o jogo mostrará o texto representando cada peça.
