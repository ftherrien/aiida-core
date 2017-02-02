install_requires = [
    'python-dateutil==2.6.0',
    'python-mimeparse==0.1.4',
    'django==1.7.4',
    'django_extensions==1.5',
    'tzlocal==1.3',
    'pytz==2014.10',
    'django-celery==3.1.16',
    'celery==3.1.17',
    'billiard==3.3.0.19',
    'anyjson==0.3.3',
    'supervisor==3.1.3',
    'meld3==1.0.0',
    'numpy==1.12.0',
    'plum==0.7.5',
    'SQLAlchemy==1.0.12',
    'SQLAlchemy-Utils==0.31.2',
    'ujson==1.35',
    'enum34==1.1.2',
    'voluptuous==0.8.11',
    'aldjemy==0.6.0',
    'passlib==1.7.1',
    'validate_email==1.3',
    'click==6.7',
    'tabulate==0.7.5',
    'ete3==3.0.0b35',
    'uritools==1.0.2',
    'psycopg2==2.6.1',
    'amqp==1.4.9',
    # When you change version of setuptools, pip and, if present, wheels
    # update also the travis.yml file
    'setuptools==34.1.0',
    'pip==9.0.1',
    'wheel==0.29.0'
]

extras_require = {
    'verdi_shell': ['ipython'],
    'ssh': [
        'paramiko==1.15.2',
        'ecdsa==0.13',
        'pycrypto==2.6.1',
    ],
    'REST': [
        'flask==0.10.1',
        'flask_restful==0.3.5',
        'flask-cors==3.0.1',
        'pyparsing==2.1.10',
        'pattern==2.6',
        'Flask-SqlAlchemy==2.1',
        'SQLAlchemy-migrate==0.10.0',
        'marshmallow-sqlalchemy==0.10.0',
        'flask-marshmallow==0.7.0',
        'itsdangerous==0.24',
        'flask-httpauth==3.2.0',
        'flask-cache==0.13.1',
        'python-memcached==1.58',
    ],
    'docs': [
        'Sphinx==1.5.2',
        'pygments==2.2.0',
        'docutils==0.13.1',
        'jinja2==2.9.5',
        'markupsafe==0.23',
        'sphinx_rtd_theme==0.1.9',
    ],
    'atomic_tools':[
        'pyspglib',#has no easily accessible version number
        'pymatgen==4.5.3',
        'ase==3.12.0',
        'PyMySQL==0.7.9', #required by ICSD tools,
        'PyCifRW==3.6.2.1',
    ]
}

dependency_links = [
    'https://bitbucket.org/aiida_team/plum/get/v0.7.5.zip#egg=plum-0.7.5',
]
