#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools, RunEnvironment
import os


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        for use_find_package in [True, False]:
            cmake = CMake(self)
            cmake.definitions['USE_FIND_PACKAGE'] = use_find_package
            cmake.configure()
            cmake.build()

    def test(self):
        bin_path = os.path.join("bin", "test_package")
        self.run(bin_path, run_environment=True)
