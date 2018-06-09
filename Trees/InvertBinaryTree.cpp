//A generic TreeNode struct
  struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode(int x) : val(x), left(NULL), right(NULL) {}
  };

class TreeUtil{
public:
    TreeNode* invertTree(TreeNode* root) {
        if (!root)
            return nullptr;
        TreeNode *temp = root->left;
        root->left = root->right; 
        root->right = temp;
        if (root->left)
            invertTree(root->left);
        if(root->right)
            invertTree(root->right);
        return root;       
    }
};
