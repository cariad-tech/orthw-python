# Copyright 2023 The ORTHW Project Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# SPDX-License-Identifier: Apache-2.0
# License-Filename: LICENSE
from __future__ import annotations

from rich import print

from orthw.utils.cmdgroups import command_group


def offending_licenses() -> None:
    print("\n[sandy_brown]This command is not implemented yet.[/sandy_brown]")


@command_group.command(
    context="SCAN_CONTEXT",
    name="offending-licenses",
    help="List licenses for which policy violations were found within initialized ORT result file.",
    short_help="List licenses for which policy violations were found within initialized ORT result file.",
)
def __offending_licenses() -> None:
    offending_licenses()
