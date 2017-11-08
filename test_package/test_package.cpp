#include <spdlog/spdlog.h>

int main(int, char* [])
{
	auto console = spdlog::stdout_color_mt("console");
}
