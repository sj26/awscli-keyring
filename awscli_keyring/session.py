from botocore.exceptions import ConfigNotFound, ProfileNotFound

from . import persistence

def cast_bool(value):
    return type(value) == type("") and value.lower() in ('1', 'yes', 'true', 'on')

def initialized(session, **kwargs):
    session.session_var_map["keyring"] = ("keyring", None, False, cast_bool)

    try:
        if session.get_config_variable("keyring") != False:
            if session.profile is not None:
                profile = session.profile
            else:
                profile = "default"

            key, secret = persistence.get_credentials(profile)

            session.set_credentials(key, secret)

    except (ConfigNotFound, ProfileNotFound):
        pass
