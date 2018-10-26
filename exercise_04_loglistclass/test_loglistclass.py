import solution
import operator
import pytest

logfilename = 'mini-access-log.txt'

@pytest.mark.nbm
def test_001_dicts_returns_list_of_dicts():
    ld = solution.LogDicts(logfilename)
    result = ld.dicts()
    assert type(result) == list
    assert all([type(one_item) == dict
                for one_item in result])

@pytest.mark.nbm
def test_002_iterdicts_returns_iterator_dicts():
    ld = solution.LogDicts(logfilename)
    result = ld.iterdicts()
    assert iter(result) == result

    result_list = list(result)
    assert type(result_list) == list

    assert all([type(one_item) == dict
                for one_item in result])

@pytest.mark.nbm
def test_003_sort_by_ip_address():
    ld = solution.LogDicts(logfilename)
    sorted_ld = ld.dicts(key=operator.itemgetter('ip_address'))

    assert sorted_ld[0]['ip_address'] <= sorted_ld[1]['ip_address']
    assert sorted_ld[0]['ip_address'] <= sorted_ld[-1]['ip_address']
    assert sorted_ld[-2]['ip_address'] <= sorted_ld[-1]['ip_address']

@pytest.mark.nbm
def test_005_sort_by_request():
    ld = solution.LogDicts(logfilename)
    sorted_ld = ld.dicts(key=operator.itemgetter('request'))

    assert sorted_ld[0]['request'] <= sorted_ld[1]['request']
    assert sorted_ld[0]['request'] <= sorted_ld[-1]['request']
    assert sorted_ld[-2]['request'] <= sorted_ld[-1]['request']

@pytest.mark.nbm
def test_006_earliest():
    ld = solution.LogDicts(logfilename)
    earliest = ld.earliest()

    sorted_ld = ld.dicts(key=operator.itemgetter('timestamp'))
    assert sorted_ld[0]['timestamp'] == earliest['timestamp']

@pytest.mark.nbm
def test_007_latest():
    ld = solution.LogDicts(logfilename)
    latest = ld.latest()

    sorted_ld = ld.dicts(key=operator.itemgetter('timestamp'))
    assert sorted_ld[-1]['timestamp'] == latest['timestamp']

@pytest.mark.nbm
def test_008_for_ip():
    ld = solution.LogDicts(logfilename)
    matching_requests = ld.for_ip("65.55.106.183")
    assert len(matching_requests) == 2
    assert all([one_item['ip_address'] == '65.55.106.183'
                for one_item in matching_requests])


@pytest.mark.nbm
def test_009_for_request():
    ld = solution.LogDicts(logfilename)
    matching_requests = ld.for_request("/robots.txt")
    assert len(matching_requests) == 16
    assert all(['/robots.txt' in one_item['request']
                for one_item in matching_requests])
