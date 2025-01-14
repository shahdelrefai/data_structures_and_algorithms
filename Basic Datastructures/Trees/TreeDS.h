//
// Created by Shahd El-Refai on 02/01/2024.
//

#ifndef DATASTRUCTURECRASHCOURSE_TREEDS_H
#define DATASTRUCTURECRASHCOURSE_TREEDS_H

#include <iostream>
#include <cmath>
#include <queue>
using namespace std;

class TreeNode {
public:
    int data{};
    TreeNode* leftChild;
    TreeNode* rightChild;

    public: TreeNode(int x)
            : leftChild(nullptr), rightChild(nullptr) {
        data = x;
    }
};

TreeNode* insertNode(TreeNode* root, int x) {
    if(root == nullptr) {
        return new TreeNode(x);
    }

    if(x < root->data) {
        root->leftChild = insertNode(root->leftChild, x);
    }
    else {
        root->rightChild = insertNode(root->rightChild, x);
    }

    return root;
}

TreeNode* findMinmumValueFromRightSubtree(TreeNode* root) {
    if(root->leftChild == nullptr) {

        return root;
    }
    return findMinmumValueFromRightSubtree(root->leftChild);
}

TreeNode* deleteNode(TreeNode* root, int x) {
    if (root == nullptr) {
        return root;
    }

    if (x < root->data) {
        root->leftChild = deleteNode(root->leftChild, x);
    } else if (x > root->data) {
        root->rightChild = deleteNode(root->rightChild, x);
    } else {
        if(root->rightChild == nullptr) {
            TreeNode *temp = root->leftChild;
            delete root;
            return temp;
        }
        else if(root->leftChild == nullptr) {
            TreeNode *temp = root->rightChild;
            delete root;
            return temp;
        }

        TreeNode* temp = findMinmumValueFromRightSubtree(root->rightChild);
        root->data = temp->data;
        root->rightChild = deleteNode(root->rightChild, temp->data);
    }

    return root;
}

int getTreeHeight(TreeNode* root) {
    if (!root) return 0;
    return 1 + max(getTreeHeight(root->leftChild), getTreeHeight(root->rightChild));
}

void displayTreeInOrder(TreeNode* root) {
    if (!root) {
        cout << "Tree is empty.\n";
        return;
    }

    queue<TreeNode*> q;
    q.push(root);
    int depth = 0;

    int height = getTreeHeight(root);
    int maxNodesAtLevel = pow(2, height - 1);

    while (true) {
        int levelSize = q.size();
        int spacing = maxNodesAtLevel / pow(2, depth);

        // leading spaces
        for (int i = 0; i < spacing; i++) cout << "  ";

        for (int i = 0; i < levelSize; i++) {
            TreeNode* current = q.front();
            q.pop();

            if (current) {
                cout << current->data;
                q.push(current->leftChild);
                q.push(current->rightChild);
            } else {
                cout << " ";
                q.push(nullptr);
                q.push(nullptr);
            }

            // spacing between nodes
            for (int j = 0; j < spacing * 2; j++) cout << "  ";
        }
        cout << endl;
        depth++;

        // Stop when all nodes at the next level are null
        bool allNull = true;
        queue<TreeNode*> temp = q;
        while (!temp.empty()) {
            if (temp.front()) {
                allNull = false;
                break;
            }
            temp.pop();
        }
        if (allNull) break;
    }
}

int countLeafNodes(TreeNode* root) {
    if(root == nullptr) return 0;
    if(root->leftChild == nullptr && root->rightChild == nullptr) return 1;
    return countLeafNodes(root->leftChild) + countLeafNodes(root->rightChild);
}

int countNodes(TreeNode* root) {
    if(root == nullptr) return 0;
    return 1 + countNodes(root->leftChild) + countNodes(root->rightChild);
}



#endif //DATASTRUCTURECRASHCOURSE_TREEDS_H
