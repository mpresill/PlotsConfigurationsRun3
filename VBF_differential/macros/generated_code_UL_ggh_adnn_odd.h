
#ifndef GGHweights_odd
#define GGHweights_odd 
 
    // Select all (Ctrl+A), Copy (Ctrl+C), paste to an empty text file (Ctrl+V) and save that file as 'generated_code.h'
    // 
    // Auto-generated header file. Assumes img to be a floating point array
    // of 64 elements (corresponding to an 8x8 b&w image)

    #include <math.h>

    float norma_GGH_odd;
    
inline float activation_GGH_odd_0 (float x, float n) 
{ return x > 0 ? x : 0;}
inline float activation_GGH_odd_1 (float x, float n) 
{ return x > 0 ? x : 0;}
inline float activation_GGH_odd_2 (float x, float n) 
{ return x > 0 ? x : 0;}
inline float activation_GGH_odd_3 (float x, float n) 
{ return x > 0 ? x : 0;}
inline float activation_GGH_odd_4 (float x, float n) 
{ return x > 0 ? x : 0;}
inline float activation_GGH_odd_5 (float x, float n) 
{ return 1./(1 + exp(-x)); }

    float guess_digit_GGH_odd (const float *img)
    {
    
  // Declare the arrays in the stack
  const float kernel_GGH_odd_0[36][13] = 
  {{  -0.3300608396530,  -0.3101342916489,  -0.0122099025175,   0.0879798233509,   0.0262575298548,   0.0377195663750,   0.2353970408440,   0.3730006515980,  -0.2869796752930,   0.0325128473341,  -0.1097612679005,   0.1579036414623,   0.0957108438015},
   {  -0.1737208217382,  -0.0735974013805,  -0.2862218320370,   0.1308932751417,  -0.0215958952904,  -0.0339702926576,   0.1136407181621,  -0.2243376076221,   0.2152303904295,   0.2493501603603,   0.0413577929139,   0.0065334276296,  -0.0047338916920},
   {  -0.0868241488934,  -0.1408856511116,  -0.1859365850687,  -0.0767337903380,   0.2851366102695,  -0.1319905519485,   0.0582000352442,  -0.2267682999372,  -0.2551297247410,   0.0724366530776,  -0.3848462402821,  -0.0085168527439,  -0.3452664613724},
   {  -0.1037752255797,  -0.3192140460014,  -0.2050446420908,  -0.2746711373329,   0.0344459824264,   0.3132374882698,  -0.2940147221088,   0.0002212581458,  -0.0991490259767,   0.1603983044624,  -0.2294529378414,   0.5567299723625,   0.1553315371275},
   {  -0.2008100897074,   0.2163743376732,   0.0973218157887,  -0.1013708114624,  -0.0129319066182,   0.0362027101219,  -0.0041568810120,  -0.0164964757860,   0.0624889396131,  -0.0803253874183,  -0.0574407391250,   0.0430197529495,  -0.1630928069353},
   {  -0.2243807613850,  -0.3703789412975,   0.3638777434826,   0.2640830278397,   0.2228508144617,   0.2544137239456,   0.1075465679169,  -0.0315750390291,  -0.2130486667156,  -0.1476236581802,   0.1152647957206,   0.0219901129603,   0.1489162892103},
   {   0.0551665350795,   0.0315550342202,   0.2808901369572,   0.1227090433240,  -0.2771593928337,   0.2198690921068,  -0.0041858539917,   0.2613520026207,  -0.1034063473344,   0.0023316997103,   0.1532675027847,  -0.0213424991816,   0.2604176700115},
   {  -0.3467973768711,  -0.4345079064369,   0.0027027684264,   0.1381724625826,  -0.3820667266846,   0.0164238866419,  -0.0970632582903,   0.4844467341900,   0.0753298476338,  -0.2713383436203,  -0.0264457594603,  -0.0309136305004,  -0.0145077453926},
   {   0.2944690883160,   0.1594080775976,   0.1733990311623,   0.0886749327183,  -0.0173964425921,  -0.0548375286162,  -0.2683529257774,   0.1636792421341,  -0.0588967725635,   0.3020718395710,  -0.1873477250338,   0.1136609017849,  -0.2176394462585},
   {   0.4412738382816,   0.2835512459278,   0.3558762371540,  -0.1602525562048,  -0.1545604020357,  -0.2806720435619,   0.0972274467349,   0.0078030885197,   0.0283324718475,   0.2667861580849,  -0.0287341680378,   0.0132548622787,   0.0243366062641},
   {   0.1998058557510,   0.0258412957191,  -0.0160192009062,  -0.0836650803685,  -0.0906752869487,  -0.2290760278702,  -0.1273849606514,   0.1493554711342,  -0.1711055189371,   0.0495773330331,   0.1045878306031,   0.1246815770864,  -0.0093638412654},
   {   0.2560594975948,  -0.0481423698366,   0.1591449677944,   0.0463738031685,   0.1166756004095,   0.0231110062450,  -0.0027564703487,   0.0468762032688,   0.0843651667237,  -0.1662348657846,  -0.0838692784309,  -0.0610387809575,   0.1243450269103},
   {  -0.1456543505192,  -0.2709292769432,   0.1918787658215,   0.2563217878342,  -0.1551776528358,   0.3445092439651,  -0.0335804969072,  -0.1827759891748,  -0.3581489920616,  -0.1764643639326,  -0.2060293406248,   0.0489234589040,   0.1489843577147},
   {  -0.2165650278330,   0.2570170760155,   0.2053321897984,  -0.1800363361835,  -0.3027254641056,   0.1805858761072,   0.0366234555840,  -0.3512761294842,   0.2242545038462,  -0.0692809224129,  -0.2694396674633,   0.0343798398972,  -0.1769826114178},
   {   0.2513164281845,   0.0560865923762,   0.0073586227372,   0.1295841634274,  -0.0146930143237,   0.0540540218353,  -0.1502516120672,   0.0424798019230,   0.1356912255287,   0.1293327510357,  -0.2210608422756,   0.0259178914130,  -0.1266934424639},
   {  -0.4939447343349,   0.3107356429100,  -0.1592684835196,   0.0350535400212,   0.0646608471870,   0.1680564135313,   0.1861787736416,  -0.1041164472699,   0.0990780368447,  -0.0018771213945,   0.0862220525742,  -0.0405069440603,  -0.0085213063285},
   {  -0.0921799615026,  -0.1152866408229,  -0.2528444528580,   0.0538901090622,   0.1153670847416,  -0.2484675794840,  -0.3504838645458,   0.0027919556014,   0.1914878785610,   0.0671614184976,  -0.1041220277548,  -0.1418268531561,   0.0941480696201},
   {  -0.1094589680433,  -0.0429589487612,   0.2178326696157,   0.1616760492325,  -0.1194216012955,  -0.0092831868678,  -0.0692742317915,  -0.0313516817987,   0.2353244423866,   0.4544816613197,  -0.0254821404815,   0.0217241626233,  -0.0710267573595},
   {  -0.0836356729269,  -0.0073266685940,   0.0653540715575,   0.0135422386229,   0.2743862271309,   0.0723031535745,  -0.2600420713425,   0.1636175513268,   0.4346196055412,  -0.1235642582178,  -0.4483139216900,   0.0984634682536,   0.2195509672165},
   {   0.1413231194019,   0.3622249066830,  -0.0099331764504,   0.3630450069904,   0.1005247235298,  -0.1818829178810,   0.0446663312614,  -0.0820253640413,  -0.1724157482386,   0.2491025775671,   0.2340326458216,   0.1962295174599,   0.0203559361398},
   {  -0.2250016629696,   0.0791938379407,   0.2231478244066,   0.0078803431243,  -0.0750555694103,  -0.1633915156126,   0.1132364198565,  -0.1072278469801,   0.1349350363016,  -0.1370655596256,  -0.0056581948884,   0.0752218738198,  -0.1640611737967},
   {   0.1069410443306,   0.0065429816023,   0.3152423501015,   0.1939494609833,  -0.1126026138663,   0.1238531470299,  -0.0041287774220,   0.0448990203440,  -0.1878910362720,  -0.1237126439810,  -0.1784255653620,  -0.1968239694834,   0.2357594817877},
   {  -0.0423491187394,  -0.2149247974157,   0.3168462216854,   0.2151206880808,   0.1486248075962,   0.2788405716419,  -0.2348854988813,   0.2122053354979,   0.0898249372840,   0.2520044445992,  -0.1425822228193,  -0.0724190250039,  -0.2527362704277},
   {   0.3344254493713,   0.0885021984577,  -0.2459824979305,  -0.1009803116322,   0.0581927038729,  -0.1161715015769,  -0.1772968620062,   0.1931135654449,  -0.3727628886700,   0.2123584598303,  -0.1594883948565,   0.1316213905811,   0.0222537443042},
   {   0.3620098829269,  -0.4747541546822,  -0.4812130033970,  -0.5547885894775,   0.0856021866202,   0.3019219934940,   0.2821519374847,   0.0636810734868,   0.5168420672417,  -0.2285431623459,  -0.3996560275555,   0.4069690108299,   0.4383749365807},
   {  -0.0633322224021,  -0.3566385507584,  -0.0763551145792,  -0.2215291410685,   0.0480757616460,   0.3362280130386,   0.1514954119921,   0.5031540989876,  -0.3051683306694,  -0.1322052180767,  -0.4060465991497,  -0.1679071635008,  -0.0568953268230},
   {   0.1614206582308,  -0.1855799406767,  -0.2078854739666,  -0.0500192232430,  -0.2095851898193,   0.0659047514200,   0.2310280054808,   0.2813173532486,   0.1265473812819,  -0.0628075301647,  -0.2565658986568,  -0.0953245311975,  -0.2041465789080},
   {   0.0981595814228,   0.1060554906726,   0.2629922330379,  -0.3888682425022,  -0.2519021034241,  -0.1776001602411,   0.4113295376301,   0.0974116846919,  -0.3114166557789,   0.0470477305353,  -0.4621744453907,   0.0083137461916,   0.1150747910142},
   {  -0.0394836515188,  -0.2288209050894,  -0.3225742876530,  -0.0285756252706,   0.2800769209862,   0.2389837503433,   0.1460896432400,  -0.0681489184499,  -0.1697514951229,  -0.1202019825578,  -0.3041816353798,  -0.0051125390455,  -0.2854945659637},
   {   0.2497612088919,   0.1191454753280,  -0.0359623320401,   0.0557712540030,  -0.3433011174202,  -0.1280239224434,  -0.1095289364457,  -0.1014230623841,   0.1596121490002,   0.2083137780428,  -0.2774240374565,   0.1151411831379,   0.2808961570263},
   {   0.1928003579378,  -0.1673935800791,   0.1123264953494,  -0.3191014230251,  -0.2112331390381,  -0.1577052175999,   0.0541176348925,   0.2583355605602,   0.0768851190805,   0.0925170406699,  -0.0242136660963,  -0.1701826304197,  -0.1102387085557},
   {  -0.1956692188978,  -0.0147803425789,  -0.0671094954014,   0.0172143988311,  -0.2888794839382,  -0.0327407345176,  -0.2059114128351,   0.0663989111781,   0.1698377877474,  -0.1063626855612,  -0.2380512058735,   0.0240808054805,   0.2799493968487},
   {  -0.0020417510532,  -0.1923352926970,   0.0068576727062,   0.3612382411957,  -0.2087250351906,  -0.3102758824825,  -0.0746421441436,   0.0289273075759,  -0.0862815380096,   0.2570014297962,  -0.0007394867716,   0.2484647780657,   0.2363847345114},
   {   0.2252580672503,  -0.2518814206123,   0.1491639763117,   0.1331641823053,  -0.1315097063780,   0.0071949730627,   0.3025434315205,  -0.0120393568650,   0.2837473154068,  -0.2186973541975,   0.1843592673540,  -0.2249512523413,   0.0598929338157},
   {   0.1458269208670,   0.2209674566984,  -0.3814195096493,   0.3189480602741,   0.1855382770300,   0.2471677958965,   0.1825493872166,   0.4711562395096,  -0.0107979793102,  -0.0094534950331,   0.1938955485821,   0.0235814228654,   0.0361468158662},
   {  -0.1802689284086,   0.0075764390640,   0.1812359094620,   0.0119685642421,  -0.0509910583496,  -0.0376587733626,   0.1158792078495,   0.2557011544704,   0.2848640978336,   0.1228009015322,   0.1094351932406,  -0.0669740438461,  -0.1811482608318}};
  const float bias_GGH_odd_0[13] = {   0.0741427242756,   0.1093580424786,  -0.0644787475467,   0.1233896017075,  -0.1076697111130,   0.0195906106383,   0.1083789169788,   0.1390233039856,   0.1400500684977,  -0.0904916450381,   0.2051562070847,   0.1411018520594,   0.0637026131153};
  // Declare the arrays in the stack
  const float kernel_GGH_odd_1[13][13] = 
  {{   0.3287456631660,  -0.1410975009203,   0.1117858141661,   0.3208838701248,  -0.4133514761925,   0.1845534741879,   0.5035697221756,   0.4342271685600,   0.4632279872894,   0.2267733216286,  -0.1411348432302,  -0.0956287384033,   0.4153668284416},
   {   0.3121324479580,  -0.2076615989208,  -0.3936490416527,   0.0522261187434,  -0.2016615569592,  -0.0238880142570,   0.2628376483917,  -0.1162098199129,   0.3365603387356,   0.0668358281255,  -0.2511937618256,  -0.4250850379467,  -0.0807180330157},
   {  -0.3709468245506,   0.3159227371216,   0.1210332065821,  -0.0905194208026,   0.2098809629679,  -0.0042477105744,   0.0159834157676,  -0.2997973859310,  -0.0967983752489,  -0.3243155181408,   0.1912815272808,  -0.3792490661144,  -0.0132597200572},
   {  -0.1583054214716,  -0.1016679629683,  -0.2566922307014,  -0.1130529716611,   0.0405862070620,   0.0708580613136,   0.3196835517883,   0.1850419044495,  -0.0317942127585,  -0.0256901867688,  -0.2981134951115,  -0.0805054754019,  -0.2425163835287},
   {  -0.3702809810638,  -0.1581853926182,  -0.2126774340868,   0.2643178105354,  -0.4250324666500,  -0.1309601217508,  -0.1681161373854,   0.1318010389805,   0.1612688302994,   0.3925648927689,   0.4133566617966,   0.0882311984897,   0.3914602994919},
   {   0.0382736213505,  -0.0396312735975,   0.4657328724861,   0.3428775072098,   0.2854381799698,  -0.2249194979668,  -0.1286264955997,   0.3279398381710,  -0.3680432438850,  -0.4249319732189,   0.2305676639080,  -0.2046174556017,   0.3303420543671},
   {   0.2918942272663,   0.3652566969395,   0.2653852105141,  -0.2176378816366,  -0.4871164858341,  -0.5747700929642,  -0.0865387767553,   0.3152125775814,  -0.4862739145756,   0.1909287571907,   0.4138475358486,  -0.2487683743238,   0.2974982261658},
   {  -0.3344490230083,  -0.0336165837944,   0.1186388954520,  -0.5253515243530,  -0.2134111225605,   0.1498211473227,  -0.1582085639238,  -0.4475496709347,   0.1559502631426,  -0.2599261701107,  -0.2211633175611,  -0.1835970580578,   0.5923174023628},
   {   0.5477946996689,  -0.1143530979753,   0.5208336114883,   0.1049943566322,   0.0028834550176,  -0.4594516456127,   0.2843059897423,   0.1365133225918,   0.1836358606815,  -0.0009338262025,   0.4868490397930,  -0.0196333527565,  -0.0945338085294},
   {  -0.0467311516404,  -0.3898082375526,  -0.0270665977150,   0.3130480945110,   0.2656466066837,  -0.1296184509993,  -0.1677073836327,   0.2962517738342,  -0.2814289033413,   0.1242371201515,  -0.1226153820753,   0.0324995219707,   0.0550104938447},
   {   0.3824038803577,   0.0866283401847,  -0.0720047727227,   0.2607295811176,  -0.3504740893841,  -0.3211809694767,   0.5372585654259,   0.1983256042004,  -0.0634332224727,  -0.0686009824276,  -0.2751270830631,  -0.3634342849255,  -0.4643287062645},
   {   0.3793389499187,  -0.0686393082142,   0.1014809012413,  -0.5283102989197,   0.0826143175364,  -0.1039361804724,  -0.2867500782013,  -0.3618648052216,   0.4452667534351,  -0.2879596352577,  -0.4860874414444,   0.6166355013847,   0.0960176885128},
   {   0.5272956490517,  -0.3298592269421,  -0.0550518184900,  -0.4401556253433,   0.0394130609930,  -0.2434043586254,  -0.0379356369376,  -0.2949109077454,  -0.1128963828087,  -0.5839828848839,  -0.4963426291943,   0.4970552325249,  -0.2678048312664}};
  const float bias_GGH_odd_1[13] = {   0.0876865983009,   0.0237374268472,   0.0796959176660,   0.0884188935161,  -0.0967246070504,  -0.0302783008665,   0.2381754070520,   0.0452839843929,  -0.0105843283236,   0.0267521776259,   0.0550783611834,   0.0481716319919,   0.0262305401266};
  // Declare the arrays in the stack
  const float kernel_GGH_odd_2[13][13] = 
  {{   0.4282843172550,  -0.4385511875153,  -0.4256361424923,   0.3828287422657,   0.4683384895325,  -0.3476496040821,  -0.0862298235297,  -0.2607223391533,   0.1827339380980,   0.0697816312313,   0.3049924969673,   0.4261586964130,   0.3350272476673},
   {  -0.1829800009727,  -0.3098979890347,   0.3591397702694,   0.4812538623810,  -0.3882572650909,   0.2612982392311,  -0.4835874736309,   0.1742545515299,   0.1100748553872,  -0.0174723304808,  -0.3601843416691,   0.3748015463352,   0.0663239508867},
   {   0.3635157644749,  -0.1633432209492,   0.1202253624797,   0.4975896477699,   0.3758620023727,   0.4368574917316,  -0.1224070340395,   0.3899304568768,  -0.1471819132566,  -0.4634058177471,  -0.3690867722034,   0.3559689521790,   0.2052678912878},
   {   0.4088526666164,  -0.2624602019787,   0.0808990523219,  -0.2626410126686,   0.0311527010053,  -0.4117199778557,   0.0833078995347,   0.1428716480732,   0.3989724218845,  -0.4160086512566,   0.5214970111847,  -0.0459956713021,   0.2816554307938},
   {  -0.4005528986454,   0.0498705171049,   0.2497245967388,  -0.1122173815966,   0.0664093270898,  -0.3475477993488,  -0.2411947250366,   0.4511640369892,  -0.0421561561525,  -0.4729861617088,   0.3304964303970,   0.0931061729789,  -0.2763988375664},
   {   0.3458073437214,  -0.4252137243748,   0.0293892081827,   0.0761442929506,  -0.4572060406208,  -0.2334340810776,   0.2195620685816,  -0.3757842183113,  -0.3122856318951,  -0.2574256658554,   0.3011190593243,  -0.2113048136234,  -0.2776045203209},
   {   0.4810631871223,  -0.1025061979890,   0.0565406866372,  -0.1339254677296,   0.1441614478827,   0.4497692883015,  -0.0801119655371,  -0.2456016689539,   0.4599206149578,  -0.1713656038046,   0.2192699313164,   0.2166675627232,  -0.4460846483707},
   {  -0.1843609064817,   0.0996922925115,   0.2176869809628,   0.0367447771132,   0.1091433838010,   0.3091745972633,   0.1114361211658,   0.2543792426586,   0.1404452621937,  -0.4060174822807,  -0.1102619767189,   0.1601836681366,  -0.3645579814911},
   {   0.2627662122250,   0.3644293844700,  -0.0114411953837,   0.3002324104309,  -0.3208719193935,   0.4653864800930,   0.1548595875502,   0.3981397747993,  -0.0036201095209,   0.1617952734232,  -0.4346874654293,   0.3416085243225,   0.0903616324067},
   {   0.1369950324297,  -0.0500435866416,  -0.1062984839082,  -0.1999974399805,  -0.4693364500999,   0.2393263280392,   0.3956691026688,   0.1482224613428,  -0.1834361851215,  -0.0398083515465,   0.3084751069546,  -0.0053805122152,  -0.1763875335455},
   {   0.0666826218367,   0.1346584856510,   0.2616350948811,   0.2201858013868,   0.2936408519745,  -0.1022751405835,   0.1894778609276,  -0.2206064313650,   0.4787137508392,  -0.3577308356762,   0.0925216898322,  -0.4470321834087,   0.0913216695189},
   {  -0.5719505548477,   0.4768337011337,  -0.5114506483078,   0.2817629575729,  -0.1759557574987,   0.2566147744656,   0.0963044315577,  -0.0957024917006,  -0.1660161614418,   0.0641665905714,   0.2526894211769,  -0.1799651533365,   0.4206211566925},
   {   0.1388029605150,  -0.3468090593815,  -0.1049964129925,  -0.0329891033471,   0.0843814462423,   0.3960226476192,  -0.4700503349304,  -0.4153245687485,  -0.1798321008682,   0.2377582788467,  -0.3161892294884,   0.2958243191242,   0.1593108475208}};
  const float bias_GGH_odd_2[13] = {   0.0725816488266,  -0.0010842893971,   0.0544059835374,   0.0961212217808,  -0.0237550511956,   0.0075210304931,  -0.0305423606187,  -0.0317692644894,   0.1198389232159,  -0.0539774037898,   0.0366749279201,   0.0699006095529,   0.0254892203957};
  // Declare the arrays in the stack
  const float kernel_GGH_odd_3[13][13] = 
  {{   0.1893578022718,  -0.2489894032478,   0.3219732642174,   0.0232110861689,  -0.0286581721157,   0.1143868416548,  -0.0920479968190,  -0.1678612083197,  -0.2564322948456,   0.1140151098371,   0.1161381602287,   0.0011740472401,   0.4260213673115},
   {   0.4731719195843,  -0.1946516185999,  -0.6366779208183,   0.2073439061642,  -0.4102550148964,  -0.2550295889378,  -0.3179351389408,   0.1561970114708,  -0.4300043284893,  -0.0299810469151,  -0.3888531923294,   0.3187324702740,  -0.0667582005262},
   {  -0.2716010212898,   0.0808804482222,   0.1881105899811,  -0.2985725104809,  -0.4542103409767,   0.3214071989059,   0.4768975675106,  -0.4161830544472,  -0.1953537613153,   0.4272170364857,   0.5208007693291,   0.0373519659042,  -0.2067542374134},
   {   0.2616011500359,   0.1177665144205,   0.1907422244549,   0.1160629242659,   0.0545400120318,   0.2181945294142,   0.1947570145130,   0.4622378647327,   0.4598260521889,   0.4185607731342,  -0.3366637527943,  -0.2404630482197,  -0.4019027352333},
   {   0.1680414974689,   0.3102276325226,  -0.2054603844881,   0.2512510120869,   0.0524963103235,  -0.1685465276241,  -0.5167859792709,   0.1915863305330,  -0.0212916173041,  -0.2961317896843,   0.3889112174511,   0.0709407404065,   0.2477919459343},
   {   0.1967312991619,  -0.0760395303369,  -0.0925330817699,   0.4585287868977,  -0.3708719313145,  -0.3838755190372,  -0.4908559024334,  -0.3337528109550,   0.2872279882431,   0.3972372412682,  -0.4525651037693,   0.2301356047392,   0.1359232366085},
   {   0.3097758889198,   0.0284019131213,   0.2613182663918,   0.2358748018742,  -0.0932891815901,  -0.1863457858562,   0.1008464694023,   0.1387679427862,   0.2476496398449,   0.5387746691704,  -0.0649771541357,  -0.3821877539158,  -0.0874459445477},
   {   0.3136907219887,  -0.2211285382509,  -0.4103335142136,   0.4485531449318,  -0.4179059267044,  -0.3180546462536,  -0.1513384431601,  -0.3955989480019,   0.0722402632236,   0.1271636188030,  -0.0017042397521,   0.5223962068558,   0.2747852802277},
   {  -0.4080054461956,  -0.4236894547939,   0.1895149946213,   0.4300054311752,  -0.0227376725525,   0.4315025806427,  -0.2266050577164,   0.0933092907071,   0.1113222017884,   0.2486537694931,  -0.3066591620445,  -0.0160158555955,   0.2223421782255},
   {   0.3384399116039,   0.2348693162203,   0.3005087673664,   0.3395782709122,  -0.0487517118454,  -0.2169470191002,   0.0337551981211,  -0.3504053652287,   0.4486718177795,  -0.0936597287655,   0.0733673647046,   0.2946599125862,  -0.0995404794812},
   {  -0.1344233006239,   0.2160108685493,   0.1933225989342,   0.0414179489017,  -0.4295251369476,   0.0200104415417,  -0.4736362099648,  -0.3326611816883,   0.1810868680477,   0.0144781339914,  -0.3786521852016,  -0.0895458310843,  -0.0657934769988},
   {   0.3223216533661,  -0.3879573047161,   0.1194648444653,  -0.2145012617111,  -0.1197112351656,   0.4886513650417,   0.2187978625298,   0.5674757957458,   0.3024249374866,   0.0772243067622,   0.0108478181064,  -0.2811329960823,  -0.3969434201717},
   {   0.3597524166107,   0.2248305082321,  -0.5487359762192,  -0.3430161774158,  -0.0455228053033,   0.2176793664694,   0.1894659399986,   0.4446107745171,   0.4342658221722,   0.1640979051590,   0.2236564606428,   0.2935288250446,   0.0160795319825}};
  const float bias_GGH_odd_3[13] = {   0.0367173925042,  -0.0198233406991,   0.1044589653611,   0.1137024685740,  -0.0097895031795,   0.0940443947911,  -0.0563959144056,   0.1053101420403,   0.0197604428977,   0.0553459264338,  -0.0341726318002,  -0.0801344662905,   0.0925344377756};
  // Declare the arrays in the stack
  const float kernel_GGH_odd_4[13][13] = 
  {{  -0.2701870501041,  -0.1828585267067,   0.1958457380533,  -0.1439840197563,   0.4674749076366,  -0.1312793046236,   0.3867853879929,   0.2932824790478,  -0.1446551978588,   0.4725210368633,  -0.2110043019056,   0.3784492313862,  -0.3204263448715},
   {  -0.3170536458492,   0.0001481410436,   0.2710629999638,   0.2790291905403,  -0.3545027971268,   0.3611060678959,   0.3748068809509,   0.1903306692839,  -0.2198350280523,   0.2555660307407,  -0.3580158352852,  -0.2786467373371,  -0.4426149427891},
   {   0.4014236927032,  -0.0212053991854,   0.4426749944687,  -0.0055388077162,  -0.2634671926498,  -0.3969878554344,  -0.2735712230206,  -0.1831123828888,   0.1866738498211,  -0.3859618306160,  -0.0386213101447,  -0.2406905442476,   0.2743257582188},
   {   0.4138433039188,  -0.0864070877433,   0.5002114772797,  -0.4364555776119,  -0.0834111124277,  -0.0764270946383,  -0.0825508087873,  -0.1487642973661,   0.3264170587063,  -0.1950893253088,   0.1994439512491,   0.3049556910992,  -0.5058903694153},
   {   0.2289074063301,   0.2197687625885,   0.4601600766182,   0.4796835184097,   0.3045846819878,  -0.0143502354622,  -0.2400582581758,   0.2250161468983,  -0.4150574803352,  -0.2085486948490,   0.3421164751053,   0.0145827727392,  -0.1296160519123},
   {   0.1142315492034,  -0.0217165499926,  -0.0031686709262,   0.1401354372501,   0.3647001981735,   0.0206763632596,   0.4351631402969,  -0.3131953477859,   0.0601572990417,  -0.2877729237080,   0.5703644752502,  -0.0197200514376,   0.0834314897656},
   {  -0.3636120557785,  -0.1661960929632,   0.0976151973009,  -0.3578121662140,  -0.1523943245411,   0.1540948301554,  -0.0414315238595,  -0.4898084998131,  -0.4447076320648,  -0.4411031901836,   0.3727170526981,  -0.2406001389027,  -0.2573982477188},
   {   0.1210525780916,  -0.4524742662907,  -0.3757221102715,  -0.0410802997649,   0.2079927176237,  -0.3716661334038,   0.3812781572342,   0.1239191293716,  -0.4108164012432,   0.3864407539368,  -0.3330344855785,   0.3071908652782,  -0.1982978433371},
   {  -0.0471839830279,  -0.1748536229134,  -0.1343449056149,  -0.1736819744110,   0.2413785010576,  -0.3313839733601,   0.3824573159218,  -0.3457914590836,  -0.1596418619156,  -0.3272116780281,   0.0744954347610,   0.2511070966721,  -0.3800377547741},
   {  -0.1386882364750,  -0.1646578311920,   0.1172621920705,  -0.3627566397190,  -0.2940605580807,  -0.3734591901302,  -0.0530807264149,  -0.2082165181637,  -0.5661571025848,   0.2031698673964,   0.0618096254766,  -0.1272780150175,  -0.3183623850346},
   {   0.2840771079063,   0.0256067831069,  -0.3346078693867,   0.0597924664617,  -0.0443219281733,   0.0091683603823,   0.2079414278269,   0.2448518276215,   0.1749824881554,  -0.4526804089546,   0.0189876910299,   0.4344225227833,   0.0196390617639},
   {  -0.2133944034576,   0.1535637378693,  -0.3358089625835,   0.1462099701166,  -0.3375893235207,   0.1040181592107,  -0.4206375777721,   0.2450698018074,  -0.1875586658716,  -0.0852980837226,   0.0047910762951,  -0.0824206545949,  -0.3337916135788},
   {   0.3738289177418,  -0.1426178216934,   0.5745490789413,  -0.2546570301056,  -0.3590407669544,   0.4373110830784,  -0.2248994857073,   0.2597685456276,   0.3157499730587,   0.3264051973820,   0.2164971232414,  -0.0082406736910,   0.1122550368309}};
  const float bias_GGH_odd_4[13] = {   0.0702702924609,  -0.0034324710723,   0.1011984422803,  -0.0142641514540,  -0.0031309353653,  -0.0234871990979,   0.0324486643076,   0.0216750428081,  -0.1023017242551,  -0.0087917894125,   0.1197050586343,   0.0215022377670,  -0.0543283112347};
  // Declare the arrays in the stack
  const float kernel_GGH_odd_5[13][1] = 
  {{   0.5774111747742},
   {   0.2007227540016},
   {   0.4549218118191},
   {  -0.4485927820206},
   {  -0.6511173844337},
   {  -0.2247069031000},
   {  -0.6809061765671},
   {   0.4098352193832},
   {  -0.3334217667580},
   {  -0.5742381811142},
   {   0.5936599969864},
   {  -0.4896680116653},
   {  -0.4743553698063}};
  const float bias_GGH_odd_5[1] = {   0.1115868166089};
  float buffer_in_GGH_odd[100];
  float buffer_out_GGH_odd[100];
  unsigned int i,j,c; 
 float mean_GGH_odd[100] = { 524.7413330078125,   0.3634985089302,   3.1177401542664,   1.1575839519501,   0.0063264570199,  -0.0169928800315, 124.2426300048828,  58.5017852783203,  -0.0014073805651,  -0.0138955321163,  -0.0023557520472,  -0.0061814840883,  74.7626495361328,  36.9241485595703,  -0.0086145969108,  -0.0209522396326,  82.4606781005859,   0.0340532884002, 109.0349807739258,  98.9228439331055, 285.6382446289062, 224.3840789794922, 198.0550842285156, 159.0251770019531,  53.9177017211914,   0.4940711855888,   0.4680215716362,   0.4494342803955,   0.6312085390091,   0.2969835102558,   0.4721918106079, 171.7479248046875, 394.7642822265625,   0.0000000000000,   0.0000000000000,   0.0000000000000};
 float sigma_GGH_odd[100] = { 557.3035278320312,   1.2420274019241,   1.7811443805695,   0.7813560962677,   2.0192506313324,   2.3721075057983, 100.4714126586914,  34.6426010131836,   1.8122875690460,   1.8139176368713,   1.1298402547836,   1.1466820240021,  52.4127655029297,  25.4452686309814,   1.8132447004318,   1.8131597042084,  60.9924812316895,   1.8190202713013,  39.8729286193848,  67.3220825195312, 222.0265045166016, 188.8608856201172, 158.0274047851562, 133.7681427001953,  57.5596466064453,   0.3904494345188,   0.3696804642677,   0.4080052375793,   0.4585592448711,   0.4307280480862,   0.3572290837765,  84.1784667968750, 220.0870056152344,   1.0000000000000,   1.0000000000000,   1.0000000000000};




  // Load the input in the buffer
  for (c = 0; c < 64; ++c) 
  buffer_in_GGH_odd[c] = (img[c]-mean_GGH_odd[c])/sigma_GGH_odd[c];
  // Processing layer 0 

            for (c = 0; c < 13; ++c ) 
              buffer_out_GGH_odd[c] = bias_GGH_odd_0[c];

            for (c = 0; c < 13; ++c )
              for (i = 0; i < 36; ++i)
                buffer_out_GGH_odd[c] += buffer_in_GGH_odd[i] * kernel_GGH_odd_0[i][c];

            norma_GGH_odd = 0;

            // Prepares for next layer 
            for (c = 0; c < 13; ++c )
              buffer_in_GGH_odd[c] = activation_GGH_odd_0(buffer_out_GGH_odd[c], norma_GGH_odd);


            
  // Processing layer 1 

            for (c = 0; c < 13; ++c ) 
              buffer_out_GGH_odd[c] = bias_GGH_odd_1[c];

            for (c = 0; c < 13; ++c )
              for (i = 0; i < 13; ++i)
                buffer_out_GGH_odd[c] += buffer_in_GGH_odd[i] * kernel_GGH_odd_1[i][c];

            norma_GGH_odd = 0;

            // Prepares for next layer 
            for (c = 0; c < 13; ++c )
              buffer_in_GGH_odd[c] = activation_GGH_odd_1(buffer_out_GGH_odd[c], norma_GGH_odd);


            
  // Processing layer 2 

            for (c = 0; c < 13; ++c ) 
              buffer_out_GGH_odd[c] = bias_GGH_odd_2[c];

            for (c = 0; c < 13; ++c )
              for (i = 0; i < 13; ++i)
                buffer_out_GGH_odd[c] += buffer_in_GGH_odd[i] * kernel_GGH_odd_2[i][c];

            norma_GGH_odd = 0;

            // Prepares for next layer 
            for (c = 0; c < 13; ++c )
              buffer_in_GGH_odd[c] = activation_GGH_odd_2(buffer_out_GGH_odd[c], norma_GGH_odd);


            
  // Processing layer 3 

            for (c = 0; c < 13; ++c ) 
              buffer_out_GGH_odd[c] = bias_GGH_odd_3[c];

            for (c = 0; c < 13; ++c )
              for (i = 0; i < 13; ++i)
                buffer_out_GGH_odd[c] += buffer_in_GGH_odd[i] * kernel_GGH_odd_3[i][c];

            norma_GGH_odd = 0;

            // Prepares for next layer 
            for (c = 0; c < 13; ++c )
              buffer_in_GGH_odd[c] = activation_GGH_odd_3(buffer_out_GGH_odd[c], norma_GGH_odd);


            
  // Processing layer 4 

            for (c = 0; c < 13; ++c ) 
              buffer_out_GGH_odd[c] = bias_GGH_odd_4[c];

            for (c = 0; c < 13; ++c )
              for (i = 0; i < 13; ++i)
                buffer_out_GGH_odd[c] += buffer_in_GGH_odd[i] * kernel_GGH_odd_4[i][c];

            norma_GGH_odd = 0;

            // Prepares for next layer 
            for (c = 0; c < 13; ++c )
              buffer_in_GGH_odd[c] = activation_GGH_odd_4(buffer_out_GGH_odd[c], norma_GGH_odd);


            
  // Processing layer 5 

            for (c = 0; c < 1; ++c ) 
              buffer_out_GGH_odd[c] = bias_GGH_odd_5[c];

            for (c = 0; c < 1; ++c )
              for (i = 0; i < 13; ++i)
                buffer_out_GGH_odd[c] += buffer_in_GGH_odd[i] * kernel_GGH_odd_5[i][c];

            norma_GGH_odd = 0;

            for(c=0;c<1;++c)
              norma_GGH_odd+=exp(buffer_out_GGH_odd[c]);

            // Prepares for next layer 
            for (c = 0; c < 1; ++c )
              buffer_in_GGH_odd[c] = activation_GGH_odd_5(buffer_out_GGH_odd[c], norma_GGH_odd);


            

      
    return buffer_in_GGH_odd[0];
      
    
   
      
    
}


#endif