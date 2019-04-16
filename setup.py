from setuptools import setup, find_packages

setup(  name             = 'pytorch_complex_ops',
        version          = '0.0.1',
        description      = 'Pytorch Complex Autograd',
        author           = 'Michael Chen',
        author_email     = 'mchen0405@berkeley.edu',
        license          = 'BSD License',
        packages         = find_packages(),
        install_requires = 'torch',
     )
