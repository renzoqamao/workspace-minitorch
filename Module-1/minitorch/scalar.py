from .autodiff import FunctionBase, Variable, History
from . import operators
import numpy as np
import math

## Task 1.1
## Derivatives


def central_difference(f, *vals, arg=0, epsilon=1e-6):
    r"""
    Computes an approximation to the derivative of `f` with respect to one arg.

    See :doc:`derivative` or https://en.wikipedia.org/wiki/Finite_difference for more details.

    Args:
       f : arbitrary function from n-scalar args to one value
       *vals (floats): n-float values :math:`x_0 \ldots x_{n-1}`
       arg (int): the number :math:`i` of the arg to compute the derivative
       epsilon (float): a small constant

    Returns:
       float : An approximation of :math:`f'_i(x_0, \ldots, x_{n-1})`
    """
    # TODO: Implement for Task 1.1.
    # raise NotImplementedError('Need to implement for Task 1.1')
    temp_array = []
    for i in vals:
        temp_array.append(i)
    add_e_list = temp_array.copy()
    add_e_list[arg] = add_e_list[arg] + epsilon
    sub_e_list = temp_array
    sub_e_list[arg] = sub_e_list[arg] - epsilon
    f_add_e = f(*add_e_list)
    f_sub_e = f(*sub_e_list)
    return ((f_add_e - f_sub_e) / (2 * epsilon))

## Task 1.2 and 1.4
## Scalar Forward and Backward


class Scalar(Variable):
    """
    A reimplementation of scalar values for autodifferentiation
    tracking.  Scalar Variables behave as close as possible to standard
    Python numbers while also tracking the operations that led to the
    number's creation. They can only be manipulated by
    :class:`ScalarFunction`.

    Attributes:
        data (float): The wrapped scalar value.

    """

    def __init__(self, v, back=History(), name=None):
        super().__init__(back, name=name)
        self.data = float(v)

    def __repr__(self):
        return "Scalar(%f)" % self.data

    def __mul__(self, b):
        return Mul.apply(self, b)

    def __truediv__(self, b):
        return Mul.apply(self, Inv.apply(b))

    def __add__(self, b):
        return Add.apply(self, b)
        # TODO: Implement for Task 1.2.
        # raise NotImplementedError('Need to implement for Task 1.2')

    def __lt__(self, b):
        return LT.apply(self, b)
        # TODO: Implement for Task 1.2.
        # raise NotImplementedError('Need to implement for Task 1.2')

    def __gt__(self, b):
        return 1 - LT.apply(self, b)
        # TODO: Implement for Task 1.2.
        # raise NotImplementedError('Need to implement for Task 1.2')

    def __sub__(self, b):
        return Add.apply(self, -b)
        # TODO: Implement for Task 1.2.
        # raise NotImplementedError('Need to implement for Task 1.2')

    def __neg__(self):
        return Neg.apply(self)
        # TODO: Implement for Task 1.2.
        # raise NotImplementedError('Need to implement for Task 1.2')

    def log(self):
        return Log.apply(self)
        # TODO: Implement for Task 1.2.
        # raise NotImplementedError('Need to implement for Task 1.2')

    def exp(self):
        return Exp.apply(self)
        # TODO: Implement for Task 1.2.
        # raise NotImplementedError('Need to implement for Task 1.2')

    def sigmoid(self):
        return Sigmoid.apply(self)
        # TODO: Implement for Task 1.2.
        # raise NotImplementedError('Need to implement for Task 1.2')

    def relu(self):
        return ReLU.apply(self)
        # TODO: Implement for Task 1.2.
        # raise NotImplementedError('Need to implement for Task 1.2')

    def get_data(self):
        return self.data


class ScalarFunction(FunctionBase):
    "A function that processes and produces Scalar variables."

    @staticmethod
    def forward(ctx, *inputs):
        """Args:

           ctx (:class:`Context`): A special container object to save
                                   any information that may be needed for the call to backward.
           *inputs (list of numbers): Numerical arguments.

        Returns:
            number : The computation of the function :math:`f`

        """
        pass

    @staticmethod
    def backward(ctx, d_out):
        """
        Args:
            ctx (Context): A special container object holding any information saved during in the corresponding `forward` call.
            d_out (number):
        Returns:
            numbers : The computation of the derivative function :math:`f'_{x_i}` for each input :math:`x_i` times `d_out`.
        """
        pass

    # checks.
    variable = Scalar
    data_type = float

    @staticmethod
    def data(a):
        return a


# Examples
class Add(ScalarFunction):
    "Addition function"

    @staticmethod
    def forward(ctx, a, b):
        return a + b

    @staticmethod
    def backward(ctx, d_output):
        return d_output, d_output


class Log(ScalarFunction):
    "Log function"

    @staticmethod
    def forward(ctx, a):
        ctx.save_for_backward(a)
        return operators.log(a)

    @staticmethod
    def backward(ctx, d_output):
        a = ctx.saved_values
        return operators.log_back(a, d_output)


class LT(ScalarFunction):
    "Less-than function"

    @staticmethod
    def forward(ctx, a, b):
        return 1.0 if a < b else 0.0

    @staticmethod
    def backward(ctx, d_output):
        return 0.0


# To implement.


class Mul(ScalarFunction):
    "Multiplication function"

    @staticmethod
    def forward(ctx, a, b):
        ctx.save_for_backward(a, b)
        return a * b
        # TODO: Implement for Task 1.2.
        # raise NotImplementedError('Need to implement for Task 1.2')

    @staticmethod
    def backward(ctx, d_output):
        var1, var2 = ctx.saved_values
        return var2 * d_output, var1 * d_output
        # TODO: Implement for Task 1.4.
        # raise NotImplementedError('Need to implement for Task 1.4')


class Inv(ScalarFunction):
    "Inverse function"

    @staticmethod
    def forward(ctx, a):
        ctx.save_for_backward(a)
        return 1.0 / a
        # TODO: Implement for Task 1.2.
        # raise NotImplementedError('Need to implement for Task 1.2')

    @staticmethod
    def backward(ctx, d_output):
        var = ctx.saved_values
        return (-1.0 / math.pow(var , 2)) * d_output
        # TODO: Implement for Task 1.4.
        # raise NotImplementedError('Need to implement for Task 1.4')


class Neg(ScalarFunction):
    "Negation function"

    @staticmethod
    def forward(ctx, a):
        return operators.neg(a)
        # TODO: Implement for Task 1.2.
        # raise NotImplementedError('Need to implement for Task 1.2')

    @staticmethod
    def backward(ctx, d_output):
        return - d_output
        # TODO: Implement for Task 1.4.
        # raise NotImplementedError('Need to implement for Task 1.4')


class Sigmoid(ScalarFunction):
    "Sigmoid function"

    @staticmethod
    def forward(ctx, a):
        ctx.save_for_backward(operators.sigmoid(a))
        return operators.sigmoid(a)
        # TODO: Implement for Task 1.2.
        # raise NotImplementedError('Need to implement for Task 1.2')

    @staticmethod
    def backward(ctx, d_output):
        var = ctx.saved_values
        return var * (1 - var) * d_output
        # TODO: Implement for Task 1.4.
        # raise NotImplementedError('Need to implement for Task 1.4')


class ReLU(ScalarFunction):
    "ReLU function"

    @staticmethod
    def forward(ctx, a):
        ctx.save_for_backward(a)
        return operators.relu(a)
        # TODO: Implement for Task 1.2.
        # raise NotImplementedError('Need to implement for Task 1.2')

    @staticmethod
    def backward(ctx, d_output):
        var = ctx.saved_values
        return operators.relu_back(var , d_output)
        # TODO: Implement for Task 1.4.
        # raise NotImplementedError('Need to implement for Task 1.4')


class Exp(ScalarFunction):
    "Exp function"

    @staticmethod
    def forward(ctx, a):
        ctx.save_for_backward(a)
        return operators.exp(a)
        # TODO: Implement for Task 1.2.
        # raise NotImplementedError('Need to implement for Task 1.2')

    @staticmethod
    def backward(ctx, d_output):
        var = ctx.saved_values
        return var * d_output
        # TODO: Implement for Task 1.4.
        # raise NotImplementedError('Need to implement for Task 1.4')


def derivative_check(f, *scalars):

    for x in scalars:
        x.requires_grad_(True)
    out = f(*scalars)
    out.backward()

    vals = [v for v in scalars]

    for i, x in enumerate(scalars):
        check = central_difference(f, *vals, arg=i)
        print(x.derivative, check)
        np.testing.assert_allclose(x.derivative, check.data, 1e-2, 1e-2)
