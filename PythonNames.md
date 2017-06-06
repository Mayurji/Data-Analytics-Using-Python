
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
    
    
    
