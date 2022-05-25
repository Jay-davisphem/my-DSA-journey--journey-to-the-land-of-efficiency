#include <iostream>
#include <utility>
#include <iterator>
#include "sort.h"

template <typename T>
void selectSortR(T arr[]){

  int indOfMax{arr[0]};
  int len{static_cast<int>(std::size(arr))};
  for(int presInd{0}; presInd < len - 1; ++presInd){
    std::cout << arr[presInd] << " ";
  }
}

int main(){
  std::cout << "\n";
  int arr[4]{45,123,67,48};
  selectSortR<int>(arr);
}
