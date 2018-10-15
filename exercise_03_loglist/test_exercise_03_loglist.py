#!/usr/bin/env python3

import solution

logfilename = 'mini-access-log.txt'

def test_001_read_logs():
    log_list = solution.logtolist(logfilename)
    assert len(log_list) == 206

def test_011_got_a_list():
    log_list = solution.logtolist(logfilename)
    assert type(log_list) is list

def test_012_all_are_dicts():
    log_list = solution.logtolist(logfilename)
    assert all([type(x) is dict
                for x in log_list])

def test_002_check_keys():
    log_list = solution.logtolist(logfilename)
    assert set(log_list[0].keys()) == {'ip_address', 'timestamp', 'request'}

def test_003_check_values():
    log_list = solution.logtolist(logfilename)
    first_log_dict = log_list[0]

    assert first_log_dict['ip_address'] == '67.218.116.165'
    assert first_log_dict['timestamp'] == '30/Jan/2010:00:03:18 +0200'
    assert first_log_dict['request'] == 'GET /robots.txt HTTP/1.0'
