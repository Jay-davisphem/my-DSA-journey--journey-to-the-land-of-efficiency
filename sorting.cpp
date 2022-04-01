/*
 * =====================================================================================
 *
 *       Filename:  sorting.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  26/03/2022 22:37:44
 *       Revision:  none
 *       Compiler:  g++
 *
 *         Author:  David Oluwafemi Joshua, davidoluwafemi178@gmail.com
 *   Organization:  Ourgooals
 *
 * =====================================================================================
 */
void swap(int *a, int *b){
  int *temp = a;
  a = b;
  b = temp;
}
void selectionSort(int arr[], int n){
  int i, j;
  for(i = 0; i < n - 1; i++){
    int jMin = i;
    for (j = i+1; j < n; j++){
      if(arr[j] < a[jMin])
        jMin = j;
    }
    if (jMin != i)
      swap(a[i], a[jMin])
  }
}
