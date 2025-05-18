from setuptools import setup, find_packages


setup(
    name='get-gitlab-issues',
    version='2025.5.180909',
    author='Eugene Evstafev',
    author_email='chigwel@gmail.com',
    description='A Python package for extracting issues from GitLab repositories.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/chigwell/get-gitlab-issues',
    packages=find_packages(),
    install_requires=[
        'requests==2.32.3',
        'python-gitlab==4.7.0'
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)