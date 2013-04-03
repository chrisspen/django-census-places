from distutils.core import setup

import census_places

setup(
    name='django-census-places',
    version=census_places.__version__,
    url='https://github.com/chrisspen/django-census-places',
    description='Use city (and census designated place) boundaries provided by the United States Census',
    author='Chris Spencer',
    author_email='chrisspen@gmail.com',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: GIS',
    ],
    packages=[
        'census_places',
        'census_places.management',
        'census_places.management.commands',
        'census_places.migrations',
    ]
)
