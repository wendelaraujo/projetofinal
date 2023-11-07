import pymysql.cursors
from aluno_model import Aluno

class AlunoData:
    def __init__(self):
        self.conexao = pymysql.connect(
            host='localhost', user='root',password='',database='escola',
            cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conexao.cursor()

    def inserir(self, aluno: Aluno) -> None:
        sql = 'INSERT INTO alunos(matricula,nome, idade,curso,nota) values'\
              '(%s,%s,%s,%s,%s)'
        try:
            self.cursor.execute(sql,(aluno.matricula,aluno.nome,aluno.idade,aluno.curso,
                                     aluno.nota))
            self.conexao.commit()
        except Exception as error:
            print(f'Erro ao inserir! :{error}')

    def select(self) -> list:
        try:
            sql = 'SELECT * FROM alunos'
            self.cursor.execute(sql)
            alunos = self.cursor.fetchall()
            return alunos
        except Exception as error:
            print(f'Erro ao listar! :{error}')

    def update(self, aluno: Aluno) -> None:
        try:
            sql = "UPDATE alunos SET nome = %s, idade = %s, curso = %s, " \
                  "nota = %s where matricula = %s"
            self.cursor.execute(sql , (aluno.nome,
                                       aluno.idade,
                                       aluno.curso,
                                       aluno.nota,
                                       aluno.matricula))
            self.conexao.commit()
        except Exception as error:
            print(f"Erro ao editar! :{error}")
    def delete(self, matricula: str) -> None:
        try:
            sql = "DELETE FROM alunos WHERE matricula = %s"
            self.cursor.execute(sql, matricula)
            self.conexao.commit()
        except Exception as error:
            print(f'Erro ao deletar! {error}')


if __name__ == '__main__':
    db = AlunoData()
    db.delete('0596423c-7cf8-11ee-94d4-80d21df33cb0')

