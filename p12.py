import requests
from bs4 import BeautifulSoup
url = 'https://www.rekhta.org/nazms/banjaara-naama-tuk-hirs-o-havaa-ko-chhod-miyaan-mat-des-bides-phire-maaraa-nazeer-akbarabadi-nazms'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
div = soup.find_all('div',class_='w')[0:13]
for i in div:
	for j in i.find_all('p'):
		print(j.text)

#Output:
'''
aaj ik aur baras biit gayā us ke baġhair
jis ke hote hue hote the zamāne mere
Tuk hirs-o-havā ko chhoḌ miyāñ mat des bides phire maarā
qazzāq ajal kā luuTe hai din raat bajā kar naqqārā
kyā badhiyā bhaiñsā bail shutur kyā gauneñ pallā sar-bhārā
kyā gehūñ chāñval moTh maTar kyā aag dhuāñ aur añgārā
sab ThāTh paḌā rah jāvegā jab laad chalegā banjārā
gar to hai lakkhī banjārā aur khep bhī terī bhārī hai
ai ġhāfil tujh se bhī chaḌhtā ik aur baḌā byopārī hai
kyā shakkar misrī qand garī kyā sāñbhar mīThā khārī hai
kyā daakh munaqqā soñTh mirach kyā kesar lauñg supārī hai
sab ThāTh paḌā rah jāvegā jab laad chalegā banjārā
tū badhiyā laade bail bhare jo pūrab pachchham jāvegā
yā suud baḌhā kar lāvegā yā TuuTā ghāTā pāvegā
qazzāq ajal kā raste meñ jab bhālā maar girāvegā
dhan daulat naatī potā kyā ik kumba kaam na āvegā
sab ThāTh paḌā rah jāvegā jab laad chalegā banjārā
har manzil meñ ab saath tire ye jitnā Derā-DāñDā hai
zar dām-diram kā bhāñDā hai bandūq sipar aur khāñDā hai
jab nāyak tan kā nikal gayā jo mulkoñ mulkoñ hāñDā hai
phir hāñDā hai na bhāñDā hai na halvā hai na māñDā hai
sab ThāTh paḌā rah jāvegā jab laad chalegā banjārā
jab chalte chalte raste meñ ye gaun tirī rah jāvegī
ik badhiyā terī miTTī par phir ghaas na charne āvegī
ye khep jo tū ne laadī hai sab hissoñ meñ baT jāvegī
dhī puut jañvā.ī beTā kyā banjāran paas na āvegī
sab ThāTh paḌā rah jāvegā jab laad chalegā banjārā
ye khep bhare jo jaatā hai ye khep miyāñ mat gin apnī
ab koī ghaḌī pal sā'at meñ ye khep badan kī hai kafanī
kyā thaal kaTorī chāñdī kī kyā pītal kī Dibyā-Dhaknī
kyā bartan sone chāñdī ke kyā miTTī kī hañDiyā chīnī
sab ThāTh paḌā rah jāvegā jab laad chale gā banjārā
ye dhūm-dhaḌakkā saath liye kyuuñ phirtā hai jangal jangal
ik tinkā saath na jāvegā mauqūf huā jab ann aur jal
ghar-bār aTārī chaupārī kyā ḳhāsā nain-sukh aur malmal
chalvan parde farsh na.e kyā laal palañg aur rañg-mahal
sab ThāTh paḌā rah jāvegā jab laad chalegā banjārā
kuchh kaam na āvegā tere ye lāl-o-zamurrad sīm-o-zar
jab pūñjī baaT meñ bikhregī har aan banegī jaan uupar
naubat naqqāre baan nishān daulat hashmat faujeñ lashkar
kyā masnad takiya mulk makāñ kyā chaukī kursī taḳht chhatar
sab ThāTh paḌā rah jāvegā jab laad chalegā banjārā
kyuuñ jī par bojh uThātā hai in gaunoñ bhārī bhārī ke
jab maut kā Derā aan paḌā phir duune haiñ byopārī ke
kyā saaz jaḌāo zar-zevar kyā goTe thaan kanārī ke
kyā ghoḌe ziin sunahrī ke kyā hāthī laal amārī ke
sab ThāTh paḌā rah jāvegā jab laad chalegā banjārā
mafrūr na ho talvāroñ par mat phuul bharose Dhāloñ ke
sab paTTā toḌ ke bhāgeñge muñh dekh ajal ke bhāloñ ke
kyā Dabbe motī hīroñ ke kyā Dher ḳhazāne māloñ ke
kyā buġhche taash moshajjar ke kyā taḳhte shaal doshāloñ ke
sab ThāTh paḌā rah jāvegā jab laad chalegā banjārā
kyā saḳht makāñ banvātā hai ḳham tere tan kā hai polā
tū ūñche coat uThātā hai vaañ gor gaḌhe ne muñh kholā
kyā renī ḳhandaq rand baḌe kyā brij kañgūrā anmolā
gaḌ.h coat rahakla top qila kyā shīsha daarū aur golā
sab ThāTh paḌā rah jāvegā jab laad chalegā banjārā
har aan naf.a aur ToTe meñ kyuuñ martā phirtā hai ban ban
Tak ġhāfil dil meñ soch zarā hai saath lagā tere dushman
kyā lauñDī bāñdī daa.ī davā kyā bandā chelā nek-chalan
kyā mandar masjid taal kuaañ kyā khetī baaḌī phuul chaman
sab ThāTh paḌā rah jāvegā jab laad chalegā banjārā

(scrap) D:\scrap_project>python p12.py
aaj ik aur baras biit gayā us ke baġhair
jis ke hote hue hote the zamāne mere
Tuk hirs-o-havā ko chhoḌ miyāñ mat des bides phire maarā
qazzāq ajal kā luuTe hai din raat bajā kar naqqārā
kyā badhiyā bhaiñsā bail shutur kyā gauneñ pallā sar-bhārā
kyā gehūñ chāñval moTh maTar kyā aag dhuāñ aur añgārā
sab ThāTh paḌā rah jāvegā jab laad chalegā banjārā
gar to hai lakkhī banjārā aur khep bhī terī bhārī hai
ai ġhāfil tujh se bhī chaḌhtā ik aur baḌā byopārī hai
kyā shakkar misrī qand garī kyā sāñbhar mīThā khārī hai
kyā daakh munaqqā soñTh mirach kyā kesar lauñg supārī hai
sab ThāTh paḌā rah jāvegā jab laad chalegā banjārā
tū badhiyā laade bail bhare jo pūrab pachchham jāvegā
yā suud baḌhā kar lāvegā yā TuuTā ghāTā pāvegā
qazzāq ajal kā raste meñ jab bhālā maar girāvegā
dhan daulat naatī potā kyā ik kumba kaam na āvegā
sab ThāTh paḌā rah jāvegā jab laad chalegā banjārā
har manzil meñ ab saath tire ye jitnā Derā-DāñDā hai
zar dām-diram kā bhāñDā hai bandūq sipar aur khāñDā hai
jab nāyak tan kā nikal gayā jo mulkoñ mulkoñ hāñDā hai
phir hāñDā hai na bhāñDā hai na halvā hai na māñDā hai
sab ThāTh paḌā rah jāvegā jab laad chalegā banjārā
jab chalte chalte raste meñ ye gaun tirī rah jāvegī
ik badhiyā terī miTTī par phir ghaas na charne āvegī
ye khep jo tū ne laadī hai sab hissoñ meñ baT jāvegī
dhī puut jañvā.ī beTā kyā banjāran paas na āvegī
sab ThāTh paḌā rah jāvegā jab laad chalegā banjārā
ye khep bhare jo jaatā hai ye khep miyāñ mat gin apnī
ab koī ghaḌī pal sā'at meñ ye khep badan kī hai kafanī
kyā thaal kaTorī chāñdī kī kyā pītal kī Dibyā-Dhaknī
kyā bartan sone chāñdī ke kyā miTTī kī hañDiyā chīnī
sab ThāTh paḌā rah jāvegā jab laad chale gā banjārā
ye dhūm-dhaḌakkā saath liye kyuuñ phirtā hai jangal jangal
ik tinkā saath na jāvegā mauqūf huā jab ann aur jal
ghar-bār aTārī chaupārī kyā ḳhāsā nain-sukh aur malmal
chalvan parde farsh na.e kyā laal palañg aur rañg-mahal
sab ThāTh paḌā rah jāvegā jab laad chalegā banjārā
kuchh kaam na āvegā tere ye lāl-o-zamurrad sīm-o-zar
jab pūñjī baaT meñ bikhregī har aan banegī jaan uupar
naubat naqqāre baan nishān daulat hashmat faujeñ lashkar
kyā masnad takiya mulk makāñ kyā chaukī kursī taḳht chhatar
sab ThāTh paḌā rah jāvegā jab laad chalegā banjārā
kyuuñ jī par bojh uThātā hai in gaunoñ bhārī bhārī ke
jab maut kā Derā aan paḌā phir duune haiñ byopārī ke
kyā saaz jaḌāo zar-zevar kyā goTe thaan kanārī ke
kyā ghoḌe ziin sunahrī ke kyā hāthī laal amārī ke
sab ThāTh paḌā rah jāvegā jab laad chalegā banjārā
mafrūr na ho talvāroñ par mat phuul bharose Dhāloñ ke
sab paTTā toḌ ke bhāgeñge muñh dekh ajal ke bhāloñ ke
kyā Dabbe motī hīroñ ke kyā Dher ḳhazāne māloñ ke
kyā buġhche taash moshajjar ke kyā taḳhte shaal doshāloñ ke
sab ThāTh paḌā rah jāvegā jab laad chalegā banjārā
kyā saḳht makāñ banvātā hai ḳham tere tan kā hai polā
tū ūñche coat uThātā hai vaañ gor gaḌhe ne muñh kholā
kyā renī ḳhandaq rand baḌe kyā brij kañgūrā anmolā
gaḌ.h coat rahakla top qila kyā shīsha daarū aur golā
sab ThāTh paḌā rah jāvegā jab laad chalegā banjārā
har aan naf.a aur ToTe meñ kyuuñ martā phirtā hai ban ban
Tak ġhāfil dil meñ soch zarā hai saath lagā tere dushman
kyā lauñDī bāñdī daa.ī davā kyā bandā chelā nek-chalan
kyā mandar masjid taal kuaañ kyā khetī baaḌī phuul chaman
sab ThāTh paḌā rah jāvegā jab laad chalegā banjārā
'''