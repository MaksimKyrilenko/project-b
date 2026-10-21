from src.file_utils import read_json, write_json
from src.logger_utils import get_logger


def test_json_roundtrip(tmp_path):
    path = tmp_path / 'data' / 'tasks.json'
    write_json(path, [{'id': 1, 'title': 'Привет'}])
    assert read_json(path) == [{'id': 1, 'title': 'Привет'}]


def test_read_json_default(tmp_path):
    assert read_json(tmp_path / 'none.json', default=[]) == []


def test_logger_single_handler():
    get_logger('lab')
    assert len(get_logger('lab').handlers) == 1
