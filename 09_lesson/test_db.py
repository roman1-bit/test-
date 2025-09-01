from sqlalchemy import create_engine
from sqlalchemy import text
import pytest


db_connecting = 'postgresql://postgres:aA123123@localhost:5432/postgres'

SQL_INSERT_TEACHER = text('insert into teacher ("teacher_id", "email", '
                          '"group_id") values (:teacher_id, :email, '
                          ':group_id)')

TEST_TEACHER_DATA = {'teacher_id': 1,
                     'email': 'test@mail.ru',
                     'group_id': 126}


@pytest.fixture()
def db_connection():
    db = create_engine(db_connecting)
    with db.connect() as connection:
        yield connection
        sql_delete = text("delete from teacher where teacher_id = :teacher_id")
        connection.execute(sql_delete, {'teacher_id': 1})
        connection.commit()


def test_insert(db_connection):
    connection = db_connection
    connection.execute(SQL_INSERT_TEACHER, TEST_TEACHER_DATA)
    connection.commit()

    rows = connection.execute(
        text("select teacher_id from teacher where teacher_id = 1")
    ).fetchall()
    row = rows[0]
    assert row[0] == 1


def test_update(db_connection):
    connection = db_connection
    connection.execute(SQL_INSERT_TEACHER, TEST_TEACHER_DATA)
    sql_update = text("update teacher set email = 'test_update@yahoo.ru' "
                      "where teacher_id = :teacher_id")
    connection.execute(sql_update, {'teacher_id': 1})
    connection.commit()

    rows = connection.execute(
        text("select email from teacher where teacher_id = 1")
    ).fetchall()
    row = rows[0]
    assert row[0] == 'test_update@yahoo.ru'


def test_delete(db_connection):
    connection = db_connection
    connection.execute(SQL_INSERT_TEACHER, TEST_TEACHER_DATA)
    sql_delete = text("delete from teacher where teacher_id = :teacher_id")
    connection.execute(sql_delete, {'teacher_id': 1})
    connection.commit()

    rows = connection.execute(
        text("select teacher_id from teacher where teacher_id = 1")
    ).fetchall()
    assert len(rows) == 0
