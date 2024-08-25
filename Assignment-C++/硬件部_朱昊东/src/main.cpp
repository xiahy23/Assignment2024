#include <fstream>
#include <iostream>
#include <string>

#include <nlohmann/json.hpp>
#include <httplib.h>

int main() {
  // Read the config.json file
  std::ifstream config_file("config.json");
  if (!config_file.is_open()) {
    std::cerr << "Unable to open config.json file" << std::endl;
    return 1;
  }

  nlohmann::json config;
  config_file >> config;
  std::string url = config["url"];

  // Use HTTP client library to access the URL
  httplib::Client cli(url.c_str());
  auto res = cli.Get("/");
  if (res && res->status == 200) {
    // Save the webpage content to the current directory
    std::ofstream output_file("output.html");
    if (!output_file.is_open()) {
      std::cerr << "Unable to create output.html file" << std::endl;
      return 1;
    }
    output_file << res->body;
    std::cout << "Webpage saved to output.html" << std::endl;
  } else {
    std::cerr << "Unable to access URL: " << url << std::endl;
    return 1;
  }

  return 0;
}