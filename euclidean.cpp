// calculates euclidean norm of a vector of length N
#include <cmath>

// recursive helper function finds sum of squares of values (sumOfSquares) and returns
// that sum's squareroot (euclidean norm)
extern "C" double euclidean_helper(int length, double* values, double sumOfSquares)
{
  if (length == 0)
  	return sqrt(sumOfSquares);
  else
  {
    sumOfSquares += (*values) * (*values);
    return euclidean_helper(--length, ++values, sumOfSquares);
  }
}

// main function returns euclidean norm of a vector of length N
extern "C" double euclidean(const int N, double* values)
{
  return euclidean_helper(N, values, 0.0);
}