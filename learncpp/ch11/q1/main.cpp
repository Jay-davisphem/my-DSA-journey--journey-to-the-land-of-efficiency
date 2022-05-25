#include <iostream>

namespace Animal{
  enum Animal{
    chicken,
    dog,
    cat,
    elephant,
    duck,
    snake,

    noOfAnimals
  };
}

void printNoOfLegs(int animalsLegs[Animal::noOfAnimals], Animal::Animal animal){
  std::cout << animalsLegs[animal] << " legs\n";
}
int main(){
  constexpr int daysInAYear{365};
  double highTemperature[daysInAYear]{};


  int animalsLegs[Animal::noOfAnimals]{2, 4, 4, 4, 2, 0};

  printNoOfLegs(animalsLegs, Animal::snake);
}
