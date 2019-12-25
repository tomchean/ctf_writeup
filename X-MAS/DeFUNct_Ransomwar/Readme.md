# Solution
from key.txt find n and e
```
n = 795569463642685540507503580717531982215679866156448758181874864294322245115046429295501396806569726084791213843313411985306755767933614251017259685360119715465741448841742926933764058184678978561438979554324014291467144646477238464467422645352253054043072408503415623126059018449111807300294890437634529289983603557882115343971407081044050231310858245171002149317227947666679143716043142141154344524386085333349328691743473103727587822968025700198172293605188589348169121979328380110985341428872278372426313622759225108517531628814853640680656657769539723198346005032762702856464738405070059566116940640592020837592563966093405895649052241416909627641069000138027201809936286028443581259045590752809132011594533609186039058798304319124598876514669458750171121861029071117458575853963148168447032328126766812085206373608016609150982512467597800331177524543178311636877811255184421602626713179220562081413985985692847372669113031244726086691179028200044542399429299315486513734144695492816493025225952668485937918985944213972980220480476191347009337324778384697829597183756976186825413917475597248616769321954150777672675555280228376126308362907381766363071890237458517881243184612898247096962136202978853341989193954815333784856612689
e = 13337
```
accoring rsa principle, find phi and d
```
def totient(n):
    factors = sympy.factorint(n)
    phi = 1
    for i,j in factors.items():
        phi *= (pow(i,j) - pow(i,j-1))
    return phi
phi = totient(n)
#phi = 795569463642685540507503580717531982215679866156448758181874864294322245115046429295501396806569726084791213843313411985306755767933614251017259685360119715465741448841742926933764058184678978561438979554324014291467144646477238464467422645352253054043072408503415623126059018449111807300294890437634529289974129444571536738052570355117041655957194797795932221088165512417385741652358788534138109677638428769384923912855674834081924263955235117285222418082095493531450824685078351263802277062074247864049889090769102738157321783125317563334972475927126639159045005010465255142270934345377339994304284391870997274086299657145887645914183207352738211747434113585868854466417725818033061437465667753585246998223876165557439167293956794262865991380668462719740982987724541500400391567701961940918159642386316128764963374724640309606761513868077290881541455948690259950121789131017262290159942490351322990758776243445625723997047941366665514450305070398888439416362632425588719735162357397479016945380129467671413842072119104000322860831477225418789147099598909139373946098302763513794437681341662578817402330966245646491800413245804870825457441490580402787793311420882850111520005066977852056917452397335125352731022949725920358513273392
d = gmpy2.invert(e, phi)
#d = 7947443900524080191446418200358964894514983896595100917345619492485351014389010789773809219193783476885894363853986839609634323382094519020045017872183892389199029691695425209960304681655760875600420216555449611351057322449998167403127238784464235940520723908120900740270593708738216059614921653939858820884570784133348078569567408195409942197024357650215243834952970787234564579228696916327118249282619782509563249974433386635864110475706385437679778847626962613679407222981079161367874254774380669773556113596975833849765492081560428806779995911549969370859406030380441549344595800788002719550696181409025832199872837747135601303973069391407073831392878046636924273364167788348975547748266210646095491571088300505759549576117346943062604622258200178886908155195598496187856561008219352702078288430556428239639338779175180953310520039842761612618360251012177164137360557331509685869582782421599486453168672995255112754229040993031774366604253249979366988203302275085602294754186912098713790531166873053644862314045105253694994187994721761839377636465577626666568155763150460347189523338307711960573939225206219655060079369394286413391401284211818353269597162262100913482480941739344161165063870167524617918897779369420501512993545

```
read the file memos.enc
```
with open('memos.enc', 'r') as f:
    cipher = f.read()
    cipher = int(cipher, 16)
```
decode the cipher by d and n
```
plaintext = pow(cipher, d, n)
plaintext = str(hex(plaintext))[2:]
plaintext = bytearray.fromhex(plaintext).decode()
```
get the flag

**X-MAS{yakuhito_should_n0t_b3_0n_th3_n@ughty_l1st_941282a75d89e080}**