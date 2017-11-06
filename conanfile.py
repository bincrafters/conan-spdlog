from conans import ConanFile, tools


class spdlogConan(ConanFile):
    name = "spdlog"
    version = "0.14.0"
    license = "MIT"
    url = "https://github.com/bincrafters/conan-spdlog"
    options = {"fmt_external": [True, False]}
    default_options = "fmt_external=False"

    def requirements(self):
        if self.options.fmt_external:
            self.requires("fmtlib/4.0.0@bincrafters/stable")

    def source(self):
        base_url = "https://github.com/gabime/spdlog/archive"
        zip_name = "v%s.zip" % self.version
        tools.download("%s/%s" % (base_url, zip_name), zip_name)
        tools.unzip(zip_name)
        #self.run("git clone https://github.com/gabime/spdlog.git")
        #self.run("cd spdlog && git checkout v%s" % self.version)

    def package(self):
        self.copy("*.h", dst="include", src="spdlog-%s/include" % (self.version))
        self.copy("*ostream.cc", dst="include", src="spdlog-%s/include" % (self.version))
        if not self.options.fmt_external:
            self.copy("*format.cc", dst="include", src="spdlog-%s/include" % (self.version))

    def package_info(self):
        if self.options.fmt_external:
            self.cpp_info.defines.append("SPDLOG_FMT_EXTERNAL")
