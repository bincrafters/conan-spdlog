#include <spdlog/spdlog.h>
#ifdef SPDLOG_FMT_EXTERNAL
#include <fmt/format.h>
#endif

int main(int, char* [])
{
	auto console = spdlog::stdout_color_mt("console");
	console->info("Welcome to spdlog!");
	console->error("Some error message with arg{}..", 1);
	console->warn("Easy padding in numbers like {:08d}", 12);
#ifdef SPDLOG_FMT_EXTERNAL
	fmt::print("The format library says the answer is {}", 42);
#endif
}
