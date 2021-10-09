from setuptools import setup, find_packages

dist = setup(
    name="toxic_state_bot",
    version='0.0.1a4',
    author="kirillbiktya",
    author_email="kirillbiktya@gmail.com",
    description="Toxic Zone bot",
    url="https://github.com/kirillbiktya/toxic_state_bot",
    packages=find_packages(),
    include_package_data=True,
    # package_data={'sg_client.token_system': ['templates/*']},
    install_requires=open('requirements.txt', 'r').read().split('\n'),
    python_requires=">=3.8"
)
