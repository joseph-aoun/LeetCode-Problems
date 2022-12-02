class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        map<int, bool>visited;
        stack<int>st; st.push(source);
        map<int, vector<int>>edge;
        
        for(auto x : edges){
                edge[x[0]].push_back(x[1]);
                edge[x[1]].push_back(x[0]);
        }
        
        while(!st.empty()){
            int node = st.top(); st.pop();
            if(node == destination) return true;
            
            visited[node] = true;
            
            for(auto &y : edge[node]){
                if(!visited[y]) st.push(y);
            }
        }
        
        return false;
    }
};