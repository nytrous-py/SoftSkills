import sqlite3

def criar_bd():
    conexao = sqlite3.connect("softskills.db")
    cursor = conexao.cursor()

    # Criar tabela de colaboradores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS colaboradores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cargo TEXT,
            departamento TEXT
        )
    ''')

    # Criar tabela de interações com todas as colunas necessárias
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS interacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            colaborador_id INTEGER,
            tipo TEXT,
            falante TEXT,
            acao TEXT,
            conteudo TEXT,
            data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            Sentimento TEXT,
            Soft_Skill TEXT,
            categoria TEXT,
            FOREIGN KEY (colaborador_id) REFERENCES colaboradores(id)
        )
    ''')

    # Criar tabela de soft skills
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS soft_skills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            colaborador_id INTEGER,
            skill TEXT,
            pontuacao REAL,
            data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (colaborador_id) REFERENCES colaboradores(id)
        )
    ''')

    # Criar tabela de engajamento
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS engajamento (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            colaborador_id INTEGER,
            engajamento REAL,
            data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (colaborador_id) REFERENCES colaboradores(id)
        )
    ''')

    # Criar tabela de análise por departamento
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS analise_departamento (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            departamento TEXT,
            sentimento_geral TEXT,
            problemas_detectados TEXT,
            data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conexao.commit()
    conexao.close()
    print("✅ Banco de dados criado/atualizado com sucesso!")

if __name__ == "__main__":
    criar_bd()
