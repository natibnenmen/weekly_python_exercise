#from __future__ import print_function
import logging
import sys

logger = logging.getLogger(__name__)

visits = {}
'''
{
    'country1': {'city1': 'counter', 'city2': 'counter'},
    'country2': {'city3': 'counter', 'city4': 'counter'}
}
'''

def collect_places():
    while True:
        raw_input_val = raw_input("Tell me where you went:")
        if raw_input_val == '': break
        logger.debug("input")
        input = [x.strip() for x in raw_input_val.split(',')]
        if len(input) != 2:
            #print(u"That's not a legal city, country combination", file=sys.stderr);
            print("That's not a legal city, country combination");
            continue
        # todo: more input validation here

        # todo: make this more elegant per: "https://stackoverflow.com/questions/1692388/python-list-of-dict-if-exists-increment-a-dict-value-if-not-append-a-new-dic"
        if input[1] in visits: # The first argument it the city and the second one is the country. However, in visit the high level key is the country.
            if input[0] in visits[input[1]]:
                visits[input[1]][input[0]] += 1;
            else:
                visits[input[1]][input[0]] = 1;
        else:
            visits[input[1]] = {input[0]: 1};

        logger.info(visits)

def display_places():
    print("You visited:")
    for country in sorted(visits.iterkeys()):
        print("\t%s" % country);
        for city in sorted(visits[country].iterkeys()):
            if visits[country][city] > 1:
                str = "\t\t{0} ({1})".format(city, visits[country][city]);
            else:
                str = "\t\t{0}".format(city);
            #print("\t\t{0} {1}".format(city, ('\(' + visits[country][city] + '\)') if (visits[country][city] > 1) else '' ));
            print (str);

if __name__ == '__main__':
    collect_places();
    display_places();

'''
You visited:
    China
        Beijing (2)
        Shanghai
    England
        London
    USA
        Boston
        Chicago (2)
        New York
'''