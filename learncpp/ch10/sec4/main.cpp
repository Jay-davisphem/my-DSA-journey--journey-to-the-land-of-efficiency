#include <iostream>
#include <string>
#include "animal.h"

std::string getAnimalName(Animal &animal){
  switch(animal){
    case pig:
      return "pig";
    case chicken:
      return "chicken";
    case goat:
      return "goat";
    case cat:
      return "cat";
    case dog:
      return "dog";
    case duck:
      return "duck";
    default:
        return "???";
  }
}

void printNumberOfLegs(Animal &animal){
  switch(animal){
    case pig:
    case goat:
    case dog:
    case cat:
      std::cout << 4;
      break;
    case chicken:
    case duck:
      std::cout << 2;
      break;
    default:
        std::cout << "???";
  }
}

int main(){
  Animal cat1{cat};
  Animal chicken1{chicken};
  Animal pig1{pig};
  Animal animals[3] = {pig1, cat1, chicken1};
  for(int i=0; i < 3; ++i){
    std::cout << "A " << getAnimalName(animals[i]) << " has ";
    printNumberOfLegs(animals[i]);
    std::cout << " legs.\n";
  }
}
