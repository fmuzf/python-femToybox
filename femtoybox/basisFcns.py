import numpy as _np

def dirchElement(grid, index):
  """Return a function phi which is the ith basis elements of
  for the Dirichlet problem.
  """

  nn = len(grid)-1
  ell = _np.diff(grid)
  if index != nn:
    rightDomain = lambda x: (x <= grid[index + 1]) * (grid[index] <= x)
    rightSlope = -1. / (grid[index + 1] - grid[index])
    rightIntercept =  grid[index +1]
  if index != 0:
    leftDomain = lambda x: (grid[index - 1] <= x) * (x <= grid[index])
    leftSlope = 1. / (grid[index] - grid[index - 1])
    leftIntercept =  grid[index - 1]

  if index == 0:
    def phi(x):
      y = rightDomain(x) * rightSlope * (x - rightIntercept)
      return y
  elif index == nn:
    def phi(x):
      y = leftDomain(x) * leftSlope * (x - leftIntercept)
      return y
  else:
    def phi(x):
      y = (rightDomain(x) * rightSlope * (x - rightIntercept)
          +  leftDomain(x) * leftSlope * (x - leftIntercept))
      return y
  
  return phi
