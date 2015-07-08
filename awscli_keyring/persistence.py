import keyring

def get_credentials(profile):
    key = keyring.get_password("awscli:key", profile)
    secret = keyring.get_password("awscli:secret", profile)

    return (key, secret)

def set_credentials(profile, key, secret):
    keyring.set_password("awscli:key", profile, key)
    keyring.set_password("awscli:secret", profile, secret)
