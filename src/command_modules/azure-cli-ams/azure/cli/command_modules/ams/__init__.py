# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader
from azure.cli.core.commands import CliCommandType

import azure.cli.command_modules.ams._help  # pylint: disable=unused-import

class MediaServicesCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        super(MediaServicesCommandsLoader, self).__init__(cli_ctx=cli_ctx)

    def load_command_table(self, args):
        super(MediaServicesCommandsLoader, self).load_command_table(args)
        from azure.cli.command_modules.ams.commands import load_command_table
        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
        super(MediaServicesCommandsLoader, self).load_arguments(command)
        from azure.cli.command_modules.ams._params import load_arguments
        load_arguments(self, command)


COMMAND_LOADER_CLS = MediaServicesCommandsLoader
