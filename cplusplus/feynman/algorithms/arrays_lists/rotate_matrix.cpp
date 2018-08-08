#include <iostream>
#include <vector>
#include <tuple>

using namespace std;

/*

The idea is to do a 4-way swap.

For instance,
int matrix[4][4] = {
  {1,2,3,4},
  {5,6,7,8},
  {9,10,11,12},
  {13,14,15,16}
};

1: Swap 1,13,16,4
{4,2,3,16},
{5,6,7,8},
{9,10,11,12},
{1,14,15,13}

2: Swap 5,14,12,3

*/
void swap(vector<tuple<int,int>> coords, int **matrix) {
  tuple<int,int> t0 = coords.at(0);
  tuple<int,int> t1 = coords.at(1);
  tuple<int,int> t2 = coords.at(2);
  tuple<int,int> t3 = coords.at(3);

  int temp = matrix[get<0>(t0)][get<1>(t0)];
  matrix[get<0>(t0)][get<1>(t0)] = matrix[get<0>(t3)][get<1>(t3)];
  matrix[get<0>(t3)][get<1>(t3)] = matrix[get<0>(t2)][get<1>(t2)];
  matrix[get<0>(t2)][get<1>(t2)] = matrix[get<0>(t1)][get<1>(t1)];
  matrix[get<0>(t1)][get<1>(t1)] = temp;
}

void print(tuple<int,int> t) {
  cout << "(" << get<0>(t) << "," << get<1>(t) << ")" << endl;
}

void print(int **matrix, int dim) {
  for(int i = 0; i < dim; i++) {
    for(int j = 0; j < dim; j++) {
      cout << matrix[i][j] << " ";
    }
    cout << endl;
  }
}

void rotate(int **matrix, int dim) {
  tuple<int,int> t0(0,0);
  tuple<int,int> t1(dim-1,0);
  tuple<int,int> t2(dim-1,dim-1);
  tuple<int,int> t3(0,dim-1);
  int curr_dim = dim;
  for(int i = 0; i < dim/2; i++) {
    for(int j = 0; j < curr_dim-1; j++) {
      t0 = tuple<int,int>(j+i,i);
      t1 = tuple<int,int>(3-i,j+i);
      t2 = tuple<int,int>(3-j-i,3-i);
      t3 = tuple<int,int>(i,3-j-i);
      swap(vector<tuple<int,int>>{t0,t1,t2,t3}, matrix);
    }
    curr_dim = curr_dim/2;
  }
}

int** get_test_matrix(int dim) {
  int **matrix = new int*[dim];
  for(int i = 0; i < dim; i++) {
    matrix[i] = new int[dim];
  }
  int k = 1;
  for(int i = 0; i < dim; i++) {
    for(int j = 0; j < dim; j++)
      matrix[i][j] = k++;
  }
  return matrix;
}

int main() {
  int **matrix = get_test_matrix(4);
  print(matrix, 4);
  rotate(matrix, 4);
  print(matrix, 4);
}
