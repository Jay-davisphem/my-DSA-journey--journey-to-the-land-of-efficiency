#include <iostream>
#include <chrono>
#include <iomanip> // for std::setprecision()
#include "utils.h"


void timeIt(function f, int* arr, int len, bool rev = false){
  std::cout << std::setprecision(10);

  auto start = std::chrono::high_resolution_clock::now();
  f(arr, len, rev);
  auto end = std::chrono::high_resolution_clock::now();

  auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);

  std::cout << "Spent " << duration.count() << "ms to produce ";
}
