#include <iostream>
#include <vector>
#include <queue>
#include "graph.h"

using namespace std;

void Graph::add_link(int a, int b, bool both=false) {
    A[a][b] = true;
    if (both)
        A[b][a] = true;
}

vector<int> Graph::neighbors(int node) {
    vector<int> node_neighbors;
    for (int i = 0 ; i < N ; i++) {
        if (A[node][i] == true)
            node_neighbors.push_back(i);
    }
    return node_neighbors;
}

void Graph::printGraph() {
    for (int i = 0 ; i < N ; i++) {
        cout << i << ": ";
        printNeighbors(i);
        cout << "\n";
    }
}

void Graph::printNeighbors(int node) {
    for (int i = 0 ; i < N ; i++) {
        if (A[node][i] == true)
            cout << i << " ";
    }
}

void Graph::bfs(int node, bool verbose=false) {
    bool *visited = new bool[N];
    queue<int> q;

    if (verbose)
        cout << node << "\n";
    q.push(node);
    visited[node] = true;

    while(!q.empty()) {
        int next_node = q.front();
        vector<int> node_neighbors = neighbors(next_node);
        
        q.pop();
        for (int i = 0 ; i < node_neighbors.size() ; i++) {
            if (!visited[ node_neighbors[i] ] ) {
                q.push(node_neighbors[i]);
                visited[ node_neighbors[i] ] = true;

                if (verbose)
                    cout << next_node << "\n";
            }
        }
    }

    delete visited;
}

int main() { 
    Graph *G = new Graph(6);
    G->add_link(0, 4);
    G->add_link(0, 2);
    G->add_link(1, 5);
    G->add_link(2, 1);    
    G->add_link(2, 3);    
    G->add_link(2, 5);    
    G->add_link(3, 5);    
    G->add_link(4, 5);    
    G->printGraph();
    G->bfs(0, false);
    delete G;
    return 0;
}