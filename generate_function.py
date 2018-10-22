import time
import random
import execjs


def generate_d():
    timestamp = int(time.time() * 1000)
    g = [['834', '0'],
         ['868', '8'],
         ['939', '26'],
         ['988', '41'],
         ['1024', '53'],
         ['1060', '67'],
         ['1075', '74'],
         ['1090', '81'],
         ['1096', '84'],
         ['1100', '87'],
         ['1103', '89'],
         ['1104', '90'],
         ['1105', '93'],
         ['1105', '97'],
         ['1105', '102'],
         ['1105', '110'],
         ['1105', '120'],
         ['1103', '129'],
         ['1102', '136'],
         ['1099', '144'],
         ['1098', '148'],
         ['1096', '154'],
         ['1096', '158'],
         ['1096', '163'],
         ['1096', '169'],
         ['1098', '174'],
         ['1102', '181'],
         ['1107', '191'],
         ['1109', '196'],
         ['1107', '196'],
         ['1104', '197'],
         ['1094', '204'],
         ['1086', '210'],
         ['1078', '217'],
         ['1072', '223'],
         ['1065', '229'],
         ['1060', '234'],
         ['1051', '244'],
         ['1046', '250'],
         ['1039', '258'],
         ['1033', '267'],
         ['1027', '275'],
         ['1022', '283'],
         ['1022', '285'],
         ['1023', '290'],
         ['1025', '301'],
         ['1029', '316'],
         ['1032', '335'],
         ['1034', '349'],
         ['1038', '374'],
         ['1040', '388'],
         ['1042', '405'],
         ['1045', '417'],
         ['1046', '422'],
         ['1049', '439'],
         ['1051', '445'],
         ['1053', '456'],
         ['1054', '459'],
         ['1054', '460'],
         ['1054', '460'],
         ['1054', '460'],
         ['1055', '459'],
         ['1055', '457'],
         ['1056', '449'],
         ['1056', '444'],
         ['1058', '436'],
         ['1058', '433'],
         ['1059', '432'],
         ['1059', '432'],
         ['1059', '429']]
    for i in g:
        i.append(timestamp)
        timestamp += random.randrange(5, 25)

    obj = execjs.compile(open('./conver_trace.js').read())
    d = obj.call('gc', g)
    return d


def generate_eid():
    string = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for i in range(90):
        result += random.choice(string)
    return result
