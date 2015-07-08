# AWS CLI Keyring

AWS command line credentials from OS X Keychain, or anything else [Keyring](https://pypi.python.org/pypi/keyring) supports.

## Usage

Install with pip/setuptools:

```
$ pip install awscli-keyring
```

Turn it on and add some credentials:

```
$ aws configure set plugins.keyring awscli_keyring
$ aws keyring add KEY
Secret: ...
$ aws --profile work ec2 describe-instances
{ ... }
```

This will change your config like:

```
# ~/.aws/config
[plugins]
keyring = awscli_keyring

[default]
keyring = true
```

You can also add keyring credentials for different profiles:

```
$ aws --profile work keyring add KEY
Secret: ...
$ aws --profile work ec2 describe-instances
{ ... }
```

Which adds the keyring flag to the profile configuration:

```
# ~/.aws/config
# ...

[profile work]
keyring = true
```

If you need to see the credentials, or use other command line tools that require credentials in your env, use show:

```
$ aws keyring show
AWS_ACCESS_KEY_ID="..."
AWS_SECRET_ACCESS_KEY="..."

$ eval "$(aws keyring show)"

$ env | grep AWS
AWS_ACCESS_KEY_ID="..."
AWS_SECRET_ACCESS_KEY="..."

# now do whatever... then close your shell.
```
