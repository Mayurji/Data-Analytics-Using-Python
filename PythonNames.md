
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



