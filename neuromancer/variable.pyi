from typing import Any, Callable, Sequence, overload
from types import Iterable, Union
import torch
from neuromancer.constraint import Constraint

_size = Union[torch.Size, Iterable[int]]
_name = Union[str, None]
_input = Union[Variable, float, int, torch.Tensor]

@overload
def variable(*, key: _name = None, is_input=False, display_name=None) -> Variable: ...
@overload
def variable(
    inputs: Iterable[_input], func: Callable, *, key: _name = None, display_name=None
) -> Variable: ...
@overload
def variable(*size: int, key: _name = None, display_name: _name = None) -> Variable: ...
@overload
def variable(size: _size, *, key: _name = None, display_name=None) -> Variable: ...
@overload
def variable(
    value: torch.Tensor, *, key: _name = None, display_name=None
) -> Variable: ...
@overload
def variable(
    inputs: Iterable[_input], func: Callable, *, key: _name = None, display_name=None
) -> Variable: ...

class Variable:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    @overload
    def __init__(self, name: str, value: torch.Tensor) -> None: ...
    @overload
    def __init__(self, name: str, value: int | float) -> None: ...
    @overload
    def __init__(self, name: str, func: Callable) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __add__(self, other) -> Variable: ...
    def __sub__(self, other) -> Variable: ...
    def __mul__(self, other) -> Variable: ...
    def __matmul__(self, other) -> Variable: ...
    def __div__(self, other) -> Variable: ...
    def __pow__(self, exponent) -> Variable: ...
    def __abs__(self) -> Variable: ...
    def __mod__(self, modulo) -> Variable: ...
    def __eq__(self, other) -> Constraint: ...
    @overload
    def unpack(names: Sequence[str]) -> Sequence[Variable]: ...
    def unpack(nargs: int) -> Sequence[Variable]: ...
    def parameters(recurse_graph: bool) -> Iterable[Any]: ...
