from conans import ConanFile


class spdlogConan(ConanFile):
    name = "spdlog"
    version = "0.14.0"
    license = "MIT"
    url = "https://github.com/memsharded/conan-spdlog"
    options = {"fmt_external": [True, False]}
    default_options = "fmt_external=False"

    def requirements(self):
        if self.options.fmt_external:
            self.requires("fmt/3.0.1@memsharded/stable")

    def source(self):
        self.run("git clone https://github.com/gabime/spdlog.git")
        self.run("cd spdlog && git checkout v%s" % self.version)

    def package(self):
        self.copy("*.h", dst="include", src="spdlog/include")
        self.copy("*ostream.cc", dst="include", src="spdlog/include")
        if not self.options.fmt_external:
            self.copy("*format.cc", dst="include", src="spdlog/include")

    def package_info(self):
        if self.options.fmt_external:
            self.cpp_info.defines.append("SPDLOG_FMT_EXTERNAL")
