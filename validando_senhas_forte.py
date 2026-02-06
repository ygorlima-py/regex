#https://regex101.com/r/o2aCEx/1
import re

regex = re.compile(
    r'^'
    r'(?=.*[a-z])'
    r'(?=.*[A-Z])'
    r'(?=.*[0-9])'
    r'(?=.*[ -\/:-@[-`{-~])'
    r'.{6,}'
    r'$',
    flags=re.M
    )


string = '''
VÁLIDAS
&vs98#DG]Ir9
0~\14KPxzY}n
8isZKtV3;?$6
[#R03W4Mch/p
_exgBD,5}88G

SEM MINÚSCULAS
5T|4*LE~16V>
57S|RYG;3^]9
3~QK5BS[3 -0
D61R9#,UI{3!
O|/F8U/K72`5

SEM MINÚSCULAS E NÚMEROS
}WHZ{M'||JO@
%>;/|LWRCEA|
+D =RGB.CL]*
#UVVW(|G^^T{
$TQO|&|<M\GV

SEM NÚMEROS CARACTERES E MINÚSCULAS
YLTQSNLTQGVB
NGQIPAGNMAPH
ETHZIIOCJRVS
QDIAVFUFIXKS
IHXXRBGXOFTO

QUANTIDADE INVÁLIDA (6)
E3^7is
Mu45e}
8dP3?e
<yqR21
2\6njV

'''

print(regex.findall(string))
