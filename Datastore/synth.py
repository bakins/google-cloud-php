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
    service='datastore',
    version='v1',
    config_path='/google/datastore/artman_datastore.yaml',
    artman_output_name='google-cloud-datastore-v1')

# copy all src including partial veneer classes
s.move(library / 'src')

# copy proto files to src also
s.move(library / 'proto/src/Google/Cloud/Datastore', 'src/')
s.move(library / 'tests/')

# copy GPBMetadata file to metadata
s.move(library / 'proto/src/GPBMetadata/Google/Datastore', 'metadata/')

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
    '**/V1/DatastoreClient.php',
    r'Copyright \d{4}',
    'Copyright 2018')
s.replace(
    'tests/**/V1/*Test.php',
    r'Copyright \d{4}',
    'Copyright 2018')

# Fix class references in gapic samples
for version in ['V1']:
    pathExpr = 'src/' + version + '/Gapic/DatastoreGapicClient.php'

    types = {
        '= new DatastoreClient': r'= new Google\\Cloud\\Datastore\\' + version + r'\\DatastoreClient',
        '= Mode::': r'= Google\\Cloud\\Datastore\\' + version + r'\\CommitRequest\\Mode::',
        'new PartitionId': r'new Google\\Cloud\\Datastore\\' + version + r'\\PartitionId',
    }

    for search, replace in types.items():
        s.replace(
            pathExpr,
            search,
            replace)
