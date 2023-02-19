import Crypto.Util.number as cun

while True:
    p = cun.getPrime(1024)
    q = p + 2
    if cun.isPrime(q):
        break

n = p * q
e = 0x10001

phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)

FLAG = cun.bytes_to_long(b"buckeye{?????????????????????????????????????????????????????????????}")
c = pow(FLAG, e, n)
assert pow(c, d, n) == FLAG

print(FLAG)
print(f"n = {n}")
print(f"c = {c}")

"""
Output:
n = 20533399299284046407152274475522745923283591903629216665466681244661861027880216166964852978814704027358924774069979198482663918558879261797088553574047636844159464121768608175714873124295229878522675023466237857225661926774702979798551750309684476976554834230347142759081215035149669103794924363457550850440361924025082209825719098354441551136155027595133340008342692528728873735431246211817473149248612211855694673577982306745037500773163685214470693140137016315200758901157509673924502424670615994172505880392905070519517106559166983348001234935249845356370668287645995124995860261320985775368962065090997084944099
c = 786123694350217613420313407294137121273953981175658824882888687283151735932871244753555819887540529041840742886520261787648142436608167319514110333719357956484673762064620994173170215240263058130922197851796707601800496856305685009993213962693756446220993902080712028435244942470308340720456376316275003977039668016451819131782632341820581015325003092492069871323355309000284063294110529153447327709512977864276348652515295180247259350909773087471373364843420431252702944732151752621175150127680750965262717903714333291284769504539327086686569274889570781333862369765692348049615663405291481875379224057249719713021
"""
