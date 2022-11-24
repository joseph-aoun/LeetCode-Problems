class Solution {
    int ans = 0;
public:
    int diameterOfBinaryTree(TreeNode* root) {
        dfs(root);
        return ans;
    }
    
    int dfs(TreeNode* root){
        if(!root) return 0;
        
        int l = dfs(root->left);
        int r = dfs(root->right);
        
        ans = max(ans, l + r);
        
        return 1+ max(l, r);
    }
};