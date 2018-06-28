import ipaddress
import os

a32 = '1.0.0.0/32'
a31 = '1.0.0.0/31'
a30 = '1.0.0.0/30'
a29 = '1.0.0.0/29'
a28 = '1.0.0.0/28'
a27 = '1.0.0.0/27'
a26 = '1.0.0.0/26'
a25 = '1.0.0.0/25'
a24 = '1.0.0.0/24'
a23 = '1.0.0.0/23'
a22 = '1.0.0.0/22'
a21 = '1.0.0.0/21'
a20 = '1.0.0.0/20'
a19 = '1.0.0.0/19'
a18 = '1.0.0.0/18'
a17 = '1.0.0.0/17'
a16 = '1.0.0.0/16'
a15 = '1.0.0.0/15'
a14 = '1.0.0.0/14'
a13 = '1.0.0.0/13'
a12 = '1.0.0.0/12'
a11 = '1.0.0.0/11'
a10 = '1.0.0.0/10'
a9 = '1.0.0.0/9'
a8 = '1.0.0.0/8'
a7 = '1.0.0.0/7'
a6 = '1.0.0.0/6'
a5 = '1.0.0.0/5'
a4 = '1.0.0.0/4'
a3 = '1.0.0.0/3'
a2 = '1.0.0.0/2'
a1 = '1.0.0.0/1'
a0 = '1.0.0.0/0'

zone = input('Insert zone name: ')

k = int(input('1. '
              '\n' 'alebo 2. '
              '\n' 'alebo 3.: '))

if k == 1:
    k = ' int-'
elif k == 2:
    k = ' ext-'
elif k == 3:
    k = ' '
else:
    print('nope')
    exit('becase')
print(k)

comment = input('Insert comment: ')

with open("hosts.txt", "r", encoding='utf-8') as h:
    with open('IPS.txt', 'w', encoding='utf-8') as out:
        with open('object_group.txt', 'w', encoding='utf-8') as group:

            for x in h:
                x = x.rstrip(os.linesep)
                # x = ipaddress.ip_network(x).netmask
                #  print(str(ipaddress.ip_network(x)) + '\n', end='')


                if ipaddress.ip_network(x).netmask == ipaddress.ip_network(a32).netmask:
                    ip_address_name = str(k) + str(x.strip('/32')) + '-cidr32 '
                    out.write('set address ' + zone + str(k) + str(x.strip('/32')) + '-cidr32 ' + str(x.strip('/32')) + ' 255.255.255.255' + ' \'' + comment + '\'' + '\n')
                    group.write('set group address '+ zone + str(x.strip('/32')) + '-cidr32 '  + 'engineering add QA_lab comment "Engineering Team"')
                    print('ok')


                elif ipaddress.ip_network(x).netmask == ipaddress.ip_network(a31).netmask:
                    out.write('IP address ' + str(x) + ' is unusable. You need to check it.')
                    print('IP address ' + str(x) + ' is unusable. You need to check it.')
                elif ipaddress.ip_network(x).netmask == ipaddress.ip_network(a30).netmask:
                    out.write('set address ' + zone + str(k) + str(x.strip('/30')) + '-cidr30 ' + str(x.strip('/30')) + ' 255.255.255.252' + ' \'' + comment + '\'' + '\n')
                    print('set address ' + zone + str(k) + str(x.strip('/30')) + '-cidr30 ' + str(x.strip('/30')) + ' 255.255.255.252' + ' \'' + comment + '\'')
                elif ipaddress.ip_network(x).netmask == ipaddress.ip_network(a29).netmask:
                    out.write('set address ' + zone + str(k) + str(x.strip('/29')) + '-cidr29 ' + str(x.strip('/29')) + ' 255.255.255.248' + ' \'' + comment + '\'' + '\n')
                    print('set address ' + zone + str(k) + str(x.strip('/29')) + '-cidr29 ' + str(x.strip('/29')) + ' 255.255.255.248' + ' \'' + comment + '\'')
                elif ipaddress.ip_network(x).netmask == ipaddress.ip_network(a28).netmask:
                    out.write('set address ' + zone + str(k) + str(x.strip('/28')) + '-cidr28 ' + str(x.strip('/28')) + ' 255.255.255.240' + ' \'' + comment + '\'' + '\n')
                    print('set address ' + zone + str(k) + str(x.strip('/28')) + '-cidr28 ' + str(x.strip('/28')) + ' 255.255.255.240' + ' \'' + comment + '\'')
                elif ipaddress.ip_network(x).netmask == ipaddress.ip_network(a27).netmask:
                    out.write('set address ' + zone + str(k) + str(x.strip('/27')) + '-cidr27 ' + str(x.strip('/27')) + ' 255.255.255.224' + ' \'' + comment + '\'' + '\n')
                    print('set address ' + zone + str(k) + str(x.strip('/27')) + '-cidr27 ' + str(x.strip('/27')) + ' 255.255.255.224' + ' \'' + comment + '\'')
                elif ipaddress.ip_network(x).netmask == ipaddress.ip_network(a26).netmask:
                    out.write('set address ' + zone + str(k) + str(x.strip('/26')) + '-cidr26 ' + str(x.strip('/26')) + ' 255.255.255.192' + ' \'' + comment + '\'' + '\n')
                    print('set address ' + zone + str(k) + str(x.strip('/26')) + '-cidr26 ' + str(x.strip('/26')) + ' 255.255.255.192' + ' \'' + comment + '\'')
                elif ipaddress.ip_network(x).netmask == ipaddress.ip_network(a25).netmask:
                    out.write('set address ' + zone + str(k) + str(x.strip('/25')) + '-cidr25 ' + str(x.strip('/26')) + ' 255.255.255.128' + ' \'' + comment + '\'' + '\n')
                    print('set address ' + zone + str(k) + str(x.strip('/25')) + '-cidr25 ' + str(x.strip('/26')) + ' 255.255.255.128' + ' \'' + comment + '\'')


                elif ipaddress.ip_network(x).netmask == ipaddress.ip_network(a24).netmask:
                    out.write('set address ' + zone + str(k) + str(x.strip('/24')) + '-cidr24 ' + str(x.strip('/24')) + ' 255.255.255.0' + ' \'' + comment + '\'' + '\n')
                    print('set address ' + zone + str(k) + str(x.strip('/24')) + '-cidr24 ' + str(x.strip('/24')) + ' 255.255.255.0' + ' \'' + comment + '\'')
                elif ipaddress.ip_network(x).netmask == ipaddress.ip_network(a23).netmask:
                    out.write('set address ' + zone + str(k) + str(x.strip('/23')) + '-cidr23 ' + str(x.strip('/23')) + ' 255.255.254.0' + ' \'' + comment + '\'' + '\n')
                    print('set address ' + zone + str(k) + str(x.strip('/23')) + '-cidr23 ' + str(x.strip('/23')) + ' 255.255.254.0' + ' \'' + comment + '\'')
                elif ipaddress.ip_network(x).netmask == ipaddress.ip_network(a22).netmask:
                    out.write('set address ' + zone + str(k) + str(x.strip('/22')) + '-cidr22 ' + str(x.strip('/22')) + ' 255.255.252.0' + ' \'' + comment + '\'' + '\n')
                    print('set address ' + zone + str(k) + str(x.strip('/22')) + '-cidr22 ' + str(x.strip('/22')) + ' 255.255.252.0' + ' \'' + comment + '\'')
                elif ipaddress.ip_network(x).netmask == ipaddress.ip_network(a21).netmask:
                    out.write('set address ' + zone + str(k) + str(x.strip('/21')) + '-cidr21 ' + str(x.strip('/21')) + ' 255.255.248.0' + ' \'' + comment + '\'' + '\n')
                    print('set address ' + zone + str(k) + str(x.strip('/21')) + '-cidr21 ' + str(x.strip('/21')) + ' 255.255.248.0' + ' \'' + comment + '\'')
                elif ipaddress.ip_network(x).netmask == ipaddress.ip_network(a20).netmask:
                    out.write('set address ' + zone + str(k) + str(x.strip('/20')) + '-cidr20 ' + str(x.strip('/20')) + ' 255.255.240.0' + ' \'' + comment + '\'' + '\n')
                    print('set address ' + zone + str(k) + str(x.strip('/20')) + '-cidr20 ' + str(x.strip('/20')) + ' 255.255.240.0' + ' \'' + comment + '\'')
                elif ipaddress.ip_network(x).netmask == ipaddress.ip_network(a19).netmask:
                    out.write('set address ' + zone + str(k) + str(x.strip('/19')) + '-cidr19 ' + str(x.strip('/19')) + ' 255.255.224.0' + ' \'' + comment + '\'' + '\n')
                    print('set address ' + zone + str(k) + str(x.strip('/19')) + '-cidr19 ' + str(x.strip('/19')) + ' 255.255.224.0' + ' \'' + comment + '\'')
                elif ipaddress.ip_network(x).netmask == ipaddress.ip_network(a18).netmask:
                    out.write('set address ' + zone + str(k) + str(x.strip('/18')) + '-cidr18 ' + str(x.strip('/18')) + ' 255.255.192.0' + ' \'' + comment + '\'' + '\n')
                    print('set address ' + zone + str(k) + str(x.strip('/18')) + '-cidr18 ' + str(x.strip('/18')) + ' 255.255.192.0' + ' \'' + comment + '\'')
                elif ipaddress.ip_network(x).netmask == ipaddress.ip_network(a17).netmask:
                    out.write('set address ' + zone + str(k) + str(x.strip('/17')) + '-cidr17 ' + str(x.strip('/17')) + ' 255.255.128.0' + ' \'' + comment + '\'' + '\n')
                    print('set address ' + zone + str(k) + str(x.strip('/17')) + '-cidr17 ' + str(x.strip('/17')) + ' 255.255.128.0' + ' \'' + comment + '\'')
                elif ipaddress.ip_network(x).netmask == ipaddress.ip_network(a16).netmask:
                    out.write('set address ' + zone + str(k) + str(x.strip('/16')) + '-cidr16 ' + str(x.strip('/16')) + ' 255.255.0.0' + ' \'' + comment + '\'' + '\n')
                    print('set address ' + zone + str(k) + str(x.strip('/16')) + '-cidr16 ' + str(x.strip('/16')) + ' 255.255.0.0' + ' \'' + comment + '\'')


                elif ipaddress.ip_network(x).netmask == ipaddress.ip_network(a15).netmask:
                    out.write('set address ' + zone + str(k) + str(x.strip('/15')) + '-cidr15 ' + str(x.strip('/15')) + ' 255.254.0.0' + ' \'' + comment + '\'' + '\n')
                    print('ok')
                elif ipaddress.ip_network(x).netmask == ipaddress.ip_network(a14).netmask:
                    out.write('set address ' + zone + str(k) + str(x.strip('/14')) + '-cidr14 ' + str(x.strip('/14')) + ' 255.252.0.0' + ' \'' + comment + '\'' + '\n')
                    print('ok')
                elif ipaddress.ip_network(x).netmask == ipaddress.ip_network(a13).netmask:
                    out.write('set address ' + zone + str(k) + str(x.strip('/13')) + '-cidr13 ' + str(x.strip('/13')) + ' 255.248.0.0' + ' \'' + comment + '\'' + '\n')
                    print('ok')
                elif ipaddress.ip_network(x).netmask == ipaddress.ip_network(a12).netmask:
                    out.write('set address ' + zone + str(k) + str(x.strip('/12')) + '-cidr12 ' + str(x.strip('/12')) + ' 255.240.0.0' + ' \'' + comment + '\'' + '\n')
                    print('ok')
                elif ipaddress.ip_network(x).netmask == ipaddress.ip_network(a11).netmask:
                    out.write('set address ' + zone + str(k) + str(x.strip('/11')) + '-cidr11 ' + str(x.strip('/11')) + ' 255.224.0.0' + ' \'' + comment + '\'' + '\n')
                    print('ok')
                elif ipaddress.ip_network(x).netmask == ipaddress.ip_network(a10).netmask:
                    out.write('set address ' + zone + str(k) + str(x.strip('/10')) + '-cidr10 ' + str(x.strip('/10')) + ' 255.192.0.0' + ' \'' + comment + '\'' + '\n')
                    print('ok')
                elif ipaddress.ip_network(x).netmask == ipaddress.ip_network(a9).netmask:
                    out.write('set address ' + zone + str(k) + str(x.strip('/9')) + '-cidr9 ' + str(x.strip('/9')) + ' 255.128.0.0' + ' \'' + comment + '\'' + '\n')
                    print('ok')
                elif ipaddress.ip_network(x).netmask == ipaddress.ip_network(a8).netmask:
                    out.write('set address ' + zone + str(k) + str(x.strip('/8')) + '-cidr8 ' + str(x.strip('/8')) + ' 255.0.0.0' + ' \'' + comment + '\'' + '\n')
                    print('ok')


                else:
                    print('dhfsjhfkjsdhfkhfoiashflsih')
