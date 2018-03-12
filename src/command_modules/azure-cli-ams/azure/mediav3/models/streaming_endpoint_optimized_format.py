# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: skip-file
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .multi_bitrate_mp4_format import MultiBitrateMp4Format


class StreamingEndpointOptimizedFormat(MultiBitrateMp4Format):
    """A multi bitrate MP4 format that is optimized for use by streaming endpoint
    in Azure Media Services.

    :param filename_pattern: Gets or sets the pattern of the filename to use
     excluding the extension. REVIEW: List "macros" that can be used and give
     examples.
    :type filename_pattern: str
    :param odatatype: Constant filled by server.
    :type odatatype: str
    :param manifest_filename: Gets or sets the pattern of the manifest file
     name to use excluding the extension. REVIEW: List "macros" that can be
     used and give examples.
    :type manifest_filename: str
    :param output_files: Gets the list of output files.
    :type output_files: list[~encoding.models.OutputFile]
    """

    _validation = {
        'odatatype': {'required': True},
    }

    def __init__(self, filename_pattern=None, manifest_filename=None, output_files=None):
        super(StreamingEndpointOptimizedFormat, self).__init__(filename_pattern=filename_pattern, manifest_filename=manifest_filename, output_files=output_files)
        self.odatatype = '#Microsoft.Media.StreamingEndpointOptimizedFormat'
