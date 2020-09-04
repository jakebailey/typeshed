from typing import Iterable, List, Optional, Text, Tuple

from google.protobuf.descriptor_pb2 import FileOptions
from google.protobuf.internal.containers import RepeatedCompositeFieldContainer, RepeatedScalarFieldContainer
from google.protobuf.message import Message

class MethodOpt1(int):
    @classmethod
    def Name(cls, number: int) -> bytes: ...
    @classmethod
    def Value(cls, name: bytes) -> MethodOpt1: ...
    @classmethod
    def keys(cls) -> List[bytes]: ...
    @classmethod
    def values(cls) -> List[MethodOpt1]: ...
    @classmethod
    def items(cls) -> List[Tuple[bytes, MethodOpt1]]: ...

METHODOPT1_VAL1: MethodOpt1
METHODOPT1_VAL2: MethodOpt1

class AggregateEnum(int):
    @classmethod
    def Name(cls, number: int) -> bytes: ...
    @classmethod
    def Value(cls, name: bytes) -> AggregateEnum: ...
    @classmethod
    def keys(cls) -> List[bytes]: ...
    @classmethod
    def values(cls) -> List[AggregateEnum]: ...
    @classmethod
    def items(cls) -> List[Tuple[bytes, AggregateEnum]]: ...

VALUE: AggregateEnum

class TestMessageWithCustomOptions(Message):
    class AnEnum(int):
        @classmethod
        def Name(cls, number: int) -> bytes: ...
        @classmethod
        def Value(cls, name: bytes) -> TestMessageWithCustomOptions.AnEnum: ...
        @classmethod
        def keys(cls) -> List[bytes]: ...
        @classmethod
        def values(cls) -> List[TestMessageWithCustomOptions.AnEnum]: ...
        @classmethod
        def items(cls) -> List[Tuple[bytes, TestMessageWithCustomOptions.AnEnum]]: ...
    ANENUM_VAL1: TestMessageWithCustomOptions.AnEnum
    ANENUM_VAL2: TestMessageWithCustomOptions.AnEnum
    field1: Text
    oneof_field: int
    def __init__(self, field1: Optional[Text] = ..., oneof_field: Optional[int] = ...) -> None: ...

class CustomOptionFooRequest(Message):
    def __init__(self) -> None: ...

class CustomOptionFooResponse(Message):
    def __init__(self) -> None: ...

class CustomOptionFooClientMessage(Message):
    def __init__(self) -> None: ...

class CustomOptionFooServerMessage(Message):
    def __init__(self) -> None: ...

class DummyMessageContainingEnum(Message):
    class TestEnumType(int):
        @classmethod
        def Name(cls, number: int) -> bytes: ...
        @classmethod
        def Value(cls, name: bytes) -> DummyMessageContainingEnum.TestEnumType: ...
        @classmethod
        def keys(cls) -> List[bytes]: ...
        @classmethod
        def values(cls) -> List[DummyMessageContainingEnum.TestEnumType]: ...
        @classmethod
        def items(cls) -> List[Tuple[bytes, DummyMessageContainingEnum.TestEnumType]]: ...
    TEST_OPTION_ENUM_TYPE1: DummyMessageContainingEnum.TestEnumType
    TEST_OPTION_ENUM_TYPE2: DummyMessageContainingEnum.TestEnumType
    def __init__(self) -> None: ...

class DummyMessageInvalidAsOptionType(Message):
    def __init__(self) -> None: ...

class CustomOptionMinIntegerValues(Message):
    def __init__(self) -> None: ...

class CustomOptionMaxIntegerValues(Message):
    def __init__(self) -> None: ...

class CustomOptionOtherValues(Message):
    def __init__(self) -> None: ...

class SettingRealsFromPositiveInts(Message):
    def __init__(self) -> None: ...

class SettingRealsFromNegativeInts(Message):
    def __init__(self) -> None: ...

class ComplexOptionType1(Message):
    foo: int
    foo2: int
    foo3: int
    foo4: RepeatedScalarFieldContainer[int]
    def __init__(
        self, foo: Optional[int] = ..., foo2: Optional[int] = ..., foo3: Optional[int] = ..., foo4: Optional[Iterable[int]] = ...
    ) -> None: ...

class ComplexOptionType2(Message):
    class ComplexOptionType4(Message):
        waldo: int
        def __init__(self, waldo: Optional[int] = ...) -> None: ...
    baz: int
    @property
    def bar(self) -> ComplexOptionType1: ...
    @property
    def fred(self) -> ComplexOptionType2.ComplexOptionType4: ...
    @property
    def barney(self) -> RepeatedCompositeFieldContainer[ComplexOptionType2.ComplexOptionType4]: ...
    def __init__(
        self,
        bar: Optional[ComplexOptionType1] = ...,
        baz: Optional[int] = ...,
        fred: Optional[ComplexOptionType2.ComplexOptionType4] = ...,
        barney: Optional[Iterable[ComplexOptionType2.ComplexOptionType4]] = ...,
    ) -> None: ...

class ComplexOptionType3(Message):
    class ComplexOptionType5(Message):
        plugh: int
        def __init__(self, plugh: Optional[int] = ...) -> None: ...
    qux: int
    @property
    def complexoptiontype5(self) -> ComplexOptionType3.ComplexOptionType5: ...
    def __init__(
        self, qux: Optional[int] = ..., complexoptiontype5: Optional[ComplexOptionType3.ComplexOptionType5] = ...
    ) -> None: ...

class ComplexOpt6(Message):
    xyzzy: int
    def __init__(self, xyzzy: Optional[int] = ...) -> None: ...

class VariousComplexOptions(Message):
    def __init__(self) -> None: ...

class AggregateMessageSet(Message):
    def __init__(self) -> None: ...

class AggregateMessageSetElement(Message):
    s: Text
    def __init__(self, s: Optional[Text] = ...) -> None: ...

class Aggregate(Message):
    i: int
    s: Text
    @property
    def sub(self) -> Aggregate: ...
    @property
    def file(self) -> FileOptions: ...
    @property
    def mset(self) -> AggregateMessageSet: ...
    def __init__(
        self,
        i: Optional[int] = ...,
        s: Optional[Text] = ...,
        sub: Optional[Aggregate] = ...,
        file: Optional[FileOptions] = ...,
        mset: Optional[AggregateMessageSet] = ...,
    ) -> None: ...

class AggregateMessage(Message):
    fieldname: int
    def __init__(self, fieldname: Optional[int] = ...) -> None: ...

class NestedOptionType(Message):
    class NestedEnum(int):
        @classmethod
        def Name(cls, number: int) -> bytes: ...
        @classmethod
        def Value(cls, name: bytes) -> NestedOptionType.NestedEnum: ...
        @classmethod
        def keys(cls) -> List[bytes]: ...
        @classmethod
        def values(cls) -> List[NestedOptionType.NestedEnum]: ...
        @classmethod
        def items(cls) -> List[Tuple[bytes, NestedOptionType.NestedEnum]]: ...
    NESTED_ENUM_VALUE: NestedOptionType.NestedEnum
    class NestedMessage(Message):
        nested_field: int
        def __init__(self, nested_field: Optional[int] = ...) -> None: ...
    def __init__(self) -> None: ...

class OldOptionType(Message):
    class TestEnum(int):
        @classmethod
        def Name(cls, number: int) -> bytes: ...
        @classmethod
        def Value(cls, name: bytes) -> OldOptionType.TestEnum: ...
        @classmethod
        def keys(cls) -> List[bytes]: ...
        @classmethod
        def values(cls) -> List[OldOptionType.TestEnum]: ...
        @classmethod
        def items(cls) -> List[Tuple[bytes, OldOptionType.TestEnum]]: ...
    OLD_VALUE: OldOptionType.TestEnum
    value: OldOptionType.TestEnum
    def __init__(self, value: OldOptionType.TestEnum) -> None: ...

class NewOptionType(Message):
    class TestEnum(int):
        @classmethod
        def Name(cls, number: int) -> bytes: ...
        @classmethod
        def Value(cls, name: bytes) -> NewOptionType.TestEnum: ...
        @classmethod
        def keys(cls) -> List[bytes]: ...
        @classmethod
        def values(cls) -> List[NewOptionType.TestEnum]: ...
        @classmethod
        def items(cls) -> List[Tuple[bytes, NewOptionType.TestEnum]]: ...
    OLD_VALUE: NewOptionType.TestEnum
    NEW_VALUE: NewOptionType.TestEnum
    value: NewOptionType.TestEnum
    def __init__(self, value: NewOptionType.TestEnum) -> None: ...

class TestMessageWithRequiredEnumOption(Message):
    def __init__(self) -> None: ...
