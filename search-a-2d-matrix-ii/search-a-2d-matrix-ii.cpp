class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int start = 0, end = matrix[0].size() - 1;
        while(start < matrix.size() && end >=0){
            if(matrix[start][end] == target)  return true;
            
            matrix[start][end] > target? end-- : start++;
        }
        
        return false;
    }
};