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
#include "sorting.h"
#include "utilities.h"

int main()
{
  int arr[] = {23, 45, 1, 3, 2, 5, 4, 6, 7, 8};

  int n{10};

  bubbleSort(arr, n);

  printArray(arr, n);
}