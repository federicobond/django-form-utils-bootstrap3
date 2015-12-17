import setuptools

setuptools.setup(
    name="django-form-utils-bootstrap3",
    version="0.1.0",
    url="https://github.com/federicobond/django-form-utils-bootstrap3",

    author="Federico Bond",
    author_email="federicobond@gmail.com",

    description="Render forms with fieldsets using Bootstrap markup via django-form-utils and django-bootstrap3",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
    ],
)
