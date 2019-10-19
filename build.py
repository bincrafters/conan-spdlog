#!/usr/bin/env python

from bincrafters import build_template_default, build_template_header_only
import os

if __name__ == "__main__":
    header_only = os.getenv("CONAN_OPTIONS", False)

    builder = build_template_default.get_builder(pure_c=False)

    if header_only:
        builder = build_template_header_only.get_builder()

    builder.run()
