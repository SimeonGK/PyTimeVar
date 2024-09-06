import setuptools

setuptools.setup(
    name='PyTimeVar',
    version="0.0.2",
    python_requires=">=3.9",
    packages=['PyTimeVar', 'tests'],
    install_requires=['numpy', 'pandas', 'matplotlib',
                      'scipy', 'time', 'datetime', 'statsmodels', 'tqdm'],
    license_files=('LICENSE.txt',),
)
