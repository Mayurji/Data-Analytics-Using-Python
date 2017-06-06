
    import pandas as pd
    babyNames = pd.read_csv('D:\names.csv')
    print(babyNames.head())
    
       year     name   percent  sex
    0  1880     John  0.081541  boy
    1  1880  William  0.080511  boy
    2  1880    James  0.050057  boy
    3  1880  Charles  0.045167  boy
    4  1880   George  0.043292  boy
    
    print(babyNames.groupby('sex').percent.sum())
    
    sex
    boy     118.141068
    girl    112.632536
    Name: percent, dtype: float64
    
    print(babyNames['year'].value_counts())
    
    1919    2000
    1983    2000
    1953    2000
    1954    2000
    1955    2000
    1956    2000
    ...     ...
    
    
    print(babyNames.groupby('year').count())
    
          name  percent   sex
    year                     
    1880  2000     2000  2000
    1881  2000     2000  2000
    1882  2000     2000  2000
    1883  2000     2000  2000
    1884  2000     2000  2000
    1885  2000     2000  2000
    ...   ...      ...   ..    

    print(babyNames.groupby('year').sex.value_counts())
    
    year  sex 
    1880  boy     1000
          girl    1000
    1881  boy     1000
          girl    1000
    1882  boy     1000
          girl    1000
    1883  boy     1000
          girl    1000
          ...     ...
          
          
    popularNames = pd.DataFrame(babyNames.sort_index(by = 'percent', ascending = False))
    popularNames.filter(items=['name','sex','percent'])
    
        name    sex     percent
    0   john    boy     0.81..
    1   william boy     0.80..
    .   ..      ..      ...
    
    popularBoyName = popularNames.loc[popularNames['sex'] == 'boy']
  
    all the records with sex as 'boy' is filtered 
    
    
    popularGirlName = popularNames.loc[popularNames['sex'] == 'girl']
    
    all the records with sex as 'girl' is filtered
    
    year2007 = popularGirlName.loc[popularGirlName['year'] == 2007][:5]
    print(year2007)
    
            year      name   percent   sex
    256000  2007     Emily  0.009155  girl
    256001  2007  Isabella  0.009049  girl
    256002  2007      Emma  0.008688  girl
    ...     ..          ..  ...         ..
    
    
    totalBirth = popularNames.pivot_table('percent',index=['name','year'],aggfunc=sum)

    name     year
    Aaden    2008    0.000442
    Aaliyah  1994    0.000744
             1995    0.000653
             1996    0.000434
             1997    0.000911
             1998    0.000722
             1999    0.000559
             2000    0.000750
             2001    0.001694
             2002    0.002422
             2003    0.001831
             2004    0.001726
             2005    0.001703
             2006    0.001790
             2007    0.001870
             2008    0.001939
    Aarav    2008    0.000101
    Aaron    1880    0.000861
             1881    0.000868
             1882    0.000697
             1883    0.000933
             1884    0.000790
             1885    0.000759
             1886    0.000722
             1887    0.000714
             1888    0.000693
             1889    0.000714
             1890    0.000802
             1891    0.000631
             1892    0.000723
                      ...   
    Zula     1903    0.000266
             1904    0.000253
             1905    0.000197
             1906    0.000185
             1907    0.000213
                .......
