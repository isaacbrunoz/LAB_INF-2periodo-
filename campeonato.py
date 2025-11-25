import psycopg2

DB_NAME = "campeonato_db"
DB_USER = "postgres" 
DB_PASSWORD = "IS114" 
DB_HOST = "localhost"
DB_PORT = "5432"


def conectar_bd():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        
        return conn
    except psycopg2.Error as e:
        print(f"Erro ao conectar com o Banco de Dados: {e}")
        return None


def criar_tabela(conn):
    cursor = conn.cursor()
    sql_criar_tabela = """
    CREATE TABLE IF NOT EXISTS Jogos (
        id SERIAL PRIMARY KEY,
        time_casa VARCHAR(100) NOT NULL,
        time_visitante VARCHAR(100) NOT NULL,
        gols_casa INTEGER,
        gols_visitante INTEGER
    );
    """

    try:
        cursor.execute(sql_criar_tabela)
        conn.commit()
    except psycopg2.Error as e:
        print(f"Erro ao criar a tabela: {e}")


def inserir_jogo_manual(conn):
    print("\n--- Registro de Novo Jogo ---")
    time_casa = input("Digite o nome do Time da Casa: ")
    time_visitante = input("Digite o nome do Time Visitante: ")
    
    while True:
        try:
            gols_casa = int(input(f"Gols do {time_casa}: "))
            gols_visitante = int(input(f"Gols do {time_visitante}: "))
            break
        except ValueError:
            print("Erro: O placar deve ser um número inteiro. Tente novamente.")

    cursor = conn.cursor()
    
    sql_inserir = """
    INSERT INTO Jogos (time_casa, time_visitante, gols_casa, gols_visitante)
    VALUES (%s, %s, %s, %s) RETURNING id; 
    """
    
    try:
        cursor.execute(sql_inserir, (time_casa, time_visitante, gols_casa, gols_visitante))
        jogo_id = cursor.fetchone()[0]
        conn.commit()
        print(f"\n✅ Jogo ID {jogo_id} ({time_casa} {gols_casa} x {gols_visitante} {time_visitante}) inserido com sucesso!")
    except psycopg2.Error as e:
        print(f"Erro ao inserir o jogo: {e}")
        conn.rollback()


def listar_jogos(conn):
    cursor = conn.cursor()
    sql_select = "SELECT id, time_casa, gols_casa, gols_visitante, time_visitante FROM Jogos ORDER BY id DESC;"
    
    try:
        cursor.execute(sql_select)
        jogos = cursor.fetchall()
        
        print("\n--- Resultados de Todos os Jogos ---")
        if not jogos:
            print("Nenhum jogo registrado.")
            return

        for jogo in jogos:
            jogo_id, time_casa, gcasa, gvisitante, time_visitante = jogo
            print(f"[ID: {jogo_id}] {time_casa} {gcasa} x {gvisitante} {time_visitante}")
        print("--------------------------------------")
    except psycopg2.Error as e:
        print(f"Erro ao listar os jogos: {e}")


def excluir_jogo_por_id(conn):
    listar_jogos(conn) 

    print("\n--- Exclusão de Partida ---")
    try:
        jogo_id = int(input("Digite o ID (número) da partida que deseja EXCLUIR: "))
    except ValueError:
        print("❌ Erro: O ID deve ser um número inteiro. Tente novamente.")
        return

    cursor = conn.cursor()
    
    sql_delete = "DELETE FROM Jogos WHERE id = %s;"
    
    try:
        cursor.execute(sql_delete, (jogo_id,))
        
        linhas_afetadas = cursor.rowcount
        conn.commit()
        
        if linhas_afetadas > 0:
            print(f"\n✅ Partida ID {jogo_id} excluída com sucesso.")
        else:
            print(f"\n⚠️ Aviso: Nenhuma partida encontrada com o ID {jogo_id}.")
            
    except psycopg2.Error as e:
        print(f"❌ Erro ao excluir a partida: {e}")
        conn.rollback()


if __name__ == "__main__":
    conexao = conectar_bd()
    
    if conexao:
        criar_tabela(conexao)

        while True:
            print("\n---- CAMPEONATO DE JOGOS ----")
            print("\nO que você deseja fazer?")
            print("1. Inserir Novo Jogo")
            print("2. Listar Todos os Jogos")
            print("3. Excluir Partida") 
            print("4. Sair")
            
            escolha = input("Digite a opção (1, 2, 3 ou 4): ")
            
            if escolha == '1':
                inserir_jogo_manual(conexao)
            elif escolha == '2':
                listar_jogos(conexao)
            elif escolha == '3': 
                excluir_jogo_por_id(conexao)
            elif escolha == '4':
                print("Encerrando o programa. Até mais!")
                break
            else:
                print("Opção inválida. Tente novamente.")
                
        conexao.close()