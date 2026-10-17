#include<iostream>
#include<string>

using namespace std;

int main(){
    string secret = "GMBH|D0ef_Cb4t1d~";
    string input;

    cout << "Nhap flag: ";
    cin >> input;

    for (int i = 0; i < input.length(); i++){
    input[i] += 1;
    }

    if (input == secret){
        cout << "Chinh xac! Ban da tim ra flag.";
    }
    else {
        cout << "Sai mat khau!";
    }

    return 0;
}