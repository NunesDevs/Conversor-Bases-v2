# Memória técnica — revisão de qualidade

Revisão: 2026-11-08. Este arquivo descreve o código validado nesta rodada; inventários automáticos anteriores registram estados históricos.

Conversão posicional validada para decimal em bases 2, 4, 8, 16 e 20; menu mantém as quatro opções originais. Corrigidas condições sempre verdadeiras e uso inválido de dígitos. API to_decimal pura, sinais e letras minúsculas suportados; não aceita prefixo, separadores internos ou frações. Quatro testes, incluindo entrada inválida e EOF em subprocesso real, passaram em Python 3.12. Não há dependências ou deploy web. Distribuição em pacote de scripts MIT com checksum.

Validações: comandos de teste do README, execução local sem dados reais, git diff --check e revisão dos arquivos antes do commit. Push/integração/publicação têm autorização explícita do titular nesta sessão. Nenhuma migração, seed ou serviço de produção foi executado.
