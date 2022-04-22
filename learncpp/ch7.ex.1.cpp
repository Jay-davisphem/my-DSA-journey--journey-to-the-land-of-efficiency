/*
 * =====================================================================================
 *
 *       Filename:  ch7.ex.1.cpp
 *
 *    Description:  Random Number generator using random device and uniform distribution function
 *
 *        Version:  1.0
 *        Created:  20/04/2022 08:36:01
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  David Oluwafemi Joshua (), davidoluwafemi178@gmail.com
 *   Organization:
 *
 * =====================================================================================
 */

#include <iostream>
#include <random> // contains std::random_device, std::uniform_int_distribution, and std:mt19937(mt -> messene twister PRNG algorithm)

namespace randOkO {
  std::mt19937 mt{ std::random_device{}() };

  int get(int min, int max){
    std::uniform_int_distribution die{ min, max };
    return die(mt);
  }
}

int main(){
  std::cout << randOkO::get(1, 6) << '\n';
  std::cout << randOkO::get(1, 20) << '\n';
  std::cout << randOkO::get(1, 100) << '\n';
}
