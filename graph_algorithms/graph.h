#ifndef GRAPH
#define GRAPH

class Graph {
    private:
        bool **A;
        int N;
    public:
        Graph(int numberOfNodes) {

            N = numberOfNodes;
            // Allocating memory for adj matrix.
            A = new bool*[N];
            for (int i = 0 ; i < N ; i++) {
                A[i] = new bool[N];
            }

            // Initializing
            for (int i = 0 ; i < N ; i++) {
                for (int j = 0 ; j < N ; j++) {
                    A[i][j] = false;
                }
            }
        }
        Graph(bool **adj_matrix, int N) {
            A = adj_matrix;
            N = N;
        }
        ~Graph() {
            for (int i = 0 ; i < N ; i++)
                delete A[i];
            delete A;
        }
        void add_link(int a, int b, bool both);
        void bfs(int start_node, bool verbose);
        void dfs(int start_node);
        std::vector<int> neighbors(int node);
        void printGraph();
        void printNeighbors(int node);
};

#endif