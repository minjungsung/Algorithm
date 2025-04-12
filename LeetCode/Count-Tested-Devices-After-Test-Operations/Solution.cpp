Input: batteryPercentages = [1,1,2,1,3]
Output: 3
Explanation: Performing the test operations in order starting from device 0:
At device 0, batteryPercentages[0] > 0, so there is now 1 tested device, and batteryPercentages becomes [1,0,1,0,2].
At device 1, batteryPercentages[1] == 0, so we move to the next device without testing.
At device 2, batteryPercentages[2] > 0, so there are now 2 tested devices, and batteryPercentages becomes [1,0,1,0,1].
At device 3, batteryPercentages[3] == 0, so we move to the next device without testing.
At device 4, batteryPercentages[4] > 0, so there are now 3 tested devices, and batteryPercentages stays the same.
So, the answer is 3.
