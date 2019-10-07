#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from conans import CMake, ConanFile, tools
from conans.errors import ConanInvalidConfiguration


class SpdlogConan(ConanFile):
    name = "spdlog"
    version = "1.4.1"
    description = "Fast C++ logging library"
    url = "https://github.com/bincrafters/conan-spdlog"
    homepage = "https://github.com/gabime/spdlog"
    author = "Bincrafters <bincrafters@gmail.com>"
    topics = ("conan", "spdlog", "logging", "header-only")
    license = "MIT"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt", "patches/*"]
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False],
               "header_only": [True, False], "wchar_support": [True, False]}
    default_options = {"shared": False, "fPIC": True, "header_only": False,
                       "wchar_support": False}

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        if self.options.header_only:
            del self.options.shared
            del self.options.fPIC
        elif self.settings.os == "Windows" and self.options.shared:
            raise ConanInvalidConfiguration("spdlog shared lib is not yet supported under windows")
        if self.settings.os != "Windows" and self.options.wchar_support:
            raise ConanInvalidConfiguration("wchar is not yet supported under windows")

    def requirements(self):
        self.requires("fmt/5.3.0@bincrafters/stable")

    def source(self):
        tools.get("{0}/archive/v{1}.tar.gz".format(self.homepage, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["SPDLOG_BUILD_EXAMPLE"] = False
        cmake.definitions["SPDLOG_BUILD_EXAMPLE_HO"] = False
        cmake.definitions["SPDLOG_BUILD_TESTS"] = False
        cmake.definitions["SPDLOG_BUILD_TESTS_HO"] = False
        cmake.definitions["SPDLOG_BUILD_BENCH"] = False
        cmake.definitions["SPDLOG_FMT_EXTERNAL"] = True
        cmake.definitions["SPDLOG_BUILD_SHARED"] = not self.options.header_only and self.options.shared
        cmake.definitions["SPDLOG_WCHAR_SUPPORT"] = self.options.wchar_support
        cmake.definitions["SPDLOG_INSTALL"] = True
        cmake.configure()
        return cmake

    def build(self):
        if self.options.header_only:
            tools.patch(base_path=self._source_subfolder,
                        patch_file=os.path.join("patches", "0001-header-only.patch"))
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy("LICENSE", dst='licenses', src=self._source_subfolder)
        cmake = self._configure_cmake()
        cmake.install()

    def package_id(self):
        if self.options.header_only:
            self.info.header_only()

    def package_info(self):
        if self.options.header_only:
            self.cpp_info.defines = ["SDPLOG_HEADER_ONLY", "SPDLOG_FMT_EXTERNAL"]
        else:
            self.cpp_info.libs = tools.collect_libs(self)
            self.cpp_info.defines = ["SDPLOG_COMPILED_LIB", "SPDLOG_FMT_EXTERNAL"]
        if self.options.wchar_support:
            self.cpp_info.defines.append("SPDLOG_WCHAR_TO_UTF8_SUPPORT")
        if tools.os_info.is_linux:
            self.cpp_info.libs.append("pthread")
