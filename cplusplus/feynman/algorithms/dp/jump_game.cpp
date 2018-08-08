/*
int A[] = {2,3,1,1,4};
int n = 5;
int i = 0;
int reach = 4;

*/
bool canJump(int A[], int n) {
  int i = 0;
  for (int reach = 0; i < n && i <= reach; i++)
    reach = max(i + A[i], reach);
  return i == n;
}
