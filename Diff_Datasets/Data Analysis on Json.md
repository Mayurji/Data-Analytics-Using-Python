            >>> import json
            >>> #path = 'import json'
            >>> path = '/Users/mayurjain/Documents/Python Data Analysis Practice/usagov.txt'
            >>> #open(path).readline()
            ... records = [json.loads(line) for line in open(path)]
            >>> records[0]

                  {'a': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.78 Safari/535.11', 'c': 'US', 'nk': 1, 'tz': 'America/New_York', 'gr': 'MA', 'g': 'A6qOVH', 'h': 'wfLQtf', 'l': 'orofrog', 'al': 'en-US,en;q=0.8', 'hh': '1.usa.gov', 'r': 'http://www.facebook.com/l/7AQEFzjSi/1.usa.gov/wfLQtf', 'u': 'http://www.ncbi.nlm.nih.gov/pubmed/22415991', 't': 1331923247, 'hc': 1331822918, 'cy': 'Danvers', 'll': [42.576698, -70.954903]}

            >>> records[0]['tz']
                  'America/New_York'
            >>> time_zones = [rec['tz'] for rec in records if 'tz' in rec]
            >>> time_zones[:10]
                  ['America/New_York', 'America/Denver', 'America/New_York', 'America/Sao_Paulo', 'America/New_York', 'America/New_York', 'Europe/Warsaw', '', '', '']
            >>> def get_counts(seq):
            ...     counts = {}
            ...     for x in seq:
            ...             if x in counts:
            ...                     counts[x] += 1
            ...             else:
            ...                     counts[x] = 1
            ...     return counts
            ... 
            >>> counts = get_counts(time_zones)
            >>> counts['America/New_York']
                  1251
            >>> len(time_zones)
                  3440
            >>> def topcount(count_dict,n=10):
            ...     vkp = [(count,tz) for tz, count in count_dict.items()]
            ...     vkp.sort()
            ...     return vkp[-n:]
            ... 
            >>> topcount(counts)
                  [(33, 'America/Sao_Paulo'), (35, 'Europe/Madrid'), (36, 'Pacific/Honolulu'), (37, 'Asia/Tokyo'), (74, 'Europe/London'), (191, 'America/Denver'), (382, 'America/Los_Angeles'), (400, 'America/Chicago'), (521, ''), (1251, 'America/New_York')]
            >>> from collections import Counter
            >>> counts = Counter(time_zones)
            >>> counts.most_common(10)
                  [('America/New_York', 1251), ('', 521), ('America/Chicago', 400), ('America/Los_Angeles', 382), ('America/Denver', 191), ('Europe/London', 74), ('Asia/Tokyo', 37), ('Pacific/Honolulu', 36), ('Europe/Madrid', 35), ('America/Sao_Paulo', 33)]
            >>> # Counting Time Zones with pandas
            ... 
            >>> from pandas import DataFrame, Series
            >>> import pandas as pd
            >>> frame = DataFrame(records)
            >>> frame

                           _heartbeat_                                                  a  \
                    0              NaN  Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKi...   
                    1              NaN                             GoogleMaps/RochesterNY   
                    2              NaN  Mozilla/4.0 (compatible; MSIE 8.0; Windows NT ...   
                    3              NaN  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8)...   
                    4              NaN  Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKi...   
                    5              NaN  Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKi...   
                    6              NaN  Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1...   
                    7              NaN  Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/2...   
                    8              NaN  Opera/9.80 (X11; Linux zbov; U; en) Presto/2.1...   
                    9              NaN  Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKi...   
                    10             NaN  Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.2)...   
                    11             NaN  Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4...   
                    12             NaN  Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.2)...   
                    13    1.331923e+09                                                NaN   
                    14             NaN  Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US...   
                    15             NaN  Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1...   
                    16             NaN  Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1...   
                    17             NaN  Mozilla/5.0 (Macintosh; Intel Mac OS X 10.5; r...   
                    18             NaN                             GoogleMaps/RochesterNY   
                    19             NaN  Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKi...   
                    20             NaN  Mozilla/5.0 (compatible; MSIE 9.0; Windows NT ...   
                    21             NaN  Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6...   
                    22             NaN  Mozilla/4.0 (compatible; MSIE 8.0; Windows NT ...   
                    23             NaN  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3)...   
                    24             NaN  Mozilla/5.0 (Windows; U; Windows NT 5.1; es-ES...   
                    25             NaN  Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1...   
                    26             NaN  Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1...   
                    27             NaN  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8)...   
                    28             NaN  Mozilla/5.0 (iPad; CPU OS 5_0_1 like Mac OS X)...   
                    29             NaN  Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X...   
                    ...            ...                                                ...   
                    3530           NaN  Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1...   
                    3531           NaN  Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6...   
                    3532           NaN  Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.2)...   
                    3533           NaN  Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) A...   
                    3534           NaN  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8)...   
                    3535           NaN  Mozilla/5.0 (Windows NT 5.1; rv:10.0.2) Gecko/...   
                    3536           NaN  Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; e...   
                    3537           NaN  Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.2)...   
                    3538           NaN  Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Ma...   
                    3539           NaN    Mozilla/5.0 (compatible; Fedora Core 3) FC3 KDE   
                    3540           NaN  Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKi...   
                    3541           NaN  Mozilla/5.0 (X11; U; OpenVMS AlphaServer_ES40;...   
                    3542           NaN  Mozilla/5.0 (compatible; MSIE 9.0; Windows NT ...   
                    3543  1.331927e+09                                                NaN   
                    3544           NaN  Mozilla/5.0 (Windows NT 6.1; WOW64; rv:5.0.1) ...   
                    3545           NaN  Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.2)...   
                    3546           NaN  Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Ma...   
                    3547           NaN  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8)...   
                    3548           NaN  Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Ma...   
                    3549           NaN  Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKi...   
                    3550           NaN  Mozilla/4.0 (compatible; MSIE 8.0; Windows NT ...   
                    3551           NaN  Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKi...   
                    3552           NaN  Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US...   
                    3553           NaN  Mozilla/4.0 (compatible; MSIE 7.0; Windows NT ...   
                    3554           NaN  Mozilla/4.0 (compatible; MSIE 7.0; Windows NT ...   
                    3555           NaN  Mozilla/4.0 (compatible; MSIE 9.0; Windows NT ...   
                    3556           NaN  Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1...   
                    3557           NaN                             GoogleMaps/RochesterNY   
                    3558           NaN                                     GoogleProducer   
                    3559           NaN  Mozilla/4.0 (compatible; MSIE 8.0; Windows NT ...   
                        Europe/Stockholm  http://www.nasa.gov/mission_pages/WISE/main/in...  
                    3550     America/New_York  http://www.nlm.nih.gov/medlineplus/news/fullst...  
                    3551                       http://www.nasa.gov/mission_pages/nustar/main/...  
                    3552      America/Chicago  http://travel.state.gov/passport/passport_5535...  
                    3553     America/New_York  http://www.shrewsbury-ma.gov/egov/gallery/1341...  
                    3554     America/New_York  http://www.shrewsbury-ma.gov/egov/gallery/1341...  
                    3555     America/New_York  http://www.fda.gov/AdvisoryCommittees/Committe...  
                    3556      America/Chicago  http://www.okc.gov/PublicNotificationSystem/Fo...  
                    3557       America/Denver        http://www.monroecounty.gov/etc/911/rss.php  
                    3558  America/Los_Angeles                http://www.ahrq.gov/qual/qitoolkit/  
                    3559     America/New_York  http://herndon-va.gov/Content/public_safety/Pu...  

                    [3560 rows x 18 columns]
            >>> frame['tz'][:10]
                    0     America/New_York
                    1       America/Denver
                    2     America/New_York
                    3    America/Sao_Paulo
                    4     America/New_York
                    5     America/New_York
                    6        Europe/Warsaw
                    7                     
                    8                     
                    9                     
                    Name: tz, dtype: object
            >>> tz_count = frame['tz'].value_counts()
            >>> tz_count[:10]
                    America/New_York       1251
                                            521
                    America/Chicago         400
                    America/Los_Angeles     382
                    America/Denver          191
                    Europe/London            74
                    Asia/Tokyo               37
                    Pacific/Honolulu         36
                    Europe/Madrid            35
                    America/Sao_Paulo        33
                    Name: tz, dtype: int64
            >>> clean_tz = frame['tz'].fillna('Missing')
            >>> clean_tz.value_counts()
                    America/New_York                  1251
                                                       521
                    America/Chicago                    400
                    America/Los_Angeles                382
                    America/Denver                     191
                    Missing                            120
                    Europe/London                       74
                    Asia/Tokyo                          37
                    Pacific/Honolulu                    36
                    Europe/Madrid                       35
                    America/Sao_Paulo                   33
                    Europe/Berlin                       28
                    Europe/Rome                         27
                    America/Rainy_River                 25
                    Europe/Amsterdam                    22
                    America/Indianapolis                20
                    America/Phoenix                     20
                    Europe/Warsaw                       16
                    America/Mexico_City                 15
                    Europe/Stockholm                    14
                    Europe/Paris                        14
                    America/Vancouver                   12
                    Pacific/Auckland                    11
                    America/Puerto_Rico                 10
                    Europe/Moscow                       10
                    Europe/Helsinki                     10
                    Europe/Oslo                         10
                    Europe/Prague                       10
                    Asia/Hong_Kong                      10
                    Asia/Calcutta                        9
                                                      ... 
                    America/Chihuahua                    2
                    Europe/Uzhgorod                      1
                    Asia/Nicosia                         1
                    Europe/Sofia                         1
                    America/Argentina/Cordoba            1
                    Asia/Kuching                         1
                    Europe/Volgograd                     1
                    Africa/Johannesburg                  1
                    Europe/Ljubljana                     1
                    Australia/Queensland                 1
                    Asia/Riyadh                          1
                    America/Argentina/Buenos_Aires       1
                    America/Tegucigalpa                  1
                    Africa/Lusaka                        1
                    Asia/Yekaterinburg                   1
                    America/Argentina/Mendoza            1
                    America/Santo_Domingo                1
                    Europe/Skopje                        1
                    America/St_Kitts                     1
                    America/Costa_Rica                   1
                    America/Montevideo                   1
                    America/Caracas                      1
                    Asia/Novosibirsk                     1
                    America/Monterrey                    1
                    Africa/Casablanca                    1
                    America/La_Paz                       1
                    Asia/Pontianak                       1
                    America/Lima                         1
                    Asia/Manila                          1
                    America/Mazatlan                     1
                    Name: tz, Length: 98, dtype: int64
            >>> clean_tz[clean_tz == ''] = 'unknown'
            >>> tz_count = clean_tz.value_counts()
            >>> tz_count[:10]
                    America/New_York       1251
                    unknown                 521
                    America/Chicago         400
                    America/Los_Angeles     382
                    America/Denver          191
                    Missing                 120
                    Europe/London            74
                    Asia/Tokyo               37
                    Pacific/Honolulu         36
                    Europe/Madrid            35
                    Name: tz, dtype: int64
            frame.head()
                       _heartbeat_                                                  a  \
                    0          NaN  Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKi...   
                    1          NaN                             GoogleMaps/RochesterNY   
                    2          NaN  Mozilla/4.0 (compatible; MSIE 8.0; Windows NT ...   
                    3          NaN  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8)...   
                    4          NaN  Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKi...   

                                   al   c          cy       g  gr       h            hc  \
                    0  en-US,en;q=0.8  US     Danvers  A6qOVH  MA  wfLQtf  1.331823e+09   
                    1             NaN  US       Provo  mwszkS  UT  mwszkS  1.308262e+09   
                    2           en-US  US  Washington  xxr3Qb  DC  xxr3Qb  1.331920e+09   
                    3           pt-br  BR        Braz  zCaLwp  27  zUtuOu  1.331923e+09   
                    4  en-US,en;q=0.8  US  Shrewsbury  9b6kNl  MA  9b6kNl  1.273672e+09   

                              hh   kw         l                        ll   nk  \
                    0  1.usa.gov  NaN   orofrog   [42.576698, -70.954903]  1.0   
                    1       j.mp  NaN     bitly  [40.218102, -111.613297]  0.0   
                    2  1.usa.gov  NaN     bitly     [38.9007, -77.043098]  1.0   
                    3  1.usa.gov  NaN  alelex88  [-23.549999, -46.616699]  0.0   
                    4     bit.ly  NaN     bitly   [42.286499, -71.714699]  0.0   

                                                                       r             t  \
                    0  http://www.facebook.com/l/7AQEFzjSi/1.usa.gov/...  1.331923e+09   
                    1                           http://www.AwareMap.com/  1.331923e+09   
                    2                               http://t.co/03elZC4Q  1.331923e+09   
                    3                                             direct  1.331923e+09   
                    4                http://www.shrewsbury-ma.gov/selco/  1.331923e+09   

                                      tz                                                  u  
                    0   America/New_York        http://www.ncbi.nlm.nih.gov/pubmed/22415991  
                    1     America/Denver        http://www.monroecounty.gov/etc/911/rss.php  
                    2   America/New_York  http://boxer.senate.gov/en/press/releases/0316...  
                    3  America/Sao_Paulo            http://apod.nasa.gov/apod/ap120312.html  
                    4   America/New_York  http://www.shrewsbury-ma.gov/egov/gallery/1341...  
            >>> frame['a'][1]
                    'GoogleMaps/RochesterNY'
            >>> frame['a'][0]
                    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.78 Safari/535.11'
            >>> results = Series([x.split()[0] for x in frame.a.dropna()])
            >>> results[:5]
                    0               Mozilla/5.0
                    1    GoogleMaps/RochesterNY
                    2               Mozilla/4.0
                    3               Mozilla/5.0
                    4               Mozilla/5.0
                    dtype: object
            >>> results.value_counts()[:8]
                    Mozilla/5.0                 2594
                    Mozilla/4.0                  601
                    GoogleMaps/RochesterNY       121
                    Opera/9.80                    34
                    TEST_INTERNET_AGENT           24
                    GoogleProducer                21
                    Mozilla/6.0                    5
                    BlackBerry8520/5.0.0.681       4
                    dtype: int64
            >>> cframe = frame[frame.a.notnull()]
            >>> import numpy as np
            >>> os = np.where(cframe['a'].str.contains('Windows'),'windows','not windows')
            >>> os[:5]
                    array(['windows', 'not windows', 'windows', 'not windows', 'windows'], 
                          dtype='<U11')
            >>> by_tz_os = cframe.groupby(['tz',os])
            >>> agg_count = by_tz_os.size().unstack().fillna(0)
            >>> agg_count[:10]
                                                    not windows  windows
                    tz                                                  
                                                          245.0    276.0
                    Africa/Cairo                            0.0      3.0
                    Africa/Casablanca                       0.0      1.0
                    Africa/Ceuta                            0.0      2.0
                    Africa/Johannesburg                     0.0      1.0
                    Africa/Lusaka                           0.0      1.0
                    America/Anchorage                       4.0      1.0
                    America/Argentina/Buenos_Aires          1.0      0.0
                    America/Argentina/Cordoba               0.0      1.0
                    America/Argentina/Mendoza               0.0      1.0
            >>> indexer = agg_count.sum(1).argsort()
            >>> indexer[:10]
                    tz
                                                    24
                    Africa/Cairo                      20
                    Africa/Casablanca                 21
                    Africa/Ceuta                      92
                    Africa/Johannesburg               87
                    Africa/Lusaka                     53
                    America/Anchorage                 54
                    America/Argentina/Buenos_Aires    57
                    America/Argentina/Cordoba         26
                    America/Argentina/Mendoza         55
                    dtype: int64
            >>> count_subset = agg_count.take(indexer)[-10:]
            >>> count_subset
                                         not windows  windows
                    tz                                       
                    America/Sao_Paulo           13.0     20.0
                    Europe/Madrid               16.0     19.0
                    Pacific/Honolulu             0.0     36.0
                    Asia/Tokyo                   2.0     35.0
                    Europe/London               43.0     31.0
                    America/Denver             132.0     59.0
                    America/Los_Angeles        130.0    252.0
                    America/Chicago            115.0    285.0
                                               245.0    276.0
                    America/New_York           339.0    912.0
            >>> indexer[:5]
                    tz
                                           24
                    Africa/Cairo           20
                    Africa/Casablanca      21
                    Africa/Ceuta           92
                    Africa/Johannesburg    87
                    dtype: int64
                    >>> 
