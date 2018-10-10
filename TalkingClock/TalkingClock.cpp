#include "TalkingClock.h"
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cctype>
#include <unordered_map>


std::unordered_map<int, std::string> NumbersToWords =
{
	{ 00, "" },
	{ 0, "oh" },
	{ 1, "one" },
	{ 2, "two" },
	{ 3, "three" },
	{ 4, "four" },
	{ 5, "five" },
	{ 6, "six" },
	{ 7, "seven" },
	{ 8, "eight" },
	{ 9, "nine" },
	{ 10, "ten" },
	{ 11, "eleven" },
	{ 12, "twelve" },
	{ 13, "thirteen" },
	{ 14, "fourteen" },
	{ 15, "fifteen" },
	{ 16, "sixteen" },
	{ 17, "seventeen" },
	{ 18, "eightteen" },
	{ 19, "nineteen" },
	{ 20, "twenty" },
	{ 30, "thirty" },
	{ 40, "fourty" },
	{ 50, "fifty" },
};

TalkingClock::TalkingClock()
{
}


TalkingClock::~TalkingClock()
{
}

bool TalkingClock::ValidateTime(std::string time)
{
	std::vector<std::string> _results = ParseString(time);

	if (!_results.empty() && _results.size() == 2)
	{	
		if (CheckHours(_results[0]) && CheckMinutes(_results[1]))
		{
			BuildOutput(_hourInt, _minuteInt);			
		}
	}
	return false;
}

void TalkingClock::Input()
{
	std::string input = "00:00";
	std::string input1 = "01:30";
	std::string input2 = "12:05";
	std::string input3 = "14:01";
	std::string input4 = "20:29";
	std::string input5 = "21:00";

	ValidateTime(input);
	ValidateTime(input1);
	ValidateTime(input2);
	ValidateTime(input3);
	ValidateTime(input4);
	ValidateTime(input5);
}



void TalkingClock::Output(std::string hour, std::string min, std::string ampm)
{
	std::cout << "It's " << hour << min << ampm << std::endl;
}

void TalkingClock::BuildOutput(int hour, int minute)
{
	std::string AmPm;
	std::string hourString;
	std::string minuteString;

	if (hour > 12)
	{
		hour -= 12;
		AmPm = PM;
	}
	else
	{
		AmPm = AM;
		if (hour == 00)
		{
			hour = 01;
		}
	}

	hourString += NumbersToWords[hour] + " ";

	if (minute / 10 != 0)
	{

		if (minute < 10 || minute > 20)
		{
			minuteString += NumbersToWords[minute - (minute % 10)] + " ";
			if (minute % 10 != 0)
			{
				minuteString += NumbersToWords[minute % 10] + " ";
			}
		}
		else
		{
			minuteString += NumbersToWords[minute] + " ";
		}
		
	}
	else if(minute % 10 != 0)
	{
		minuteString += "oh " + NumbersToWords[minute] + " ";
	}
	
	Output(hourString, minuteString, AmPm);
}

std::vector<std::string> TalkingClock::ParseString(std::string time)
{
	std::istringstream ss(time);
	std::string token;
	std::vector<std::string> temp;

	while (std::getline(ss, token, ':'))
	{
		try
		{
			temp.push_back(token);
		}
		catch (const std::exception &e)
		{
			std::cout << e.what();
		}
	}

	return temp;
}

bool TalkingClock::CheckHours(std::string hour)
{
	if (isNumber(hour))
	{
		int tempHour = std::stoi(hour);
		if (tempHour < 24)
		{
			_hourInt = tempHour;
			return true;
		}
	}
	return false;
}

bool TalkingClock::CheckMinutes(std::string minute)
{
	if (isNumber(minute))
	{
		int tempMin = std::stoi(minute);
		if (tempMin < 60)
		{
			_minuteInt = tempMin;
			return true;
		}
	}
	return false;
}

bool TalkingClock::isNumber(const std::string s)
{
	return !s.empty() && std::find_if(s.begin(), s.end(), [](char c) {return !std::isdigit(c); }) == s.end();
}

