#pragma once
#include <string>
#include <vector>
class TalkingClock
{
public:
	TalkingClock();
	~TalkingClock();
	
	void Input();

private:

	const std::string AM = "AM";
	const std::string PM = "PM";

	int _hourInt;
	int _minuteInt;

	std::vector<std::string> ParseString(std::string time);

	void Output(std::string hour, std::string min, std::string ampm);
	void BuildOutput(int hour, int minute);

	bool ValidateTime(std::string time);	
	bool CheckHours(std::string hour);
	bool CheckMinutes(std::string minute);
	bool isNumber(const std::string);
};


