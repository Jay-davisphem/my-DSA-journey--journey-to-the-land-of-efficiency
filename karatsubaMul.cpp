#include <cmath>
#include <iostream>
int karatsubaMultiply(int x,  int y, int n){
  /*
   * let a, b, c, d --> upper, lower halves of x, y respectively                                     
   * n is the length of x and y(assume they have equal lengths)
   * xy = (10^n)ac + (10^(n/2))((a + b)(c + d) - ac - bd) + bd 
   */
  if(n == 1)
    return x * y;
  else{
    int a, b, c, d, ac, bd, p, q, pq;
    a = x / pow(10, n/2);
    b = x % int(pow(10, n/2));
    c = y / pow(10, n/2);
    d = y % int(pow(10, n/2));
    p = a + b;
    q = c + d;

    ac = karatsubaMultiply(a, c, n/2);
    bd = karatsubaMultiply(b, d, n/2);
    pq = karatsubaMultiply(p, q, n/2);

    return pow(10, n) * ac + pow(10, n/2)*(pq - ac - bd) + bd;
  }
}

int main(){
  int x, y, n;
  std::cin >> x >> y >> n;
  int prod = karatsubaMultiply(x, y, n);
  std::cout << prod << '\n';
}
