# https://leetcode.com/problems/substring-with-largest-variance/description/
import time


''' fast_solution
class Solution:
    def largestVariance(self, s: str) -> int:
        res = 0
        chars = list(set(s))

        for i in range(len(chars)):
            for j in range(i + 1, len(chars)):
                c1, c2 = chars[i], chars[j]

                diff = 0
                maxdiff = mindiff = 0
                lastc1diff = lastc2diff = 0
                meetc1 = meetc2 = False

                for c in s:
                    if c == c1:
                        meetc1 = True
                        diff += 1
                        maxdiff = max(lastc1diff, maxdiff)
                        lastc1diff = diff
                    elif c == c2:
                        meetc2 = True
                        diff -= 1
                        mindiff = min(lastc2diff, mindiff)
                        lastc2diff = diff
                    else:
                        continue
                    if meetc1 and meetc2:
                        res = max(maxdiff - diff, diff - mindiff, res)
        return res
'''

class Solution:

    def _logic(self, inc: str, dec: str, s: str) -> int:
        loc = 0
        count1, other1 = 0, 0
        count2, other2 = 0, 0
        for idx in range(len(s)):
            count1 += (s[idx] == inc)
            other1 += (s[idx] == dec)
            variance1 = count1 - other1 if other1 != 0 else 0
            if variance1 < 0:
                count1, other1 = 0, 0

            count2 += (s[idx] == dec)
            other2 += (s[idx] == inc)
            variance2 = count2 - other2 if other2 != 0 else 0
            if variance2 < 0:
                count2, other2 = 0, 0

            loc = max(loc, variance1, variance2)

        if count1 > 0 and other1 == 0:
            loc = max(loc, count1 - 1)
        if count2 > 0 and other2 == 0:
            loc = max(loc, count2 - 1)
        return loc

    def largestVariance(self, s: str) -> int:
        rlt = 0
        vault = list(set(s))
        if len(vault) < 2:          # case 'bbb'
            return 0
        for idx in range(len(vault)):
            for jdx in range(idx + 1, len(vault)):
                rlt = max(rlt, self._logic(vault[idx], vault[jdx], s))

        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', ("aababbb",), 3),
        ('test_01', ("lripaa",), 1),
        ('test_02', ("abb",), 1),
        ('test_03', ("bab",), 1),
        ('test_04', ("bba",), 1),
        ('test_05', ("abbaaabzaabaaaaaaaaaaaaa",), 18),
        ('test_06', ("eclxprpsikqrrejlmrssdmyutotguuxnftfwzlidgesnhtqdtmhkdhmqfltxcsctrgdjmmkboazjwfgdpiiqoacvrhhxbbqspfnkvhjztompwicltxoyssjhuiuamqpdrhvcetfmczldpozxebprmpwtcpcunmtiomzgwwylonkonomlgasxhbssjohlatvpjkuoighojbdepxtpfqudbjmjugggyiggvoascelgoknsjqnltxlicopzlkfyqgaejmugariqpnuymkskoazesdbjhdhgapmglcqcyglcqnbndbepfavzssgkxsxfwl",), 14),
        ('test_97', ("fzvpszwyavklghcedpgnygnqmxotgpcowkzvinkthpsmuvdhdmbcgaeeeqqdqocxesblxpkdpzeutiawmxqctnhemffgivsvdsledgsrybsflgzptfcjulnwiuownzpdoyncrhtcvdrgwtqogceftgrocjbtfvivzdlnzbjegniwnndepuuoqxtiydjkoyngqvmshmmawiapqhibbfwijlqagssoamnrvlgkyatyijdairipcacoxgpknahwhkcwzcwxtrqhhsyluiahgyfmfbjxxumaackpwkkaxcmvgupfnbqalrmpcwarkeztxvcbafwzmivecrjvorywnvjjoefebxmxfpsbszeeywncmultdlcortdohtkvbngtxonkmfbrgfanyzhfmcaavppctcqapehicqryqtvwafifkergimfqefbwrfumrezjnphjmgrtwjsezttksstnwwouleqovmkzmcofkieemptajedhmqwbybzsfgzjjxdnmgwhgwevldrmnnafhjzrbtczldfsdngompxbuyhtiznnvhtawueiuezuhnvhyfshtkcsjmgpelotpmiwunnrukeniouuqlprydcjlowvuwirdrfstvlgpbzaixgynjxumffsswjjtiiseyfcdlbvszoqizdtzfmiwpctrritnlpqxrqqjhtgvqdgiqducskrwqlivqrhpgwnvqydgpvihdffjuuopwaacmrknutjgjbckovgioifdevlayynjshmprmqgjdpmijwkhwhdvgbayeuccvstdlxzdxjtyexsdedarlqdnxlxeblfwirkxtebqkqgoogngyzauqeltsqteskucoqmdhndzlyanzswxdhzhfsdktuwhagnzlifatnnwccaddapuuvzmkcyhzgvwljqenrplbgnqpbnsswptstxospqkootogdwynhlthxqncmoixbbtvgyvqfcpawayfxtcnvimzlijvservsctwktykkzpbytlmdcwbzztgdsbtfzmrxzijoshsbjcjpvrwgimlgiqgfuvydhzwurfifotzpihdlnmhafsjpvnfizacilwwzrvahztliynxafirnbosvvmmisvktlckagiaaqswezavoxapzfolsmxhrqwxhrsgopnbtjgyivhkcrlcjiuuuaywmvefkntliexntpfsnmgllulffxvnpoffxaaykozqufiegagdtmootlrzkvsheexacneunbpvcficounhhyiavhyzyblfcyykwtamjglseibxxwfzpwphafmspclzdbfixzythluoiehivxdqnhmfhekmxfgpfaapmknwiukvabvkcysbtllgkxvkliqqgmjgpjanzjbvsykvskvdadhgejdhqeluewqjzvayxcgsghxpuyszncrlfxjckgfoygrabkrbryuaqesyobfoduyjqhizztnnkqnqprcwcssqerqcxcfsovcxeeilxxtrhfwptqxbpemnydsqdxggctotpzdseofpetoktexyhgxxasjhpaqrkuxdauaqujkuvtmhlmmiflivtsqspmarblnmuwfnnniqkfsbrnsftdftyatzuzuwpkhrmbswyuupytrqngvdjwiceazrrurkfawaupldfeptwewekvumgijlrywjjdyfmvgxwddbwwncdjdxjpmtcakcnzowceofjfnpcldtotrctmcyzwyxdsgagvblybfecisqubnaurtwbiedsryizhpnotkqoywdjhjgnhdkxcwvtnkmfrcgirgajibjzjhohnfjenxqjblwzrvozwksgulcfeuuabcavjsftxwxdzppnbqehnrxsqlpicenpemhudvrxaqpluxotbvpyqipuelazcenrqcrrmdcorbhqplqgsjrgbdfdfchsjvncyxyhuntyelhdxlkayniuwdxzauhazqdrqjskdugssujzygcnyhuyeaktvdqlvtamzqwyyqxmluhfsuhguzdhmyvrycwcuxuhrulmefovbecgqknhghbxfrtboptalfxwuqynfmgsppmfgiynwuyoxyqydgwxhvmobjayjucvnuamufjdtbxinlrmchkqfvsvavgyenwtqffmuscqffhlqodagqrfhfomutdsccwnfwexzqyhagoqquxjdyeggnudfcepenkqudfjlbodmexhjehxgcvnvsnljbnhwbjkjytffezukhnljmuzfrospjgrtmewvjzftuwrvjkavkgllmunxyfktvwbgzjqssakwaaxeqjjsowrtdfulxpfdkjykqnursrdakcvnkiojtpkhllsmnctpeqhbsycpvaqsfdvlellespcwzzfqhzxitrkrfauhzibeqlbwmqerkqvorioeornedysqbtnjiybqovgecsohpgrylppwtercxeenovetiltytoldzwjbrqibnjlgxapohvmtrnxyjfhcadvnvdsjskcszucyctnnevlsqtrlxronbtpqqogquhfeykpgumdlcswcocffzxsgtjfmxzwfhrmmjusjpxicqqwweugxpzxzwqhdrpgtuebdwdbiirxzunvryhcfabugimifaucznrbmuhsdswpepwdpvnbakleeqshnikuljwlrorzzzpbzvrlifrsdwwkmnyjoigfcmzkukhjfzmqxebdsyfhwtqyetuqvnefwfmdkmzggeqhqfgkkyiybjeqznvrhcoulypctjslphyqsanrygdhvkwgiyqgnflrvvtsxzjpxmwhbfojjguyttyuetcxpyukkkoxrhbeemjwwuzofmmrygvktxhjzadlovhmyocfxjfsruhfqjrncolzoqehuhyqmoqmdbplbscjknlxryuxwmifhlxvguknisuhmbcaclmfgteebbypcyemqimolnznhwcktjqzwsfulapbkmmgkgtnqotffjegxwvcvunohfqgczmalhhlizpidqkeaoyglwxqkrppytcscxmbbcpfmktxfynayzfcqmyalxuocgvvawgigxlfonotrxjfuhfduexixsaihpfdnanqtiftvskqwhkobpaceorxrljstbyeehummkxxhqptixtdkaueippjueidlhychhacsrgadxhcaonclmrgnnmxddumcdscyhijigcewbvvulyzohfdvqbcphgoqqcxvskpwwnmnqmldowiijxretntlrdlodstbryjpnfcavipexdlunwycbemgkrgupbgycootkgydalojqtsbxatberwdjptfdtnvqkahyihiazmtdrzhbggyiamowpgcmydcktszykvkgxlztrfgdaajqngcsvehzyjwjqrymwqvznsphstowbgvwirtngdjevqbdacxngapsvercnjxcobqhmpgpwfkrowlpgirvzpmtsqcxjmakhqzsvplidhsdguisbikpcahxebtucrcpsopzvlpsqrrlkteeiavjyqvapkktbzdgtcbgjiiocenzgytqfdbzxjqualawzigagsknlsgbztvsmspesbohoprpguetopmcwkokxqghovnelfgflgphoighgssqlteiwyyezmyslzgveyycbhobgzgruvyqxwgqspakymawjxvonsexnqrxbmnplvaqaznomerdklcgadxoyvpofrpkirfcjfooowlovnjxkyuohzpjnxxwtjhganlqcdpzbleralupwfnbybznvefwhnlttfyhnoxwwrpyftbggpruwsppjxblppxctoyhltffockgyskdwfgopehzdljxmlhtrlgjdchsikwkaksezbeyzbncjduqroxyatfhldibqifgicahwmahdhofcppurvtezsqchxslnsqqylmfahlavfrivmezixtxicieovcsajdfjmkqwaqdbelswwdqqzjyefhxgmzlzidnkovrrfqoytizhppwdtlybtvfogwuxqjayelbielflelmorpjxbotpyjjhgwweknojesyghbxaycjoqoyqjpogwbxdjtexztsbiynquxhpmwkikoftlxvnlpqyqcublehyotrncuorczsehnqqnxrntjkztwhlfrqouvzewqyonorfummfzsbkbwlzrasscasdzccymjuwrjxpyaosdnxwrjoehphfrdxplpnesamtronxdiktamhzbhskhjwsfxcynnpvjrunkocyiecqtkkvfuxhzoxbmskrclogrxwwwkfqqmkkxejryczrihzqoptqozfddslsgrwfbtajgddevyexzecjlcyyyjgmacjludzolcalapyizcfjqeizzuijrfuxuotyafemhqxbivcnfesumcgqlcauqivxxtftxxfyhxqkaspzxeuhaazizwpvcjledbrenveqtyclyjnfnyoarrnbwssphmeuptwvvvcziixegexyyitgsmjjcsnnmoppqojgpdssotqdyyxwrnwigrxhngekunrmjjzecbgjqbxtkyjrzbpgbhuuhbhwrecgcsxzshdjoxcktoddxywtznuqavthodgdqdqmjlxquhyezgebxmnjdheqjwvpgghbifrzflaltfdiyevkzhpgvjrioxvievxylgqzwffaqdqgmpludcgzveusclpjcqwqrawueyqzwcjltgdszrdygzrxuicmawhaghtwduafygnwuxdsbjbrdqdyakslcsunxswudanuwkrkhviyajmwmpoihqkibyrodnmixdjtbhjbzjaskdsfarvuzyxjoxhhfaikgilmsxikjbnywcyrahftpbxckhhomjmsyynksoyeryvzybubbiihahqnnzjgqgrfzvrixlszqsvxtlcthadkhuxjzmaigewvaagicqlegxvlwvfzydebuwxofaxkvljzoxvbipuhzamoncjitetsnvywzwryeuqupvrudgrwlrutxyumwxecgyvkuwwalluoqqohpldrukzvjbenizoxcgvlzatvptoccxgoxzcejeyocapeumciacljnnxwtqsnkfwjugnfohbqupowgmhnsjhwtwmjrqqawyrrbmkucrpivillwjvxaonwnkkkdxqffopzyfayzjaypzjhjstrylngdhwizzgeuogtzmdjmfnkjxirsnfxctbgizcnsqcuvbazqrlqbtuycrxjmyscfiftbxtzahfuazwffcexwzsrykimcsmsysgjukybmwmuahbpezqvllznjpoffliuphwaqsdtpfqaqlmyhnwzxidllbafsnjmyaijcjedpjeddakicylmaflearcdmfrznkwhtsbyobyduytbdaymohadykujrhmkenomcphstuhxcndcujwdtkdzgpkrmalnxiuoqlvlyntmdygewbuqinouxrazqiiwkfnntflcdujqzbpcaiyjpurtcraxtjhkfdodtxbdbepmrmwheogxmcskcjxhschamrsmxrzahtdurdebfmctdankssnpzsvbrmfumboqmcfgwzwjinfmiqymnzhxuxebftnyutosuhtoicopcifvfvfprhczbjrwfuxvmzdynzasqgdjcsrspfvnpbwgkuofjloxxtfvglvyeczasnyoxquebyaupyhilchbtuhzargkotxpmtcewcbmnzkexpkxoponqrbzbcvyhtnkmxgzdpitzaljgtfuzltyfxqvnznqpxmliqjubkzgwqgoltqntjlwmelvplbgljojrfimuurvwmcfibrqaedobcbjizwjmqxtgqwlwnpbhvsbeawqxoipzlokrzroibgryvqukmtafqhqqnrfkdnyexmfibltjczqvviwmwhofazjqyvhjwjiqngtonratdrfghqovddteejgnixrtawttkgdxnxhlcbxedmsipijtlehdixatqhgskwagqzgvoralqataxztiuxmjdzurnevgojftcdmcfrcvihugkutfljnjgnajbtydmfxqnqllstwqugtmxfsjelqjqvfvlegdomygjqjehmvmglowbislmfuihsybxuwnqgzuuabexpnqkgvjtinxacdcxhyhslddhflxrwaspzsetsvbrtzqoupmiwnehojxhrpfkyoxxiklxjpzhbtyjoejdeeuelquhstvqrwtnlsurdyitlchvxrbxhljzbryehtmqttcodrpantdsqjneddylcmdzbotuyqnqbzipdyxzappcfqpsykzzfvtjzurnetoslorhpzcetqrmbshuecdjyobzcsvzpeqbxwslzqrvcpehqtchirchqzeetiyqydatdtdwsvvcilwpexkhetlkmoynknxsicrmqcnpsoekqbapvuioeqdfnpajmdvjennzfnghnadcebjnvebhhiakqyshodzmipspylgtqcipabyqyrzkkbqfheacculvfekttoefqqhbqxvbhfvsfrjqasdvqvlcafjxhjowbrnoblyfiuksvizrdytobrbojypgdhgnbjcbrdryxdqgywuulqdbwhxcxobkmznhfhrvplugwekgnlkzfyskjqdcsxqcygqhqulgnnidistiekrdiawvphicordpkkpkalcbnxetjazgyzladgvnvpoqhbghbvueejrbzxypmugxuetscgzdvsuavypkgascriidvyefjpfxmlvnnvaswcpjqmagwzxnkquaefxcsmqhttnytunjhxbkvilplbrijqzyevpxbxkwpzhtacbefvtzpwagndspeukxfhnmrzxnxmkposnkhgfkhwqdubenplrqwrgpavimdetagrvoyenkdozucmygmokhlocijhtwxwzqdcwhmpmqllvejowpmijkbtebwvogyehnpebiasrpxnsfqdztmkmpxqhgwnacucdfewwnjdzoeebpepkhfmxoxovxpsabjllnpxnlvsoaxvxsdyungcpvegqmafnkzfnuwyvquhkrypkwjjrjnnmekolbokszcqsgjskerwytflfqqtfiidkz",), 81),
    ]

    foo = Solution()
    method2test = Solution.largestVariance
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
