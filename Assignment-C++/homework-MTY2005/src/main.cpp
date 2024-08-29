// main.cpp  
#include <iostream>  
#include <fstream>  
#include <nlohmann/json.hpp>  
#include "httplib.h"  
  
using json = nlohmann::json;  
  
int main() {  
    // 读取config.json  
    std::ifstream i("config.json");  
    json j;  
    i >> j;  
    std::string url = j["url"];  
  
    // 创建HTTP客户端并请求  
    httplib::Client cli(url);  
    auto res = cli.Get("/");  
  
    // 将网页保存到文件  
    std::ofstream out("page.html");  
    out << res->body;  
  
    return 0;  
}