"""
Numpy's mypy stub. Only type declarations for ndarray, the scalar hierarchy and array creation
methods are provided.
"""

from typing import (Any, Callable, Dict, Generic, Iterator, List, Optional, Sequence, Tuple, Type,
                    TypeVar, Union)
from abc import ABCMeta

class dtype: ...
_dtype = dtype


class flagsobj:
    """numpy.flagsobj"""
    aligned = None       # type: bool
    behaved = None       # type: bool
    c_contiguous = None  # type: bool
    carray = None        # type: bool
    contiguous = None    # type: bool
    f_contiguous = None  # type: bool
    farray = None        # type: bool
    fnc = None           # type: bool
    forc = None          # type: bool
    fortran = None       # type: bool
    owndata = None       # type: bool
    updateifcopy = None  # type: bool
    writeable = None     # type: bool
    def __getitem__(self, item: str) -> bool: ...
    def __setitem__(self, item: str, value: bool) -> None: ...

#
# Type variables. _T wasn't used to avoid confusions with ndarray's "T" attribute.
#

_S = TypeVar('_S')
_U = TypeVar('_U')
_V = TypeVar('_V')
_A = TypeVar('_A', bound='_ArrayLike', covariant=True)


#
# Auxiliary types
#

ShapeType = Union[int, Tuple[int, ...]]
AxesType = Union[int, Tuple[int, ...]]
OrderType = Union[str, Sequence[str]]
DtypeType = Union[dtype, type]

class flatiter(Generic[_S], Iterator[_S], metaclass=ABCMeta):
    coords = ...  # type: ShapeType
    def copy(self) -> flatiter[_S]: ...

class _ArrayLike(Generic[_S]):
    """
    "array-like" interface that both numpy.ndarray and all scalars (descendants of numpy.generic)
    implement this interface.
    """
    #
    # Array-like structures attributes
    #
    # T: _ArrayLike[_S] = ...
    @property
    def T(self: _A) -> _A: ...

    d: Any = ...
    dtype: _dtype = ...
    flags: flagsobj = ...
    @property
    def flat(self: _A) -> flatiter[_A]: ...
    @property
    def imag(self: _A) -> _A: ...
    @property
    def real(self: _A) -> _A: ...
    size: int = ...
    itemsize: int = ...
    nbytes: int = ...
    ndim: int = ...
    shape: Tuple[int, ...] = ...
    strides: Tuple[int, ...] = ...
    @property
    def base (self: _A) -> Optional[_A]: ...

    #
    # Array-like methods
    #

    # Once this issue https://github.com/python/mypy/issues/1907 is resolved, most methods that
    # have an 'out' argument, will be implemented using overload instead of with a Union
    # result. mypy is smart enough to assign the proper type (_ArrayLike[_U]) when out is present
    # but it falls back to the union when it's not.
    def all(self: _A, axis: AxesType=None, out: '_ArrayLike[_U]'=None,
            keepdims: bool=False) -> Union['_ArrayLike[_U]', '_ArrayLike[bool]']: ...

    def any(self: _A, axis: AxesType=None, out: '_ArrayLike[_U]'=None,
            keepdims: bool=False) -> Union['_ArrayLike[_U]', '_ArrayLike[bool]']: ...

    def argmax(self: _A, axis: int=None,
               out: '_ArrayLike[_U]'=None) -> Union['_ArrayLike[_U]', '_ArrayLike[int]']: ...

    def argmin(self: _A, axis: int=None,
               out: '_ArrayLike[_U]'=None) -> Union['_ArrayLike[_U]', '_ArrayLike[int]']: ...

    def argpartition(self: _A, kth: Union[int, Sequence[int]], axis: Optional[int]=-1,
                     kind: str='introselect', order: OrderType=None) -> '_ArrayLike[int]': ...

    def argsort(self: _A, axis: int=None, kind: str='quicksort',
                order: OrderType=None) -> '_ArrayLike[int]': ...

    def astype(self: _A, dtype: Any, order: str='K', casting: str='unsafe', subok: bool=True,
               copy: bool=False) -> '_ArrayLike[Any]': ...

    def byteswap(self: _A, inplace: bool=False) -> '_ArrayLike[_S]': ...

    def choose(self: _A, choices:Sequence['_ArrayLike[_V]'], out: '_ArrayLike[_U]'=None,
               mode: str='raise') ->  Union['_ArrayLike[_U]', '_ArrayLike[_V]']: ...

    def clip(self: _A, a_min: Any, a_max: Any,
             out: '_ArrayLike[_U]'=None) -> Union['_ArrayLike[_S]', '_ArrayLike[_U]']: ...

    def compress(self: _A, condition: Sequence[bool], axis: int=None,
                 out: '_ArrayLike[_U]'=None) -> Union['_ArrayLike[_S]', '_ArrayLike[_U]']: ...

    def conj(self) -> '_ArrayLike[_S]': ...

    def conjugate(self) -> '_ArrayLike[_S]': ...

    def copy(self: _A, order: str='C') -> '_ArrayLike[_S]': ...

    def cumprod(self: _A, axis: int=None, dtype: Any=None,
                out: '_ArrayLike[Any]'=None) -> '_ArrayLike[Any]': ...

    def cumsum(self: _A, axis: int=None, dtype: DtypeType=None,
                out: '_ArrayLike[Any]'=None) -> '_ArrayLike[Any]': ...

    def diagonal(self: _A, offset: int=0, axis1: int=0, axis2: int=1) -> '_ArrayLike[_S]': ...

    def dot(self: _A, b: '_ArrayLike[Any]', out: '_ArrayLike[Any]'=None) -> '_ArrayLike[Any]': ...

    def dump(self: _A, file: str) -> None: ...

    def dumps(self) -> str: ...

    def fill(self: _A, value: _S) -> None: ...

    def flatten(self: _A, order: str='C') -> '_ArrayLike[_S]': ...

    def getfield(self: _A, dtype: DtypeType, offset: int=0) -> '_ArrayLike[Any]': ...

    def item(self: _A, args: AxesType) -> generic: ...

    def itemset(self: _A, arg0: Union[int, Tuple[int, ...]], arg1: Any=None) -> None: ...

    def max(self: _A, axis: AxesType=None,
            out: '_ArrayLike[_U]'=None) -> Union['_ArrayLike[_S]', '_ArrayLike[_U]']: ...

    def mean(self: _A, axis: AxesType=None, dtype: Any=None,
             out: '_ArrayLike[_U]'=None, keepdims: bool=False) -> '_ArrayLike[floating]': ...

    def min(self: _A, axis: AxesType=None,
            out: '_ArrayLike[_U]'=None) -> Union['_ArrayLike[_S]', '_ArrayLike[_U]']: ...

    def newbyteorder(self: _A, new_order: str='S') -> '_ArrayLike[_S]': ...

    def nonzero(self) -> '_ArrayLike[int]': ...

    def partition(self: _A, kth: AxesType, axis: int=-1, kind: str='introselect',
                  order: OrderType=None) -> None: ...

    def prod(self: _A, axis: AxesType=None, dtype: DtypeType=None,
             out: '_ArrayLike[_U]'=None, keepdims: bool=False) -> '_ArrayLike[Any]': ...

    def ptp(self: _A, axis: int=None,
            out: '_ArrayLike[_U]'=None) -> Union['_ArrayLike[_S]', '_ArrayLike[_U]']: ...

    def put(self: _A, ind: '_ArrayLike[int]', v: '_ArrayLike[_S]', mode: str='raise') -> None: ...

    def ravel(self: _A, order: str='C') -> '_ArrayLike[_S]': ...

    def repeat(self: _A, repeats: Union[int, Sequence[int]],
               axis: int=None) -> '_ArrayLike[_S]': ...

    def reshape(self: _A, newshape: ShapeType,
                order: str='C') -> '_ArrayLike[_S]': ...

    def resize(self: _A, new_shape: ShapeType, refcheck: bool=True) -> None: ...

    def round(self: _A, decimals: int=0,
              out: '_ArrayLike[_U]'=None) -> Union['_ArrayLike[_S]', '_ArrayLike[_U]']: ...

    def searchsorted(self: _A, v: Union[_S, '_ArrayLike[_S]'], side: str='left',
                     sorter: '_ArrayLike[int]'=None) -> '_ArrayLike[int]': ...

    def setfield(self: _A, val: Any, dtype: DtypeType, offset: int=0) -> None: ...

    def setflags(self: _A, write: bool=None, align: bool=None,
                 uic: bool=None) -> None: ...

    def sort(self: _A, axis: int=-1, kind: str='quicksort', order: OrderType=None) -> None: ...

    def squeeze(self: _A, axis: AxesType=None) -> '_ArrayLike[_S]': ...

    def std(self: _A, axis: AxesType=None, dtype: DtypeType=None,
            out: '_ArrayLike[_U]'=None, ddof: int=0, keepdims: bool=False) -> '_ArrayLike[floating]': ...

    def sum(self: _A, axis: AxesType=None, dtype: DtypeType=None,
            out: '_ArrayLike[_U]'=None,
            keepdims: bool=False) -> '_ArrayLike[Any]': ...

    def swapaxes(self: _A, axis1: int, axis2: int) -> '_ArrayLike[_S]': ...

    def take(self: _A, indices: Sequence[int], axis: int=None,
             out: '_ArrayLike[_U]'=None,
             mode: str='raise') -> Union['_ArrayLike[_S]', '_ArrayLike[_U]']: ...

    def tobytes(self: _A, order: str='C') -> bytes: ...

    def tofile(self: _A, fid: object, sep: str='',  # TODO fix fid definition (There's a bug in mypy io's namespace https://github.com/python/mypy/issues/1462)
               format: str='%s') -> None: ...

    def tolist(self) -> List[Any]: ...

    def tostring(self: _A, order: str='C') -> bytes: ...

    def trace(self: _A, offset: int=0, axis1: int=0, axis2: int=1,
              dtype: DtypeType=None, out: '_ArrayLike[_U]'=None) -> '_ArrayLike[Any]': ...

    def transpose(self: _A, axes: Optional[AxesType]) -> '_ArrayLike[_S]': ...

    def var(self: _A, axis: AxesType=None, dtype: DtypeType=None,
            out: '_ArrayLike[_U]'=None, ddof: int=0, keepdims: bool=False) -> '_ArrayLike[Any]': ...

    def view(self: _A, dtype: Union[DtypeType, Type['ndarray']]=None,
             type: type=None) -> '_ArrayLike[Any]': ...

    #
    # Magic methods
    #

    def __abs__(self) -> '_ArrayLike[_S]': ...

    def __add__(self: _A, value: object) -> '_ArrayLike[Any]': ...

    def __and__(self: _A, value: object) -> '_ArrayLike[int]': ...

    def __array__(self: _A, dtype: DtypeType=None) -> '_ArrayLike[Any]': ...

    def __array_prepare__(self: _A, context: object=None) -> '_ArrayLike[Any]': ...

    def __array_wrap__(self: _A, context: object=None) -> '_ArrayLike[Any]': ...

    def __bool__(self) -> bool: ...

    def __complex__(self) -> complex: ...

    def __contains__(self: _A, key: object) -> bool: ...

    def __copy__(self) -> '_ArrayLike[_S]': ...

    def __deepcopy__(self) -> '_ArrayLike[_S]': ...

    def __delattr__(self: _A, name: str) -> None: ...

    def __delitem__(self: _A, key: str) -> None: ...

    def __dir__(self) -> List[str]: ...

    def __divmod__(self: _A, value: object) -> Tuple['_ArrayLike[int]', '_ArrayLike[float]']: ...

    def __eq__(self: _A, value: object) -> '_ArrayLike[bool]': ...  # type: ignore

    def __float__(self) -> float: ...

    def __floordiv__(self: _A, value: object) -> '_ArrayLike[int]': ...

    def __ge__(self: _A, value: object) -> '_ArrayLike[bool]': ...

    def __getattribute__(self: _A, name: str) -> Any: ...

    def __getitem__(self: _A, key: Any) -> '_ArrayLike[_S]': ...

    def __gt__(self: _A, value: object) -> '_ArrayLike[bool]': ...

    def __iadd__(self: _A, value: object) -> None: ...

    def __iand__(self: _A, value: object) -> None: ...

    def __ifloordiv__(self: _A, value: object) -> None: ...

    def __ilshift__(self: _A, value: object) -> None: ...

    def __imatmul__(self: _A, value: '_ArrayLike[Any]') -> None: ...

    def __imod__(self: _A, value: object) -> None: ...

    def __imul__(self: _A, value: object) -> None: ...

    def __index__(self) -> int: ...

    def __int__(self) -> int: ...

    def __invert__(self) -> '_ArrayLike[_S]': ...

    def __ior__(self: _A, value: object) -> None: ...

    def __ipow__(self: _A, value: object) -> None: ...

    def __irshift__(self: _A, value: object) -> None: ...

    def __isub__(self: _A, value: object) -> None: ...

    def __iter__(self) -> Iterator['_ArrayLike[_S]']: ...

    def __itruediv__(sel, value: object) -> None: ...

    def __ixor__(self: _A, value: object) -> None: ...

    def __le__(self: _A, value: object) -> '_ArrayLike[bool]': ...

    def __len__(self) -> int: ...

    def __lshift__(self: _A, value: object) -> '_ArrayLike[_S]': ...

    def __lt__(self: _A, value: object) -> '_ArrayLike[bool]': ...

    def __matmul__(self: _A, value: '_ArrayLike[Any]') -> '_ArrayLike[Any]': ...

    def __mod__(self: _A, value: object) -> '_ArrayLike[_S]': ...

    def __mul__(self: _A, value: object) -> '_ArrayLike[Any]': ...

    def __ne__(self: _A, value: object) -> '_ArrayLike[bool]': ...  # type: ignore

    def __neg__(self) -> '_ArrayLike[_S]': ...

    def __or__(self: _A, value: object) -> '_ArrayLike[_S]': ...

    def __pos__(self) -> '_ArrayLike[_S]': ...

    def __pow__(self: _A, value: object) -> '_ArrayLike[Any]': ...

    def __radd__(self: _A, value: object) -> '_ArrayLike[Any]': ...

    def __rand__(self: _A, value: object) -> '_ArrayLike[_S]': ...

    def __rdivmod__(self: _A, value: object) -> Tuple['_ArrayLike[int]', '_ArrayLike[float]']: ...

    def __rfloordiv__(self: _A, value: object) -> '_ArrayLike[Any]': ...

    def __rlshift__(self: _A, value: object) -> '_ArrayLike[Any]': ...

    def __rmatmul__(self: _A, value: object) -> '_ArrayLike[Any]': ...

    def __rmod__(self: _A, value: object) -> '_ArrayLike[Any]': ...

    def __rmul__(self: _A, value: object) -> '_ArrayLike[Any]': ...

    def __ror__(self: _A, value: object) -> '_ArrayLike[_S]': ...

    def __rpow__(self: _A, value: object) -> '_ArrayLike[Any]': ...

    def __rrshift__(self: _A, value: object) -> '_ArrayLike[Any]': ...

    def __rshift__(self: _A, value: object) -> '_ArrayLike[Any]': ...

    def __rsub__(self: _A, value: object) -> '_ArrayLike[Any]': ...

    def __rtruediv__(self: _A, value: object) -> '_ArrayLike[Any]': ...

    def __rxor__(self: _A, value: object) -> '_ArrayLike[_S]': ...

    def __setattr__(self: _A, name: str, value: Any) -> None: ...

    def __setitem__(self: _A, key: Any, value: Any) -> None: ...

    def __str__(self) -> str: ...

    def __sub__(self: _A, value: object) -> '_ArrayLike[Any]': ...

    def __truediv__(sel, value: object) -> '_ArrayLike[Any]': ...

    def __xor__(self: _A, value: object) -> '_ArrayLike[_S]': ...

#
# numpy's scalar hierarchy (http://docs.scipy.org/doc/numpy/reference/arrays.scalars.html#scalars)
#

class generic(_ArrayLike[_S], Generic[_S]): ...
class bool_(generic[bool]): ...
bool8 = bool_
class object_(generic[Any]): ...
class number(generic[_S], Generic[_S]): ...
class integer(number[int]): ...
class signedinteger(integer): ...
class byte(signedinteger): ...
class short(signedinteger): ...
class intc(signedinteger): ...
class int_(signedinteger): ...
class longlong(signedinteger): ...
class int8(signedinteger): ...
class int16(signedinteger): ...
class int32(signedinteger): ...
class int64(signedinteger): ...
class unsignedinteger(integer): ...
class ubyte(unsignedinteger): ...
class ushort(unsignedinteger): ...
class uintc(unsignedinteger): ...
class uint(unsignedinteger): ...
class ulonglong(unsignedinteger): ...
class uint8(signedinteger): ...
class uint16(signedinteger): ...
class uint32(signedinteger): ...
class uint64(signedinteger): ...
class inexact(number[float]): ...
class floating(inexact): ...
class half(floating): ...
class single(floating): ...
class float_(floating): ...
class longfloat_(floating): ...
class longdouble(floating): ...
class float16(floating): ...
class float32(floating): ...
class float64(floating): ...
class float128(floating): ...
class complexfloating(inexact): ...
class csingle(complexfloating): ...
class complex_(complexfloating): ...
class clongfloat(complexfloating): ...
class complex64(complexfloating): ...
class complex128(complexfloating): ...
class complex256(complexfloating): ...
class flexible(generic[_S], Generic[_S]): ...
class character(flexible[str]): ...
class str_(character): ...
class unicode_(character): ...
class void(flexible[None]): ...

class ndarray(_ArrayLike[_S], Generic[_S]):
    """numpy.ndarray"""
    ctypes = None    # type: Any  # TODO Implement ctypes type hint

    # TODO Need to find a way to restrict buffer type
    def __init__(self: ndarray, shape: Tuple[int, ...], dtype: DtypeType=None,
                 buffer: Any=None, offset: int=None,
                 strides: Tuple[int, ...]=None, order: str=None) -> None: ...

#
# Array creation routines
#

def array(object: Any, dtype: Any=None, copy: bool=True,
          order: str=None, subok: bool=False,
          ndmin: int=0) -> ndarray[Any]: ...
def asarray(a: Any, dtype: DtypeType=None, order: str=None) -> ndarray[Any]: ...
def asanyarray(a: Any, dtype: DtypeType=None, order: str=None) -> ndarray[Any]: ...  # TODO figure out a way to restrict the return type
def asmatrix(data: Any, dtype: DtypeType=None) -> Any: ...  # TODO define matrix
def ascontiguousarray(a: Any, dtype: DtypeType=None) -> ndarray[Any]: ...
def copy(a: Any, order: str=None)	-> ndarray[Any]: ...
def empty(shape: ShapeType, dtype: DtypeType=float, order: str='C') -> ndarray[Any]: ...
def empty_like(a: Any, dtype: Any=None, order: str='K', subok: bool=True) -> ndarray[Any]: ...
def eye(N: int, M: int=None, k: int=0, dtype: DtypeType=float) -> ndarray[Any]: ...
def frombuffer(buffer: Any, dtype: DtypeType=float, count: int=-1,  # TODO figure out a way to restrict buffer
               offset: int=0) -> ndarray[Any]: ...
def fromfile(file: object, dtype: DtypeType=float, count: int=-1, sep: str='') -> ndarray[Any]: ...  # TODO fix file definition (There's a bug in mypy io's namespace https://github.com/python/mypy/issues/1462)
def full(shape: ShapeType, fill_value: Any, dtype: DtypeType=None,
         order: str='C') -> ndarray[Any]: ...
def full_like(a: Any, fill_value: Any, dtype: DtypeType=None, order: str='C',
              subok: bool=True) -> ndarray[Any]: ...
def fromfunction(function: Callable[..., _S], shape: ShapeType, dtype: DtypeType=float) -> ndarray[_S]: ...
def fromiter(iterable: Iterator[Any], dytpe: DtypeType, count: int=-1) -> ndarray[Any]: ...
def fromstring(string: str, dtype: DtypeType=float, count: int=-1, sep: str='') -> ndarray[Any]: ...
def identity(n: int, dtype: DtypeType=None) -> ndarray[Any]: ...
def loadtxt(fname: Any, dtype: DtypeType=float, comments: Union[str, Sequence[str]]='#',
            delimiter: str=None, converters: Dict[int, Callable[[Any], float]]=None,
            skiprows: int=0, usecols: Sequence[int]=None,
            unpack: bool=False, ndmin: int=0) -> ndarray[float]: ...
def ones(shape: ShapeType, dtype: Optional[DtypeType]=..., order: str='C') -> ndarray[Any]: ...
def ones_like(a: Any, dtype: Any=None, order: str='K', subok: bool=True) -> ndarray[Any]: ...
def zeros(shape: ShapeType, dtype: DtypeType=float, order: str='C') -> ndarray[Any]: ...
def zeros_like(a: Any, dtype: Any=None, order: str='K', subok: bool=True) -> ndarray[Any]: ...


# Specific values
inf: float
