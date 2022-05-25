/* g++ --c++2a */
#include <algorithm>
#include <iostream>
#include <iterator>
#include "sorting.h"
#include "../utils.h"
#include <chrono>

int main(){
  int array[]{9,8,6,4,7,445,565,234,4576,34435,5654,4354,77,3443,436,767,34534,74,3445,76,4344,5635,7476,454,55,566,565,34,4353,223,56656767,8858,545,888,55,88,343,622,22222,666,44,666,44,66,446,33,66,33};
  int len = static_cast<int>(std::size(array));

  printArray(array, len);
  timeIt(selectSort, array, len, false);
  printArray(array, len);

  int array1[]{9,8,6,4,7,445,565,234,4576,34435,5654,4354,77,3443,436,767,34534,74,3445,76,4344,5635,7476      ,454,55,566,565,34,4353,223,56656767,8858,545,888,55,88,343,622,22222,666,44,666,44,66,446,33,66,33};
  timeIt(bubbleSort_naive, array1, len, false);
  printArray(array1, len);

  int array2[]{9,8,6,4,7,445,565,234,4576,34435,5654,4354,77,3443,436,767,34534,74,3445,76,4344,5635,7476      ,454,55,566,565,34,4353,223,56656767,8858,545,888,55,88,343,622,22222,666,44,666,44,66,446,33,66,33};
  timeIt(bubbleSort, array2, len, false);
  printArray(array2, len);

  int array3[]{9,8,6,4,7,445,565,234,4576,34435,5654,4354,77,3443,436,767,34534,74,3445,76,4344,5635,7476      ,454,55,566,565,34,4353,223,56656767,8858,545,888,55,88,343,622,22222,666,44,666,44,66,446,33,66,33};
  auto start = std::chrono::high_resolution_clock::now();

  std::sort(std::begin(array3), std::end(array3));

  auto end = std::chrono::high_resolution_clock::now();

  auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
  std::cout << "Spent " << duration.count() << "ms to produce ";
  printArray(array3, len);

}
