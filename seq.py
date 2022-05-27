class seq:

    def __iter__(self):

        self.x=1

        return self

    def __next__(self):

        y=self.x

        self.x=self.x+1

        return y

s1=seq()

itr=iter(s1)

print(next(itr))

print(next(itr))

print(next(itr))

print(next(itr))

print(next(itr))

print(next(itr))

print(next(itr))
