# 📊 Mapeamento de Soft Skills com BERT

## 📝 Descrição
Este projeto é um **dashboard interativo** para análise de **soft skills e sentimentos** utilizando **BERT (modelo NLP)**. Permite que equipas de Recursos Humanos analisem interações digitais (e-mails, transcrições, etc.) para obter insights sobre as **competências interpessoais** e **níveis de envolvimento** dos colaboradores e candidatos.

## 🚀 Funcionalidades
- **Análise de Sentimentos**: Classificação de emoções nas interações.
- **Identificação de Soft Skills**: Deteção automática de competências interpessoais.
- **Upload de Ficheiros**: Suporte para CSV e TXT.
- **Filtragem Inteligente**: Apenas mensagens de **candidatos** são processadas.
- **Relatórios de Envolvimento**: Estatísticas sobre interações por categoria.
- **Gráficos Dinâmicos**: Visualização de sentimentos por departamento.

## 🛠️ Tecnologias Utilizadas
- **Python**
- **Streamlit** (para interface)
- **SQLite** (base de dados)
- **Transformers (Hugging Face)** (modelo BERT para análise de sentimentos)
- **Pandas** (manipulação de dados)

## 📂 Estrutura do Projeto
```
📦 softskills-dashboard
├── app.py  # Interface principal
├── database.py  # Configuração da base de dados
├── requirements.txt  # Dependências do projeto
├── README.md  # Documentação do projeto
└── data/  # Ficheiros de entrada e saída
```

## 📥 Como Instalar e Executar
### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/softskills-dashboard.git
cd softskills-dashboard
```

### 2️⃣ Criar ambiente virtual e instalar dependências
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Criar a base de dados
```bash
python database.py
```

### 4️⃣ Executar o dashboard
```bash
streamlit run app.py
```

## 🔥 Contribuir
Se quiser contribuir, sinta-se à vontade para **abrir uma issue ou enviar um pull request**! 🚀

## 📜 Licença
Este projeto está sob a licença MIT. Consulte `LICENSE` para mais detalhes.

