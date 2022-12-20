from msilib.schema import Binary


def main():
    fin = open('report.txt')
    ones = []
    zeros = []


    for i in range(12):
        ones.append(0)
        zeros.append(0)

    for r in fin:
        for i in range(len(r)-1):
           # print(f"{i} {r[i]} ", end='')

            if r[i] == '0':
                zeros[i] += 1
                #print(f"Zeros: {zeros}")
            else:
                ones[i] += 1
                #print(f"Ones: {ones}")

    gama_string = ''
    epsilon_string = ''

    for i in range(len(zeros)):
        if zeros[i] > ones[i]:
            gama_string += '0'
            epsilon_string += '1'
        else:
            gama_string += '1'
            epsilon_string += '0'

    print(zeros)
    print(ones)
    print(gama_string)
    print(epsilon_string)

    report = read_report('report.txt')

    for i in range(12):
        if len(report) > 1:
            value = find_common_value(report, i)
            print(f"Value: {value}")
            report = filter_value(report, value, i)


    ox_value = int(report[0], base=2)

    report = read_report('report.txt')
    for i in range(12):
        if len(report) > 1:
            value = find_common_value(report, i)
            value = '1' if value == '0' else '0'
            print(f"Value: {value}")
            report = filter_value(report, value, i)

    co_value = int(report[0], base=2)

    print(co_value * ox_value)

    #print(int(o2_gen_rate, base=2) * int(co2_gen_rate, base=2))


def find_common_value(report, i):
    zeros = 0
    ones = 0

    for l in report:
        if l[i] == '0':
            zeros += 1
        else:
            ones += 1

    if zeros > ones:
        return '0'
    else:
        return '1'



def filter_value(diagnostic_report, value, position):
   # filter out values based on value variable
    diagnostic_report = list(filter(lambda x: True if x[position] == value else False, diagnostic_report))

    #print(diagnostic_report)
    return(diagnostic_report)

def read_report(report_name):
    #open file connection
    fin = open(report_name)
    #read in file lines and append to an array
    report = []
    for l in fin:
        report.append(l.replace('\n', ''))

    # return report as a list
    return report



if __name__ == '__main__':
    main()

#this is a test comment
