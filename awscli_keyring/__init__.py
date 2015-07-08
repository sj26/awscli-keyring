from . import commands, session

def awscli_initialize(events):
    events.register("building-command-table.main", commands.build_command_table)
    events.register("session-initialized", session.initialized)
