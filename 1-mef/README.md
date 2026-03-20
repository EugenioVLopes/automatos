# MEF — Máquina de Estados Finitos

Projeto 1 de Autômatos e Linguagens Formais (DCA-3705) — UFRN 2026.1

Simulador de uma Máquina de Estados Finitos (MEF) genérica, com menu interativo e dois exemplos pré-configurados.

## Estrutura

```
mef/
├── main.py          # Entry point
├── core/            # Lógica da MEF (criar, processar, resetar)
├── display/         # Exibição e execução interativa
└── exemplos/        # Máquinas pré-configuradas
```

## Como executar

```bash
python main.py
```

ou

```bash
uv run python main.py
```

## Exemplos incluídos

- **Máquina 1** — Exemplo do enunciado (3 estados, entradas `{0,1}`)
- **Máquina 2** — Detector de sequência `"01"` (saída `1` ao detectar o padrão)
