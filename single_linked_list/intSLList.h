#ifndef SL_LIST_H
#define SL_LIST_H

class IntNode {
    public:
        int data;
        IntNode *next;
        IntNode() {
            next = NULL;
        }
        IntNode(int i, IntNode *in = NULL) {
            data = i, next = in;
        }
};

class IntSLList {
    public:
        IntNode *head, *tail;
        IntSLList() {
            head = tail = NULL;
        }
        ~IntSLList();
        int isEmpty() {
            return head == NULL;
        }
        void addToHead(int);
        void addToTail(int);
        int deleteFromHead();
        int deleteFromTail();
        void reverseIterative();
        void reverseRecursive(IntNode*);
        void deleteNode(int);
        bool contains(int) const;
        void printElementsIterative();
        void printElementsRecursive(IntNode*);
};

#endif