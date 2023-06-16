#!/usr/bin/env python3

import libcalamares
from libcalamares.utils import target_env_call

def remove_airos(config):
    user = "airos"
    target_env_call(['deluser', '--remove-all-files', user])

def run():
    return remove_airos(libcalamares.job.configuration)
