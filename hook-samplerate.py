# ------------------------------------------------------------------
# Copyright (c) 2020 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE.GPL.txt, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------

from PyInstaller.utils.hooks import collect_dynamic_libs
from PyInstaller.compat import is_darwin, is_win
if is_win:
 binaries = collect_dynamic_libs('samplerate',search_patterns=["*.dll"])
elif is_darwin:
 binaries = collect_dynamic_libs('samplerate',search_patterns=["*.dylib"])