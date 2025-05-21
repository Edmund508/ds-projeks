# Datu struktūras un algoritmi kursa noslēguma projekts
Programmatūra sūdzību nolasīšanai no vietnes sudzibas.lv
## Projekta uzdēvums
Projekta uzdevums bija izveidot programmatūru, kas automātiski savāc sūdzības par konkrētu organizāciju vai personu no vietnes sudzibas.lv. Programmatūras lietošanas laikā lietotājam jābūt iespējai pašam izvēlēties kategoriju no vietnēs pieejamajām un ievadīt organizācijas vai personas nosaukumu. Katrai atrastai sudzībai ir jāizveido .txt failu, kura būs ierakstīta sudzību informācija - tēma, sudzības apraksts un datums. Katram failam jābut unikālam nosaukumam, kas sakritīs as personālu ID sudzībai vietne.
## Izmantotas bibliotēkas
### Requests HTTP Library
Bibliotēka Requests tiek izmantota lai nolasīt vietnes kodu turpmakai apstrādei.
### Beautiful Soup
Bibliotēka Beautiful Soup tiek izmantota lai apstradātu vietnes kodu un nolasīt no ta nepieciešamo informāciju.
## Projekta definētas datu struktūras
### List
Koda dažādam nolukam tiek izveidoti dažādi saraksti. 
Tie ir izmantoti lai:
    1. Atrāst visas sudzības uz vienas lapas.
    2. Parbaudīt, vai ir nākāma lapa.
    3. Saņemt sudzības ID no href.
## Programmatūras izmantošana
https://youtu.be/W7JNk9NC7NQ