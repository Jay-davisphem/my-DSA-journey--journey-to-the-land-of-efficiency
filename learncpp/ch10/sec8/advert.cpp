#include <iostream>
#include "advert.h"

void printAdvert(Advert <double>&advert){
  std::cout << "\nTotal number of ads is " << advert.numOfAds << '\n';
  std::cout << advert.percClicked << "% of the advert were clicked!\n";
  std::cout << "An advert click worths $" << advert.amountPerClick << '\n';
}

template <typename T>
T calculateTotalAdvertEarning(Advert <double>&advert){
  return advert.numOfAds * (advert.percClicked/100.0) * advert.amountPerClick;
}
int main(){
  Advert <double>advert{};

  std::cin >> advert.numOfAds;
  std::cin >> advert.percClicked;
  std::cin >> advert.amountPerClick;

  printAdvert(advert);

  std::cout << "\nYou earned $" << calculateTotalAdvertEarning<double>(advert) << "!\n";
}
