#include <iostream>
#include <random>
#include <limits>

namespace hiLo {
  std::random_device rand;
  std::seed_seq seeds{ rand(), rand(), rand(), rand(),
                       rand(), rand(), rand(), rand() };
  std::mt19937 mt{ seeds };

  int get(int min, int max){
    std::uniform_int_distribution<> die100{ min, max };

    return die100(mt);
  }
}

void ignoreLine(){
  std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
}

void printResult(int rand, int ans){
  if(rand < ans)
    std::cout << "Your guess is too high.\n";
  else if(rand == ans)
    std::cout << "Correct! You win!\n";
  else
    std::cout << "Your guess is too low.\n";
}

int getInput(int count){
  int x{};
  while (1){
    std::cout << "Guess #" << count << ": ";
    std::cin >> x;
    if(std::cin.fail()){
      std::cin.clear();
      ignoreLine();
    }
    else{
      ignoreLine();
      return x;
    }
  }
}

char getCharInput(){
  std::cout << "Would you like to play again (y/n)? ";
  char x{};
  std::cin >> x;
  ignoreLine();
  return x;
}

char playAgain(){
  char continueChoice{};
  while(1){
    continueChoice = getCharInput();
    if(continueChoice == 'y' || continueChoice == 'n')
      break;
  }
  return continueChoice;
}

void startMsg(int guessNumber){
  std::cout << "Let's play a game. I'm thinking of a number. You have " << guessNumber << " tries to guess what it is.\n";
}

void playGame(int guessNumber){
  startMsg(guessNumber);
  char continueChoice{};
  do{
    int rand{hiLo::get(1, 100)};
    int count{1};
    while(count <= guessNumber){
      int ans { getInput(count) };
      printResult(rand, ans);

      if(rand == ans)
        break;
      if(rand != ans && count == guessNumber)
        std::cout << "Sorry, you lose. The correct number was " << rand << ".\n";
      ++count;
    }
    continueChoice = playAgain();
    if (continueChoice == 'n')
      break;
    startMsg(guessNumber);
  }while(continueChoice == 'y');
  std::cout << "Thank you for playing.\n";
}

int main(){
  playGame(7);
}
