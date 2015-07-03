import keyring

def awscli_initialize(events):
    events.register("session-initialized", session_initialized)

def cast_bool(value):
    return type(value) == type("") and value.lower() in ('1', 'yes', 'true', 'on')

def session_initialized(session, **kwargs):
    session.session_var_map["keyring"] = ("keyring", None, False, cast_bool)
    if session.get_config_variable("keyring") != False:
        if session.profile is not None:
            account = session.profile
        else:
            account = "default"

        key = keyring.get_password("awscli:key", account)
        secret = keyring.get_password("awscli:secret", account)

        session.set_credentials(key, secret)
