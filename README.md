# Conversor-Bases-v2

Conversor de entradas binárias, octais, hexadecimais e vigesimais para o sistema decimal.

## Funcionalidades verificadas

- Menu com bases 2, 8, 16 e 20.
- Conversão de dígitos alfanuméricos.
- Acumulação por potências da base.

## Operação e arquitetura verificadas

conversor.py separa menu e rotina de conversão; execução interativa sem dependências externas.

Arquivos principais: `conversor.py`.

### Requisitos e execução

Python 3; biblioteca padrão.

```text
python conversor.py
```



### Testes e estado

Não foi identificada uma suíte automatizada específica para os fluxos descritos; valide a execução e os casos de borda antes de publicar.

Estado: projeto de estudo/experimental. Deploy ativo não foi confirmado nesta revisão.

### Limitações conhecidas

- O menu não oferece base 4.
- Condições como opt == 16 or 20 são sempre verdadeiras e dígitos fora da base não são rejeitados.

### Licença e manutenção

Nenhum arquivo de licença foi identificado nesta revisão; não foi adicionada uma nova licença. Atualize comandos e limitações quando houver mudança de comportamento.
