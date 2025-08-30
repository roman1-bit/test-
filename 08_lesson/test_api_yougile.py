import pytest
from Pages import Pages

# Тестовые данные
pages_instance = Pages('https://yougile.com/')
token = ''
invalid_token = 'invalid_token_12345'
id_project = "8907ceb7-b312-4c29-91d0-f65d3c3dcdd5"
id_project_neg = "ce4a2a83-98f0-4924-9924-05700508ce9"
malformed_id = "not-a-valid-uuid"


@pytest.mark.positive
def test_сreate_pos():
    new_simple = pages_instance.create(token, 'Тест 1')
    assert new_simple[0] == 201


def test_change_pos():
    change = pages_instance.change(token, 'Тест 1 Новый', id_project)
    assert change[0] == 200


def test_get_by_id_pos():
    get_by_id = pages_instance.get_by_id(token, id_project)
    assert get_by_id[0] == 200
    print(get_by_id[1])


@pytest.mark.negative
def test_сreate_neg():
    create_new = pages_instance.create(token, '')
    assert create_new[0] == 400


@pytest.mark.negative
def test_change_neg():
    change = pages_instance.change(token, '', id_project)
    assert change[0] == 400


@pytest.mark.negative
def test_get_by_id_neg():
    get_by_id = pages_instance.get_by_id(token, id_project_neg)
    assert get_by_id[0] == 404


@pytest.mark.negative
def test_create_with_invalid_token():
    create_new = pages_instance.create(invalid_token, 'Тест проект')
    assert create_new[0] == 401


@pytest.mark.negative
def test_create_without_token():
    create_new = pages_instance.create('', 'Тест проект')
    assert create_new[0] == 401


@pytest.mark.negative
def test_change_with_invalid_token():
    change = pages_instance.change(invalid_token, 'Новое название', id_project)
    assert change[0] == 401


@pytest.mark.negative
def test_get_by_id_with_invalid_token():
    """Тест получения проекта с недействительным токеном авторизации."""
    get_by_id = pages_instance.get_by_id(invalid_token, id_project)
    assert get_by_id[0] == 401  # Ожидаем ошибку авторизации


@pytest.mark.negative
def test_create_with_special_characters():
    special_chars_title = '<script>alert("xss")</script>'
    create_new = pages_instance.create(token, special_chars_title)
    assert create_new[0] in [400, 201]


@pytest.mark.negative
def test_change_with_malformed_project_id():
    change = pages_instance.change(token, 'Новое название', malformed_id)
    assert change[0] in [400, 404]


@pytest.mark.negative
def test_get_by_id_with_malformed_id():
    get_by_id = pages_instance.get_by_id(token, malformed_id)
    assert get_by_id[0] in [400, 404]


@pytest.mark.negative
def test_create_with_null_title():
    try:
        create_new = pages_instance.create(token, None)
        assert create_new[0] == 400
    except (TypeError, AttributeError):
        pass


@pytest.mark.negative
def test_change_nonexistent_project():
    change = pages_instance.change(token, 'Новое название', id_project_neg)
    assert change[0] == 404
