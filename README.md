# AWS CLI Keyring

AWS command line credentials from OS X Keychain, or anything else [Keyring](https://pypi.python.org/pypi/keyring) supports.

## Usage

Install with pip/setuptools:

```
pip install awscli-keyring
```

Turn it on in your config for the default profile, or specific profiles.

```
# ~/.aws/config
[plugins]
keyring = awscli_keyring

[default]
keyring = true
```

Add your key and secret to the keychain. The services should be `awsclikey` and `awscli:secret`, the account name should be your profile, or `default`, and the password should be your `AWS_ACCESS_KEY_ID` or `AWS_SECRET_KEY` respectively.

## TODO

 [ ] Setup commands
