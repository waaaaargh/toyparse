from distutils.core import setup

setup(
    name='toyparse',
    version='0.1',

    description='Parser library for Python',
    author='Johannes Fürmann',
    author_email='johannes@weltraumpflege.org',
    url='https://github.com/waaaaargh/toyparse',

    py_modules=[
        'toyparse.parser',
        'toyparse.character',
        'toyparse.combinator'
    ]
)
