#include <iostream>
#include "spdlog/spdlog.h"

int main(int, char* [])
{
    namespace spd = spdlog;
    try
    {
        auto console = spd::stdout_color_mt("console");
        console->info("Welcome to spdlog!") ;
        console->info("An info message example {}..", 1);    

        // Formatting examples
        console->warn("Easy padding in numbers like {:08d}", 12);
        console->critical("Support for int: {0:d};  hex: {0:x};  oct: {0:o}; bin: {0:b}", 42);
        console->info("Support for floats {:03.2f}", 1.23456);
        console->info("Positional args are {1} {0}..", "too", "supported");
        console->info("{:<30}", "left aligned");
        console->info("{:>30}", "right aligned");
        console->info("{:^30}", "centered");
    }
    catch (const spd::spdlog_ex& ex)
    {
        std::cout << "Log failed: " << ex.what() << std::endl;
    }
}