#ifndef UTILS_H
#define UTILS_H

using function = void (int *, int, bool);


void timeIt(function f, int * arr, int len, bool rev);

#endif
