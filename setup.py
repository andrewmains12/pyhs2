from distutils.core import setup

setup(
    name='pyhs2',
    version='0.1.1',
    author='Brad Ruderman',
    author_email='bradruderman@gmail.com',
    packages=['pyhs2', 'pyhs2/cloudera', 'pyhs2/TCLIService'],
    url='https://github.com/BradRuderman/pyhs2',
    license='LICENSE.txt',
    description='Python Hive Server 2 Client Driver',
    long_description=open('README.txt').read(),
    install_requires=[
        "sasl",
        "thrift",
    ],
)
