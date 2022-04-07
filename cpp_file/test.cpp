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
#include <iomanip>
int main()
{
  std::cout << std::boolalpha;

  float zero{0.0};
  double five{5.0};
  std::cout << five / zero << '\n';
  std::cout << -five / zero << '\n';
  std::cout << zero / zero << '\n';

  int arr[] = {23, 45, 1, 3, 2, 5, 4, 6, 7, 8, 45, 2, 2, 1, 4, 6, 4, 7};
  int n{18};

  insertionSort(arr, n);

  printArray(arr, n);
}