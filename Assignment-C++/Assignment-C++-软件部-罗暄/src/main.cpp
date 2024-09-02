#include <iostream>
#include <fstream>
#include <string>
#include "nlohmann/json.hpp"
#include "httplib.h"

int main(int argc, char** argv) {

    // read config.json and get url
    std::ifstream file("config.json");
    nlohmann::json config;
    file >> config;
    file.close();
    std::string url = config["url"].get<std::string>();

    // use http client to visit url and save html
    if (!url.empty())
    {
        httplib::Client client(url);
        auto res = client.Get("/");
        std::ofstream f("output.html");
        f << res->body;
        f.close();
    }

    return 0;
}
