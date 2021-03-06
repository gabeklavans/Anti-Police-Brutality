import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rpb",
    version="0.0.1",
    author="The APB project",
    author_email="APB.Program11@gmail.com",
    description="A program to help users report acts of police bruality to local authorities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kauii8school/Report-Police-Brutality",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "click==7.1.2",
        "Flask==1.1.2",
        "gunicorn==20.0.4",
        "itsdangerous==1.1.0",
        "Jinja2==2.11.2",
        "MarkupSafe==1.1.1",
        "Werkzeug==1.0.1",
    ],
)
