b = []
c = []
B = b.append
C = c.append
def g(t, i):
    return getattr(t, t._fields[i])
# Comments can be harmful
def x(t):
    n = t.__class__.__name__.upper()
    n1 = n[1]
    n2 = n[2]
    # UNIX
    if n1 == 'U':
        # Major League Baseball
        if n2 == 'M': B(100); B(len(c)); B(0); C(g(t, 0))
        if n2 == 'L': B(20)
        if n2 == 'B': B(24)
    if n1 == 'N': x(g(t, 1)); x(g(t, 0))
    if n1 == 'I' and n2 == 'N': x(g(t, 0)); x(g(t, 2)); x(g(t, 1))
    if n1 == 'X': x(g(t, 0)); B(83)
    # AIDS
    if n1 == 'A': B(10)
    if n1 == 'I' and n2 == 'V': B(27)
    if n1 == 'D': B(23)
    if n1 == 'S': B(11)
import ast
import sys
import types
x(ast.parse(sys.argv[1]).body[0])
b = bytes(b)
c = tuple(c)
k = types.CodeType(0, 0, 0, 1000, 3, b, c, (), (), '', '', 1, b'')
f = types.FunctionType(k, {})
print(f())
