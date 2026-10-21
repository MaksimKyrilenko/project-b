from setuptools import setup, find_packages

setup(
    name='project-b-utils',
    version='1.1.0',
    packages=find_packages(exclude=['tests*', 'src*']),
    author='Ivan Ivanov',
    description='Утилиты для работы с датами, строками, файлами и логированием',
    python_requires='>=3.8',
)
