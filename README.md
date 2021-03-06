# rustici_software_cloud_v2
REST API used for SCORM Cloud integrations.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0
- Package version: 1.0.1
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import rustici_software_cloud_v2
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import rustici_software_cloud_v2
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import rustici_software_cloud_v2 as scorm_cloud
from datetime import datetime, timedelta

# Configure HTTP basic authorization: APP_NORMAL
scorm_cloud.configuration.username = 'SCORM_CLOUD_APP_ID'
scorm_cloud.configuration.password = 'SECRET_KEY_FOR_APP_ID'

# Then (optionally) further authenticate via Oauth2 token access
app_management_api = scorm_cloud.ApplicationManagementApi()

# get Oauth2 token with a life of 60 minutes and with permission to read the registrations api
token_request = {
# the expiry expected for token request must be in ISO-8601 format
    'expiry': (datetime.utcnow() + timedelta(minutes=60)).isoformat() + 'Z',
    'permissions': scorm_cloud.PermissionsSchema(['read:registration'])
}
response = app_management_api.create_token(token_request)

# further calls with this configuration will use Oauth2
scorm_cloud.configuration.access_token = response.result

registration_api = scorm_cloud.RegistrationApi()
registration_list = registration_api.get_registrations()

print(registration_list)
```

