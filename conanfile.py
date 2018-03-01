#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class spdlogConan(ConanFile):
    name = "spdlog"
    version = "0.16.3"
    description = "Fast C++ logging library"
    url = "https://github.com/bincrafters/conan-spdlog"
    homepage = "https://github.com/gabime/spdlog"
    license = "MIT"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    source_subfolder = "source_subfolder"
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"fmt_external": [True, False]}
    default_options = "fmt_external=False"

    def requirements(self):
        if self.options.fmt_external:
            self.requires("fmt/4.1.0@bincrafters/stable")

    def source(self):
        source_url = "https://github.com/gabime/spdlog"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self.source_subfolder)
    
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        
    def package(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.install()
        self.copy(pattern="LICENSE", dst='licenses', src=self.source_subfolder)

    def package_info(self):
        if self.options.fmt_external:
            self.cpp_info.defines.append("SPDLOG_FMT_EXTERNAL")
        if self.settings.os == "Linux":
            self.cpp_info.libs.append("pthread")
            
    def package_id(self):
        self.info.header_only()