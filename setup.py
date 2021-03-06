from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(
    version='0.2.0',
    name='FuelSDKWrapper',
    description='Simplify and improve the FuelSDK for Salesforce Marketing Cloud (ExactTarget)',
    long_description=readme,
    author='Seb Angel',
    author_email='seb.angel.force@gmail.com',
    py_modules=['FuelSDKWrapper'],
    packages=[],
    url='https://github.com/seb-angel/FuelSDK-Python-Wrapper',
    license='MIT',
    install_requires=[
        'FuelSDK>=0.9.3',
        'suds-jurko>=0.6',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2.7',
    ],
)