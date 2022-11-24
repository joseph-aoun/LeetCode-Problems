class Solution {
public:
    vector<int> getRow(int rowIndex) {
        return pascal(rowIndex);
    }
    
    vector<int>pascal(int idx){
        if(idx == 0) return {1};
        
        vector<int> x = pascal(idx-1);
        vector<int>ans;
        ans.push_back(1);
        for(int i= 0; i < x.size() - 1; i++){
            ans.push_back(x[i] + x[i+1]);
        }
        ans.push_back(1);
        return ans;
    }
};