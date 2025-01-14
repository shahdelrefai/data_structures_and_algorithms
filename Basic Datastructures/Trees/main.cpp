#include <iostream>
#include "TreeNode.h"
using namespace std;


int main() {
    TreeNode* root = nullptr;
    root = insertNode(root, 6);
    root = insertNode(root, 8);
    root = insertNode(root, 2);
    root = insertNode(root, 1);
    root = insertNode(root, 4);
    root = insertNode(root, 7);
    root = insertNode(root, 10);

    displayTreeInOrder(root);
    std::cout << std::endl;
    root = deleteNode(root, 2);
    displayTreeInOrder(root);
    std::cout << "\nLeaf Count: " << countLeafNodes(root);
    return 0;
}
