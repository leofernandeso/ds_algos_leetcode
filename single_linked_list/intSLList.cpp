#include <iostream>
#include "intSLList.h"

void IntSLList::addToHead(int data) {
    IntNode *new_node = new IntNode(data);
    new_node->next = head;
    head = new_node;

    if (tail == NULL) {
        tail = new_node;
    }
}

void IntSLList::addToTail(int data) {
    IntNode *new_node = new IntNode(data);
    if (tail != NULL) {
        tail->next = new_node;
        tail = new_node;
    }
    else {
        head = tail = new_node;
    }
}

void IntSLList::printElements() {
    IntNode *p_it = head;
    while (p_it != NULL) {
        std::cout << p_it->data << "\n";
        p_it = p_it->next;
    }
}

int IntSLList::deleteFromHead() {
    IntNode *node = head;
    int data = node->data;

    if (head == tail)   // 1 or zero elements
        head = tail = NULL;
    else // more than one element
        head = head->next;

    delete node;
    return data;
}

int IntSLList::deleteFromTail() {
    IntNode *node = tail;
    int data = node->data;

    if (head == tail) {
        head = tail = NULL;
        delete head;
    }
    else {
        IntNode *aux = head;
        while (aux->next != tail)     // going through the n-1th element
            aux = aux->next;
        delete tail;
        tail = aux;
        tail->next = NULL;
    }
    return data;
}

void IntSLList::deleteNode(int data) {
    IntNode *p = head;
    
    if (head->data == data)
        deleteFromHead();
    else if (tail->data == data)
        deleteFromTail();
    else {
        while (p->next->data != data)
            p = p->next;
        IntNode *aux = p->next;
        p->next = p->next->next;
        delete aux;        
    }   
}

bool IntSLList::contains(int data) const {
    for (IntNode *p = head ; p != NULL ; p = p->next) {
        if (p->data == data) {
            return 1;
        }
    }
    return 0;
}

int main() {
    IntSLList *ll = new IntSLList();
    ll->addToHead(2);
    ll->addToHead(4);
    ll->addToTail(10);
    ll->addToTail(11);
    ll->addToHead(3);
    ll->printElements();
    std::cout << "\n";
    ll->deleteFromHead();
    std::cout << "\n";
    ll->printElements();
    std::cout << "\n";
    ll->deleteFromTail();
    ll->deleteNode(4);
    ll->printElements();
    std::cout << ll->contains(10) << " " << ll->contains(4);
}