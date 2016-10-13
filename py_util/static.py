class Test(object):
    i = 0
    def p(self):
        print self.i


a = Test
a.i = 1
b = a()
b.p()


print(b[i])
