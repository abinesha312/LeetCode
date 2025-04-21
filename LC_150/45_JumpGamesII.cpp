#include <iostream>
#include <vector>
using namespace std;

class solution{
    public: 
        int jump(vector<int>& nums) {
            int n = nums.size();
            if (n <= 1) return 0;
            int jumps = 0, currentEnd = 0, farthest = 0;
            for (int i = 0; i < n - 1; i++) {
                farthest = max(farthest, i + nums[i]);
                if (i == currentEnd) {
                    jumps++;
                    currentEnd = farthest;
                }
            }
            return jumps;
        }
};

// Example usage
int main() {
    solution sol;
    vector<int> nums = {2, 3, 1, 1, 4};
    cout << sol.jump(nums) << endl; // Output: 2
    return 0;
}


//Example input: [2,3,0,1,4]
//Expected output : 2
//Actual output : 2

//Time complexity: O(n) where n is the length of the input array nums.
//Space complexity: O(1) as we are using only a constant amount of space for variables.
