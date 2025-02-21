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

from pathlib import Path

import click

from orthw.utils import logging
from orthw.utils.cmdgroups import command_group
from orthw.utils.process import run


def scan(
    ort_file: str,
    output_dir: str | None = None,
    format_: str = "JSON",
    docker: bool = False,
) -> int:
    """Runs ORT Scanner on given source code directory to detect licenses and copyrights

    Args:
        ort_file (str): Analyzer file.
        format_ (str, optional): Format of the result output. Defaults to "JSON".
        output_dir (str | None, optional): Specified output dir or cuurent dir
        docker (bool, optional): If is runing on docker. Defaults to False.
    Returns:
        int | Container: Status code for local runs or Container object for docker runs
    """

    if not Path(ort_file):
        logging.error(f"Path for ort file {ort_file} do not exists. Bailing out.")
        return 1
    workdir = Path(ort_file).parent.absolute()

    logging.debug(f"Running ort scan on {workdir} with ort file {ort_file} and format {format_}")

    args: list[str] = [
        "ort",
        "scan",
        "--output-formats",
        format_,
        "--ort-file",
        Path(ort_file).name,
    ]

    # Execute external run
    return run(
        args=args,
        is_docker=docker,
        workdir=workdir,
        output_dir=Path(output_dir) if output_dir else workdir,
    )


@command_group.command(
    name="scan",
    help=(
        "Runs ORT Scanner on given source code directory to via external scanners " "detect licenses and copyrights."
    ),
    short_help=(
        "Runs ORT Scanner on given source code directory to via external scanners " "detect licenses and copyrights."
    ),
    context="NO_SCAN_CONTEXT",
    context_settings={
        "allow_extra_args": True,
        "ignore_unknown_options": True,
    },
)
@click.option("--format", "-f", "format_", default="JSON")
@click.option("--output-dir", type=click.Path(exists=False), required=False)
@click.option("--ort-file", type=click.Path(exists=False), required=True)
def __scan(ctx: click.Context, ort_file: str, format_: str, output_dir: str) -> None:
    scan(ort_file=ort_file, format_=format_, output_dir=output_dir, docker=bool("docker" in ctx.obj))
