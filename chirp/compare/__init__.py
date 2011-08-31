# -*- coding: iso-8859-1 -*-
# -*- mode: python -*-
"""
Package containing modules for comparing vocalizations.

This component of chirp uses a plugin-based architecture to allow
users to define new comparison methods.  Plugins should register under
the entry point '%s', using the method name as a key.

base_comparison:  defines the methods needed by a comparison class
pitchdtw:         compare signals using dynamic time warping of pitch traces
spcc:             compare signals using spectrographic cross-correlation
masked_spcc:      SPCC + masking

Copyright (C) 2011 Dan Meliza <dmeliza@gmail.com>
Created 2011-08-02
"""

from .methods import entry_point_name as methods_entry_point

__doc__ = __doc__ % methods_entry_point

# Variables:
# End: