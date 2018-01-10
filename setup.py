from setuptools import find_packages, setup

setup(
    name='time-lapse',
    version='1.0.0.dev0',
    packages=find_packages(exclude=['tests', 'scripts']),
    include_package_data=True,
    zip_safe=False,
    url='https://github.com/153957/time-lapse',
    author='Arne de Laat',
    author_email='arne@delaat.net',
    description='Time-lapse movie assembly',
    long_description=open('README.rst').read(),
    keywords=[
        'ffmpeg',
        'photography',
        'time-lapse',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Multimedia :: Video :: Conversion',
    ],
    license='MIT',
    install_requires=[
        'ffmpeg-python',
        'graphviz',
    ],
    extras_require={
        'dev': [
            'check-manifest',
            'coverage',
            'flake8',
            'flake8-bugbear',
            'flake8-isort',
            'isort',
            'pep8-naming',
            'readme_renderer',
            'twine',
            'wheel',
        ],
    },
    test_suite='tests',
)
