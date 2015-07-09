import sys
import os

from botocore.compat import OrderedDict

from awscli.customizations.commands import BasicCommand
from awscli.customizations.configure import ConfigFileWriter

from . import persistence

def build_command_table(command_table, session, **kwargs):
    command_table["keyring"] = KeyringCommand(session)

"""Add credentials for a profile to keyring"""
class AddCommand(BasicCommand):
    NAME = "add"

    DESCRIPTION = "Add credentials for the current profile to keyring"

    SYNOPSIS = "add <key> [secret]"

    ARG_TABLE = [
        {"name": "key", "positional_arg": True, "nargs": "?", "action": "store", "help_text": "AWS_ACCESS_KEY_ID; if omitted you will be asked to enter the secret using a password prompt."},
        {"name": "secret", "positional_arg": True, "nargs": "?", "action": "store", "help_text": "AWS_SECRET_ACCESS_KEY; if omitted you will be asked to enter the secret using a password prompt."},
    ]

    def _run_main(self, parsed_args, parsed_globals):
        current_key = None
        current_secret = None
        masked_current_secret = None
        if self._session._credentials:
            current_key = self._session._credentials.access_key
            current_secret = self._session._credentials.secret_key
            if current_secret is not None:
                masked_current_secret = "*" * (len(current_secret) - 4) + current_secret[-4:]

        key = parsed_args.key
        if key is None:
            import getpass
            key = getpass.getpass("AWS Access Key ID [%s]: " % current_key)
            if key is None or key == "":
                key = current_key

        secret = parsed_args.secret
        if secret is None:
            import getpass
            secret = getpass.getpass("AWS Secret Access Key [%s]: " % masked_current_secret)
            if secret is None or secret == "":
                secret = current_secret

        profile = self._session.profile
        if profile is None:
            profile = "default"
            config_section = "default"
        else:
            config_section = "profile {0}".format(profile)

        persistence.set_credentials(profile, key, secret)

        config_update = {"__section__": config_section, "keyring": "true"}
        config_filename = os.path.expanduser(self._session.get_config_variable("config_file"))

        config_writer = ConfigFileWriter()
        config_writer.update_config(config_update, config_filename)

        return 0

class ShowCommand(BasicCommand):
    NAME = "show"

    DESCRIPTION = "Show credentials for current profile like environment variables\n\nUseful for sourcing in a shell or using as a wrapper for command line programs which expect credentials in environment variables."

    EXAMPLES = "Command::\n\n    aws keyring show\n\nOutput::\n\n    AWS_ACCESS_KEY_ID=\"ABC...\"\n    AWS_SECRET_ACCESS_KEY=\"123...\""

    def _run_main(self, parsed_args, global_args):
        if self._session._credentials:
            print('AWS_ACCESS_KEY_ID="{0}"'.format(self._session._credentials.access_key))
            print('AWS_SECRET_ACCESS_KEY="{0}"'.format(self._session._credentials.secret_key))
            if getattr(self._session._credentials, "token", None) is not None:
                print('AWS_SESSION_TOKEN="{0}"'.format(self._session._credentials.token))
            return 0
        else:
            sys.stderr.write('There are no credentials to show.\n')
            return 1

"""Keyring commands"""
class KeyringCommand(BasicCommand):
    NAME = "keyring"

    DESCRIPTION = "keyring management"

    SUBCOMMANDS = [
        {"name": "add", "command_class": AddCommand},
        {"name": "show", "command_class": ShowCommand},
    ]

    def _run_main(self, parsed_args, parsed_globals):
        self._display_help(parsed_args, parsed_globals)
        return 1
