# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DefaultKey(Model):
    """Class to specify properties of default content key for each encryption
    scheme.

    :param label: Label can be used to specify Content Key when creating
     Stremaing Locator
    :type label: str
    :param policy_name: Policy used by Default Key
    :type policy_name: str
    """

    _attribute_map = {
        'label': {'key': 'label', 'type': 'str'},
        'policy_name': {'key': 'policyName', 'type': 'str'},
    }

    def __init__(self, label=None, policy_name=None):
        super(DefaultKey, self).__init__()
        self.label = label
        self.policy_name = policy_name
