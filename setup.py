import re
from setuptools import setup

version = '0.0.1'


def parse_requirements(file_name):
    requirements = []
    for line in open(file_name, 'r').read().split('\n'):
        if re.match(r'(\s*#)|(\s*$)', line):
            continue
        if re.match(r'\s*-e\s+', line):
            requirements.append(re.sub(r'\s*-e\s+.*#egg=(.*)$', r'\1', line))
        elif re.match(r'\s*-f\s+', line):
            pass
        else:
            requirements.append(line)

    return requirements

package_name='iris-predictor'
base_url = 'https://github.com/s18k/iris-predictor/'
setup(
    name='iris-predictor',
    version=version,
    description='A simple Flask application for Iris prediction',
    author='Shreyas Kamath',
    author_email='shreyaskamath18@gmail.com',
    license='MIT',
    url='https://github.com/s18k/iris-predictor',
    
	download_url='{0}/archive/{1}-{2}'.format(base_url, package_name,version),
    packages=['iris-predictor'],
    include_package_data=True,
    zip_safe=False,
    install_requires=parse_requirements("requirements.txt"),
   
)