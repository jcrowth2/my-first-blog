# Django Girls Tutorial
# https://tutorial.djangogirls.org/en/python_introduction/

def hi(name):
    print("Hi " + name)

hi('Jack')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('Next girl')