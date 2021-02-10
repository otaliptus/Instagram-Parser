// This extremely fundamental template is the first one
// that I used string manipulation to parse the data.
// I am/will not use this in this project, it's just a basic template.


#include <iostream>

int main(){
    char c; 
    freopen("messages.json", "r", stdin);
    freopen("template.txt", "w", stdout);
    std::string s;   int yaz = 1;
    while( (c = getchar())!=EOF){
        s.push_back(c);
        if(c == '}'){
            std::string check = "participants";
            int bak = s.find(check);
            if(bak == std::string::npos){
                if(yaz){
                    std::cout << s << "\n";  s.clear();  continue;
                }
                s.clear();  continue;
            }
            std::string k = "{\"participants\": [\"user_1\", \"user_2\"]";
            std::string t = "{\"participants\": [\"user_2\", \"user_1\"]";
            int n = s.find(k), m = s.find(t);
            if(n == std::string::npos and m == std::string::npos){
                s.clear();  yaz = 0;    continue;
            }
            std::cout << s << "\n";  s.clear(); yaz = 1;
        }
    }
}