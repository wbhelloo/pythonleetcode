#include <math.h>
int gcd(int x, int y);
int in_mandel(double x0, double y0, int n);
int divide(int a, int b, int *remainder);
/* A C data structure */
typedef struct Point {
    double x,y;
} Point;
double distance(Point *p1, Point *p2);
