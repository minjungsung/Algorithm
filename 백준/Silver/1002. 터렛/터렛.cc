#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	int num=0;
	int result = 0;
	int x1, y1, x2, y2, r1, r2= 0;
	double distance = 0;

	cin >> num;
	for (int i = 0; i < num; i++)
	{
		cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
		
		distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2)); // 두 점 사이의 거리를 이용하여 두 원의 중심좌표의 거리를 구함

		if (x1 == x2 && y1 == y2 && r1 == r2)
			result = -1; // 무한대로 만난다
		else if (abs(r1 - r2) <distance && r1 + r2 > distance)
			result = 2; // 두 점에서 만난다
		else if (r1 + r2 == distance)
			result = 1; // 외접하므로 한점에서 만난다.
		else if (abs(r1 - r2) == distance)
			result = 1; // 내접하므로 한점에서 만난다.
		else if (r1 + r2 < distance)
			result = 0; // 두 반지름의 합이 distance보다 짦기에 만나지 않는다.
		else if (abs(r1 - r2) > distance)
			result = 0; // 두 반지름의 차가 distance보다 길기에 만나지 않는다.

		cout << result << endl;
	}

}
