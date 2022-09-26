import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker




def PolyCoefficients(x, coeffs):
    """ Returns a polynomial for ``x`` values for the ``coeffs`` provided.
    The coefficients must be in ascending order (``x**0`` to ``x**order``).
    """
    print(f'# This is a polynomial of order {order}. ')
    y = 0
    for i in range(order-1,-1,-1):
        y += coeffs [(order-1)-i] * x ** i
    # for i in range(order):
    #     y += coeffs[i] * x ** i
    return y

def SimpleFunction(x):
    y = 0
    y = eval(expr)
    return y


x = np.linspace(-5, 5, 100)
simple_poly = int(input("""print:
- "1" - simple input
- "0" - part input 
"""))

if simple_poly:
    expr = input("Enter the function(in terms of x):")
    print(f"y={expr}")
    try:
        type(int(expr)) == int
        y = np.linspace(int(expr), int(expr), 100)
        plt.plot(x, y)
    except:
        plt.plot(x, SimpleFunction(x))
else:
    order = int(input("Input polynomial order:"))
    coeffs = [eval(input(f"term #{i + 1}: ")) for i in range(order)]
    plt.plot(x, PolyCoefficients(x, coeffs))

    poly_func = f"y={coeffs[-1]:{'+' if order > 1 else ''}} "
    for i in range(1, order):
        if coeffs[(order-1)]!=0:
            poly_func = poly_func[:2] + \
                        f"{coeffs[(order - 1) - i]:{'+' if (order-1) != i else ''}}x^{i}" \
                        + poly_func[2:]
    print(poly_func)


plt.grid()
plt.axvline(x=0,color='black')
plt.axhline(y=0,color='black')
plt.gca().xaxis.set_minor_locator(ticker.AutoMinorLocator(10))
plt.gca().yaxis.set_minor_locator(ticker.AutoMinorLocator(10))


lim_question = input("Graph limits: 'Yes' to input")
if lim_question == "Yes":
    limits = [int(float(num)) for num in input(
        "Input limits|  x: y, down: upper | in one string (e.g. -5 5 -10 -10)").split()]
    plt.xlim(limits[0], limits[1])
    plt.ylim(limits[2], limits[3])


plt.show()