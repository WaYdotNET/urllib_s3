# urllib_s3

urllib_s3 is a urllib handler for s3 protocol


## Usage

install library

```bash
pip install urllib_s3

```

```python
from six.moves.urllib.request import urlopen
import urllib_s3

server_settings = {
    'server-url': {
        'access_key': 'xx',
        'secret_key': 'xxx',
        'secure': True
    }
}

urllib_s3.setup(server_settings)

# now you use s3 protocol
urlopen('s3://server-url/bucket/foo.png')

```

