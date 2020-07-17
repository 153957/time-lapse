import pathlib

from setuptools import find_packages, setup

readme = pathlib.Path(__file__).parent.joinpath('README.rst').read_text()

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
    long_description=readme,
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
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Video :: Conversion',
    ],
    license='MIT',
    install_requires=[
        'ffmpeg-python',
    ],
    extras_require={
        'graph': [
            'graphviz',
        ],
        'dev': [
            'check-manifest',
            'coverage',
            'flake8',
            'flake8-bugbear',
            'flake8-isort',
            'pep8-naming',
            'twine',
            'wheel',
        ],
    },
    entry_points={
        'console_scripts': [
            'timelapse = time_lapse.cli:main'
        ]
    },
    test_suite='tests',
)
