# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps

# pylint: disable=line-too-long, too-many-lines

helps['ams'] = """
    type: group
    short-summary: Manage Azure Media Services resources.
"""

helps['ams account'] = """
    type: group
    short-summary: Manage Azure Media Services accounts.
"""

helps['ams account create'] = """
    type: command
    short-summary: Create an Azure Media Services account.
"""

helps['ams account list'] = """
    type: command
    short-summary: List Azure Media Services accounts for the entire subscription.
"""

helps['ams account show'] = """
    type: command
    short-summary: Show the details of an Azure Media Services account.
"""

helps['ams storage'] = """
    type: group
    short-summary: Manage secondary storage for an Azure Media Services account.
"""

helps['ams storage add'] = """
    type: command
    short-summary: Attach a secondary storage to an Azure Media Services account.
"""

helps['ams storage remove'] = """
    type: command
    short-summary: Detach a secondary storage from an Azure Media Services account. 
"""

helps['ams sp'] = """
    type: group
    short-summary: Manage service principal and role based access for an Azure Media Services account.
"""

helps['ams sp create'] = """
    type: command
    short-summary: Create a service principal and configure its access to an Azure Media Services account.
    parameters:
        - name: --account-name
          short-summary: The name of the Azure Media Services account within the resource group.
        - name: --name
          short-summary: The app name or app URI to associate the RBAC with. If not present, a name like '{amsaccountname}-access-sp' will be generated.
        - name: --password
          short-summary: The password used to log in. Also known as 'Client Secret'. If not present, a random secret will be generated.
        - name: --role
          short-summary: The role of the service principal.
        - name: --xml
          short-summary: Flag that enables xml output format.
    examples:
        - name: Create a service principal with password and configure its access to an Azure Media Services account. Output will be in xml format.
          text: >
            az ams sp create -a {myamsaccount} -g {myresourcegroup} -n {mySpName} -password {mySpPassword} --role {rol} --xml
    """