import itertools
import datetime
import os
import sys


def parse_date(str_date):
    parts = map(int, str_date.split('/'))
    possible_dates = []
    for year, month, day in itertools.permutations(parts, 3):
        if year in range(0, 99):
            year += 2000
        if year < 2000 or year > 2999:
            continue  # wrong combination
        try:
            possible_dates.append(datetime.date(year, month, day))
        except ValueError: 
            continue
    if not possible_dates:
        return str_date + " is illegal"
    possible_dates.sort()
    return possible_dates[0].strftime('%Y-%m-%d')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Please define input file name as first argument and output as" \
              " second"
        sys.exit(1)
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    if not os.path.isfile(input_file_name):
        print 'File {} does not exists'.format(input_file_name)
        sys.exit(1)
    output = file(output_file_name, 'w')
    with file(input_file_name, 'r') as input_file:
        for line in input_file:
            output.write('{}\n'.format(parse_date(line)))
    output.close()
    print "Done. Results are stored in {}".format(output_file_name)