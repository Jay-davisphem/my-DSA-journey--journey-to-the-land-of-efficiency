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
#include <iostream>

void selectionSort(int arr[], int n)
{
  int i, j;
  for (i = 0; i < n - 1; i++)
  {
    int jMin = i;
    for (j = i + 1; j < n; j++)
    {
      if (arr[j] < arr[jMin])
        jMin = j;
    }
    if (jMin != i)
      std::swap(arr[i], arr[jMin]);
  }
}

void printArray(int arr[], int n)
{
  for (int i = 0; i < n; i++)
    std::cout << arr[i] << ' ';

  printf("\n");
}

int main()
{
  int arr[] = {23, 45, 1, 3, 2, 5, 4, 6, 7, 8};

  int n{10};

  selectionSort(arr, n);

  printArray(arr, n);
}