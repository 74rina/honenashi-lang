hone/
├── README.md
├── pyproject.toml
├── .gitignore
├── examples/
│ └── hello.hone
├── src/
│ └── hone/
│ ├── **init**.py
│ ├── cli.py
│ ├── commands/
│ │ ├── **init**.py
│ │ ├── run.py
│ │ └── repl.py
│ └── core/
│ ├── **init**.py
│ ├── runner.py
│ ├── lexer.py
│ ├── token.py
│ ├── parser.py
│ ├── ast.py
│ ├── interpreter.py
│ └── errors.py
└── tests/
├── test_runner.py
└── fixtures/
└── hello.hone

.honeファイル
↓
hone CLI
↓
言語処理系
↓
出力
