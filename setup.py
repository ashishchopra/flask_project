from setuptools import setup

setup(
    name='flask_app',
    version='1.0',
    long_description=__doc__,
    packages=['flask_app'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
        'Flask-Migrate'
    ]
)
