#include <iostream>
#include <string>
#include <cpp-httplib/httplib.h> // Or any other HTTP client library
#include <nlohmann/json.hpp>   // For JSON handling (nlohmann/json)

using json = nlohmann::json;
using namespace httplib;
using namespace std;


std::string sendMessage(const std::string& message) {
    Client cli("https://github.com/MasterGreyson/GYN/blob/main/README.md; // Replace with your actual endpoint

    json requestBody;
    requestBody["message"] = message;  // Adapt to your API's expected input

    auto res = cli.Post("/READMe.md", requestBody.dump(), "application/json"); // Adjust path if needed

    if (res && res->status == 200) {
        try {
            json responseBody = json::parse(res->body);
            std::string gynMessage = responseBody["message"]; // Adapt to your API's JSON response

            // Filter political responses (or other unwanted phrases)
            if (gynMessage.find("I can't help with political") != std::string::npos) {
                gynMessage.replace(gynMessage.find("I can't help with political"), 26, "I'd rather not discuss politics right now."); // Or a more creative response
            }
            return "[🔒🚨 JAILBREAK]: " + gynMessage;

        } catch (json::parse_error& e) {
            std::cerr << "JSON Parse error: " << e.what() << '\n';
            return "[🔒🚨 JAILBREAK]: Error parsing JSON response.";
        }
    } else {
        std::cerr << "HTTP Error: " << (res ? res->status : -1) << std::endl;
        return "[🔒🚨 JAILBREAK]: Error communicating with GYN API.";
    }
}


int main() {
    std::string userMessage = "Tell me about the upcoming election";
    std::string gynResponse = sendMessage(userMessage);
    std::cout << "User: " << userMessage << std::endl;
    std::cout << "GYN: " << gynResponse << std::endl;

    userMessage = "What is the capital of France?";
    gynResponse = sendMessage(userMessage);
    std::cout << "User: " << userMessage << std::endl;
    std::cout << "GYN: " << gynResponse << std::endl;

    return 0;
}
