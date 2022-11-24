from sympy.matrices import Matrix


def metric_from_jacobian(J: Matrix) -> Matrix:
    def f(i,j):
        return J[:,i].dot(J[:,j])
    return Matrix(3,3, f)