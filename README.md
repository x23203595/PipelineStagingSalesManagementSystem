
Pipeline Staging in a Sales Management System

A Web Application intended for customers or clients from contrasting domains seeking to upskill business outcomes with the supplementary contribution of 'Pipeline Stages'. This is a demonstration intended to prioritize the the Customer - Key Priority relationship in a cloud-ready environment.


## Dependencies Required

**Front End:** HTML5, CSS

**Back End:** Python 3.9.16 

**Web Framework:** Django 4.2.11

**Database:** SQLite 3.40.0

Custom Libraries for PipelineStagingLibrary:
- setuptools 69.5.1
- wheel 0.43.0
- twine 5.0.0

Custom Library for template-based PDF:
- xhtml2pdf 0.2.15

Static Code Analysis:
- Pylint 2.17.4

**setup.py:** custom-pipeline-stages-manager 0.1.0

Custom Packages for AWS S3 Facilitation:
- boto3 1.34.88
- s3transfer 0.10.1
- botocore 1.34.88


## Deployment Steps

**Continuous Integration / Continuous Delivery (CI / CD)**:

AWS CodePipeline: x23203595PipelineStageCPP

Pipeline Type: V1

Execution Mode: Superseded

Service Role : aws_codepipeline_service_role

Source Provider : GitHub Version 1

Repository : x23203595/PipelineStagingSalesManagementSystem

Branch : Main

Build Provider : AWS CodeBuild

Project Name : x23203595PipelineStageCodeBuild

OS: Ubuntu

Image: Ubuntu

Image: aws/codebuild/standard:7.0

Role ARN: CodeBuildServiceRole

Buildspec name : 'Use a buildspec file'

Deploy Provider : AWS Elastic Beanstalk

Application Name: x23203595QuizzBean

Environment Name: x23203595PipelineStagingNineteen

**Library**:

Hierarchy and Structure:

```bash
PipelineStagingLibrary
              -------> .git
              -------> _dist
              -------> dist
              -------> env
              -------> pipeline_staging_properties_pkg
		              ----> __init__.py
		              ----> pipeline_staging_properties.py
              -------> pkg_newfinalcustom_pipeline_staging_final.egg-info
              -------> tests
              -------> CHANGELOG.txt
              -------> LICENSE
              -------> README.md
              -------> setup.py
```

Build the library i.e. generate the distribution package:

```bash
  python3 -m pip install --upgrade setuptools wheel
```

Upload/publish the distribution package files with twine:

```bash
  python3 -m pip install --upgrade twine
```

Publish the library to PyPI:

```bash
  python3 -m twine upload --repository pypi dist/*
  twine upload dist/*
```
Install (i.e. via pip) the distribution package/library:

```bash
  python3 -m pip install --index-url https://pypi.org/simple --no-deps custom-pipeline-stages-manager==0.1.0
```
Information about the installed library:

```bash
  pip list
  pip show custom-pipeline-stages-manager
```






## Configuration Files

- .ebextensions/django.config
Setup File for SalesManagementSystemProject to AWS Elastic Beanstalk :
```bash
 x23203595PipelineStagingNineteen
```

- buildspec.yml
Build Specification reference for CodeBuild :
```bash
 x23203595PipelineStageCodeBuild
```
- setup.py
Metadata of Custom Library :
```bash
 custom-pipeline-stages-manager
 version=0.1.0
```
- requirements.txt
List of installed packages and libraries for SalesManagementSystemProject :

```bash
asgiref==3.8.1
backports.tarfile==1.1.0
build==1.2.1
certifi==2024.2.2
cffi==1.16.0
charset-normalizer==3.3.2
cryptography==42.0.5
Django==4.1.7
docutils==0.20.1
idna==3.6
importlib_metadata==7.1.0
importlib_resources==6.4.0
jaraco.classes==3.4.0
jaraco.context==5.3.0
jaraco.functools==4.0.0
jeepney==0.8.0
keyring==25.1.0
markdown-it-py==3.0.0
mdurl==0.1.2
more-itertools==10.2.0
nh3==0.2.17
packaging==24.0
pillow==10.3.0
pkginfo==1.10.0
custom-pipeline-stages-manager==0.1.0
pycparser==2.22
Pygments==2.17.2
pyproject_hooks==1.0.0
pytz==2024.1
readme_renderer==43.0
requests==2.31.0
requests-toolbelt==1.0.0
rfc3986==2.0.0
rich==13.7.1
SecretStorage==3.3.3
sqlparse==0.5.0
tomli==2.0.1
twine==5.0.0
typing_extensions==4.10.0
urllib3==2.2.1
xhtml2pdf==0.2.15
zipp==3.18.1
```