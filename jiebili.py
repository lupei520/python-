class axe:
    import time
    from fractions import Fraction
    def Hello(self):
        self.a=input("请输入第一个比例的前项(不知道为X):")
        self.b=input('请输入第一个比例的后项(不知道为X):')
        self.c=input('请输入第二个比例的前项(不知道为X):')
        self.d=input('请输入第二个比例的后项(不知道为X):')
        if self.a=='X' or self.a=='x' or self.a=='y' or self.a=='Y' or self.a=='a' or self.a=='A' or self.a=='z' or self.a=='Z':
            self.b=float(self.b)
            self.c=float(self.c)
            self.d=float(self.d)
            self.important=float(self.b*self.c)
            self.a=float(self.important/self.d)
            print('X等于:',self.a)
        elif self.b=='x' or self.b=='X' or self.b=='y' or self.b=='Y' or self.b=='a' or self.b=='A' or self.b=='z' or self.b=='Z':
            self.a=float(self.a)
            self.c=float(self.c)
            self.d=float(self.d)
            self.important=float(self.a*self.d)
            self.b=float(self.important/self.c)
            print('X等于:',self.b)
        elif self.c=='x' or self.c=='X' or self.c=='y' or self.c=='Y' or self.c=='a' or self.c=='A' or self.c=='z' or self.c=='Z':
            self.a=float(self.a)
            self.b=float(self.b)
            self.d=float(self.d)
            self.important=float(self.a*self.d)
            self.c=float(self.important/self.b)
            print('X等于:',self.c)
        elif self.d=='x' or self.d=='X' or self.d=='y' or self.d=='Y' or self.d=='a' or self.d=='A' or self.d=='z' or self.d=='Z':
            self.a=float(self.a)
            self.b=float(self.b)
            self.c=float(self.c)
            self.important=float(self.b*self.c)
            self.d=float(self.important/self.a)
            print('X等于:',self.d)
        self.time.sleep(10)
    def fenshu(self):
        from fractions import Fraction
        super_big_ask=input('a:b=c:d中谁是x:')
        if super_big_ask=='a':
            self.bask=input('请输入b是否为分数:')
            if self.bask=='是':
                self.b_part1=int(input('请输入第一个比例的后项的分子:'))
                self.b_part2=int(input('请输入第一个比例的后项的分母:'))
                self.b=Fraction(self.b_part1,self.b_part2)
            elif self.bask=='不是' or self.bask=='否':
                self.b=float(input('请输入第一个比的后项的值:'))
            self.cask=input('请输入c是否为分数:')
            if self.cask=='是':
                self.c_part1=int(input('请输入第一个比例的后项的分子:'))
                self.c_part2=int(input('请输入第一个比例的后项的分母:'))
                self.c=Fraction(self.c_part1,self.c_part2)
            elif self.cask=='否' or self.cask=='不是':
                self.c=float(input('请输入第二个比的前项的值:'))
            self.dask=input('请输入d是否为分数:')
            if self.dask=='是':
                self.d_part1=int(input('请输入第二个比例的后项的分子:'))
                self.d_part2=int(input('请输入第二个比例的后项的分母:'))
                self.d=Fraction(self.d_part1,self.d_part2)
            elif self.dask=='否' or self.dask=='不是':
                self.d=float(input('请输入第二个比的后项的值:'))
            self.important=self.b*self.c
            self.a=self.important/self.d
            print('X等于(小数形式):',self.a)
            self.a=str(self.important/self.d)
            print('X等于(分数形式):',Fraction(self.a))
        if super_big_ask=='b':
            self.aask=input('请输入a是否为分数:')
            if self.aask=='是':
                self.a_part1=int(input('请输入第一个比例的前项的分子:'))
                self.a_part2=int(input('请输入第一个比例的前项的分母:'))
                self.a=Fraction(self.a_part1,self.a_part2)
            elif self.aask=='不是' or self.aask=='否' or self.aask=='No':
                self.a=float(input('请输入第一个比的前项的值:'))
            self.cask=input('请输入c是否为分数:')
            if self.cask=='是':
                self.c_part1=int(input('请输入第二个比例的前项的分子:'))
                self.c_part2=int(input('请输入第二个比例的前项的分母:'))
                self.c=Fraction(self.c_part1,self.c_part2)
            elif self.cask=='否' or self.cask=='不是':
                self.c=float(input('请输入第二个比的前项的值:'))
            self.dask=input('请输入d是否为分数:')
            if self.dask=='是':
                self.d_part1=int(input('请输入第二个比例的后项的分子:'))
                self.d_part2=int(input('请输入第二个比例的后项的分母:'))
                self.d=Fraction(self.d_part1,self.d_part2)
            elif self.dask=='否' or self.dask=='不是':
                self.d=float(input('请输入第二个比的前项的值:'))
            self.important=self.a*self.d
            self.b=self.important/self.c
            print('X等于(小数形式):',self.b)
            self.b=str(self.b)
            print('X(分数形式)等于:',Fraction(self.b))
        if super_big_ask=='c':
            self.aask=input('请输入a是否为分数:')
            if self.aask=='是':
                self.a_part1=int(input('请输入第一个比例的前项的分子:'))
                self.a_part2=int(input('请输入第一个比例的前项的分母:'))
                self.a=Fraction(self.a_part1,self.a_part2)
            elif self.aask=='不是' or self.aask=='否':
                self.a=float(input('请输入第一个比的前项的值:'))
            self.bask=input('请输入b是否为分数:')
            if self.bask=='是':
                self.b_part1=int(input('请输入第一个比例的后项的分子:'))
                self.b_part2=int(input('请输入第一个比例的后项的分母:'))
                self.b=Fraction(self.b_part1,self.b_part2)
            elif self.bask=='否' or self.bask=='不是':
                self.b=float(input('请输入第二个比的前项的值:'))
            self.dask=input('请输入d是否为分数:')
            if self.dask=='是':
                self.d_part1=int(input('请输入第二个比例的后项的分子:'))
                self.d_part2=int(input('请输入第二个比例的后项的分母:'))
                self.d=Fraction(self.d_part1,self.d_part2)
            elif self.dask=='否' or self.dask=='不是':
                self.d=float(input('请输入第二个比的后项的值:'))
            self.important=self.a*self.d
            self.c=self.important/self.b
            print('X等于(小数形式):',self.c)
            self.c=str(self.c)
            print('X等于(分数形式):',Fraction(self.c))
        if super_big_ask=='d':
            self.aask=input('请输入a是否为分数:')
            if self.aask=='是':
                self.a_part1=int(input('请输入第一个比例的前项的分子:'))
                self.a_part2=int(input('请输入第一个比例的前项的分母:'))
                self.a=Fraction(self.a_part1,self.a_part2)
            elif self.aask=='不是' or self.aask=='否':
                self.a=float(input('请输入第一个比的前项的值:'))
            self.bask=input('请输入b是否为分数:')
            if self.bask=='是':
                self.b_part1=int(input('请输入第一个比例的后项的分子:'))
                self.b_part2=int(input('请输入第一个比例的后项的分母:'))
                self.b=Fraction(self.b_part1,self.b_part2)
            elif self.bask=='否' or self.bask=='不是':
                self.b=float(input('请输入第二个比的前项的值:'))
            self.cask=input('请输入c是否为分数:')
            if self.cask=='是':
                self.c_part1=int(input('请输入第二个比例的前项的分子:'))
                self.c_part2=int(input('请输入第二个比例的前项的分母:'))
                self.c=Fraction(self.c_part1,self.c_part2)
            elif self.cask=='否' or self.cask=='不是':
                self.c=float(input('请输入第二个比的前项的值:'))
            self.important=self.b*self.c
            self.d=self.important/self.a
            print('X等于(小数形式):',self.d)
            self.d=str(self.d)
            print('X等于(分数形式):',Fraction(self.d))
        self.time.sleep(10)
ask=input('请输入需要计算分数吗：')
if ask =='否' or ask=='不用' or ask=='不需要':
    test=axe()
    test.Hello()
if ask=='需要' or ask=='是' or ask=='1':
    test=axe()
    test.fenshu()
