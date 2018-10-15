import solution
from io import StringIO
import sys

# todo 1 - added the u to solve the unicode problem (TypeError: initial_value must be unicode or None, not str).
# todo 2 - pytest.monkeypatch doesn't work using jupyter notebook.
empty_place_inputs = StringIO(u'\n')
one_place_input = StringIO(u'London, England\n\n')
many_place_inputs = StringIO(u'''Shanghai, China
Beijing, China
Tel Aviv, Israel
Haifa, Israel
Madrid, Spain
Barcelona, Spain

''')

# todo - note that the last empty line is important for the empty response case

def test_no_places_001(monkeypatch):
    monkeypatch.setattr('sys.stdin', empty_place_inputs)
    solution.collect_places()
    assert len(solution.visits) == 0


def test_one_place_002(monkeypatch):
    monkeypatch.setattr('sys.stdin', one_place_input)
    solution.collect_places()
    assert len(solution.visits) == 1


def test_many_places_003(monkeypatch):
    monkeypatch.setattr('sys.stdin', many_place_inputs)
    solution.collect_places()
    assert len(solution.visits) == 3


def test_invalid_input_004(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO(u'abcd\n\n'))
    solution.collect_places()
    captured_out, captured_err = capsys.readouterr()
    assert captured_out.strip().startswith("Tell me where you went:That's not a legal city, country combination")
    assert captured_out.strip().endswith("Tell me where you went:")


def test_sorting_cities_005(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO(u'Shanghai, China\nBeijing, China\nBeijing, China\n\n'))
    solution.collect_places()
    captured_out, captured_err = capsys.readouterr()

    solution.display_places()
    captured_out, captured_err = capsys.readouterr()
    beijing_index = captured_out.index('Beijing')
    shanghai_index = captured_out.index('Shanghai')
    assert beijing_index < shanghai_index


def test_sorting_countries_006(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO(u'Haifa, Israel\nLondon, England\nNew York, USA\n\n'))
    solution.collect_places()
    captured_out, captured_err = capsys.readouterr()

    solution.display_places()
    captured_out, captured_err = capsys.readouterr()
    israel_index = captured_out.index('Israel')
    england_index = captured_out.index('England')
    usa_index = captured_out.index('USA')
    assert england_index < israel_index
    assert israel_index < usa_index


def test_counting_007(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO(u'Shanghai, China\nBeijing, China\nBeijing, China\n\n'))
    solution.collect_places()
    captured_out, captured_err = capsys.readouterr()
    assert len(solution.visits['China']) == 2

    solution.display_places()
    captured_out, captured_err = capsys.readouterr()
    assert 'Beijing (2)' in captured_out
    assert 'Shanghai' in captured_out
