from setuptools import setup, find_packages


setup(
    name='mango-web',
    version='0.1',
    description='The mango web backend.',
    long_description=open('README.md').read(),
    author='Laurie Clark-Michalek',
    author_email='lclarkmichalek@gmail.com',
    zip_safe=True,
    url='https://github.com/bluepeppers/mango-web',
    license='MIT',
    packages=find_packages(),
    keywords='',
    install_requires=[
        'mongoengine',
        'flask',
        'gunicorn',
        ],
    classifiers=[
        ]
    )
