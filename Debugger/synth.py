# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This script is used to synthesize generated parts of this library."""

import os
import synthtool as s
import synthtool.gcp as gcp
import logging

logging.basicConfig(level=logging.DEBUG)

gapic = gcp.GAPICGenerator()
common = gcp.CommonTemplates()

library = gapic.php_library(
    service='clouddebugger',
    version='v2',
    config_path='/google/devtools/artman_clouddebugger.yaml',
    artman_output_name='google-cloud-debugger-v2')

# copy all src including partial veneer classes
s.move(library / 'src')

# copy proto files to src also
s.move(library / 'proto/src/Google/Cloud/Debugger', 'src/')
s.move(library / 'tests/')

# copy GPBMetadata file to metadata
s.move(library / 'proto/src/GPBMetadata/Google/Devtools/Clouddebugger', 'metadata/')

# document and utilize apiEndpoint instead of serviceAddress
s.replace(
    "**/Gapic/*GapicClient.php",
    r"'serviceAddress' =>",
    r"'apiEndpoint' =>")
s.replace(
    "**/Gapic/*GapicClient.php",
    r"@type string \$serviceAddress\n\s+\*\s+The address",
    r"""@type string $serviceAddress
     *           **Deprecated**. This option will be removed in a future major release. Please
     *           utilize the `$apiEndpoint` option instead.
     *     @type string $apiEndpoint
     *           The address""")
s.replace(
    "**/Gapic/*GapicClient.php",
    r"\$transportConfig, and any \$serviceAddress",
    r"$transportConfig, and any `$apiEndpoint`")

# prevent proto messages from being marked final
s.replace(
    "src/V*/**/*.php",
    r"final class",
    r"class")

# fix year
s.replace(
    '**/Gapic/*GapicClient.php',
    r'Copyright \d{4}',
    'Copyright 2018')
s.replace(
    '**/V2/Controller2Client.php',
    r'Copyright \d{4}',
    'Copyright 2018')
s.replace(
    '**/V2/Debugger2Client.php',
    r'Copyright \d{4}',
    'Copyright 2018')
s.replace(
    'tests/**/V2/*Test.php',
    r'Copyright \d{4}',
    'Copyright 2018')
