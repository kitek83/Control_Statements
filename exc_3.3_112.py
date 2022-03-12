#exc_3.3_112
"""belows code print < if row % 2 ==1 and of row % 2 = 0, print >"""
for row in range(10):
    for column in range(10):
        print('<' if row % 2 == 1 else '>', end=' ')
    print()

"""
 out:
> > > > > > > > > > 
< < < < < < < < < < 
> > > > > > > > > > 
< < < < < < < < < < 
> > > > > > > > > > 
< < < < < < < < < < 
> > > > > > > > > > 
< < < < < < < < < < 
> > > > > > > > > > 
< < < < < < < < < < 
"""