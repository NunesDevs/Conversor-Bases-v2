# Conversor para decimal

Converte números binários, octais, hexadecimais e vigesimais para decimal pela avaliação posicional dos dígitos. A API também aceita base 4. Não usa bibliotecas externas.

```sh
python conversor.py
python -m unittest discover -s tests -v
```

O menu mantém as quatro opções originais. Uma opção ou um dígito inválido recebe mensagem e nova tentativa; EOF e interrupção encerram a execução. Importar o módulo não inicia interação.

```python
from conversor import to_decimal
assert to_decimal("10101", 2) == 21
assert to_decimal("ff", 16) == 255
assert to_decimal("-J", 20) == -19
```

`to_decimal(texto, base)` valida cada dígito contra a base, aceita letras sem distinguir caixa, sinal opcional e espaços externos. Não aceita prefixos como `0x`, separadores internos ou frações. `conversao(valor, opt)` preserva a impressão do exemplo original e devolve o inteiro.

Quatro testes verificam dígitos, zero, sinais, letras minúsculas, entradas vazias/inválidas e resultados contra o parser de referência do Python. A correção removeu condições booleanas que sempre eram verdadeiras, como `if opt == 16 or 20`.

Aplicação de console Python 3. A distribuição é o código Python com sua licença MIT (`LICENSE`); não há site ou serviço externo.

Memória técnica: `docs/ai-context/QUALITY_REFRESH.md`.
