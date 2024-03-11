from setuptools import setup, find_packages

setup(
    name='MyTeahc',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # 任何依赖项都在这里列出
        'httpcat-sdk',
        'myhttpcat',
        'myhcat',
    ],
    author='dwge1',
    author_email='rich_dwge@outlook.com',
    description='MyTeahc',
    license='MIT',
    keywords='MyTeahc',
    url='https://github.com/MyTeahc/MyTeahc',
    download_url='https://github.com/MyTeahc/MyTeahc',
    project_url='https://github.com/MyTeahc/MyTeahc',
    "project_urls":{
        "Source":"https://github.com/MyTeahc/MyTeahc",
    }
)

