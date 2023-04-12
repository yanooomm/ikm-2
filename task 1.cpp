/*Написать программу, которая получает на вход N целых чисел и стоит по ним
дерево поиска, причем оно не должно содержать повторяющихся значений
(дубликаты игнорировать). Вывести полученное дерево на экран «боком».
Вывести на экран все листья дерева в убывающем порядке.*/

#include <iostream>

using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;
};

Node* createNode(int data) { // создаем узел
    Node* node = new Node;
    node->data = data;
    node->left = nullptr;
    node->right = nullptr;
    return node;
}

void insertNode(Node*& root, int data) { // добавляем узел
    if (root == nullptr) {
        root = createNode(data);
        return;
    }
    if (data < root->data) {
        insertNode(root->left, data);
    }
    else
        if (data > root->data) {
            insertNode(root->right, data);
        }
}

void printTree(Node* root, int a = 0) { // вывод дерева на экран боком
    if (root == nullptr) {
        return;
    }
    printTree(root->right, a + 1); 
    for (int i = 0; i < a; i++) {
        cout << " ";
    }
    cout << root->data << endl;
    printTree(root->left, a + 1);
}

void printLeaves(Node* root) {// вывод листьев в убывающем порядке
    if (root == nullptr) {
        return;
    }
    if (root->left == nullptr && root->right == nullptr) {
        cout << root->data << " ";
    }
    printLeaves(root->right);
    printLeaves(root->left);
}

int main()
{
    setlocale(LC_ALL, "rus");
    int n;
    cin >> n;
    Node* root = nullptr;
    for (int i = 0; i < n; i++) {
        int data;
        cin >> data;
        insertNode(root, data);
    }
    cout << "Полученное дерево: " << endl;
    printTree(root);
    cout << "Листья в убывающем порядке: ";
    printLeaves(root);
}

