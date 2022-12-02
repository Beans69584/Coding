#include <iostream>
#include <ctime>
#include <string>
#include <sstream>
#include <iomanip>
#include <Windows.h>

using namespace std;

int main()
{
    while (true) {
        time_t now = time(0);
        tm *ltm = localtime(&now);
        int year = 1900 + ltm->tm_year;
        int month = 11;
        int day = 25;
        tm christmas = {0, 0, 0, day, month, year - 1900};
        time_t xmas = mktime(&christmas);
        double difference = difftime(xmas, now);
        int days = difference / (60 * 60 * 24);
        difference -= days * (60 * 60 * 24);
        int hours = difference / (60 * 60);
        difference -= hours * (60 * 60);
        int minutes = difference / 60;
        difference -= minutes * 60;
        int seconds = difference;
        system("cls");
        cout << "Until Christmas 2022\n" << days << " days, " << hours << " hours, " << minutes << " minutes, and " << seconds << " seconds" << endl;
        Sleep(1000);
    }
}