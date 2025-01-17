from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterator

from .audio_segment import AudioSegment

class SignalGenerator(ABC):
    sample_rate: int
    bit_depth: int
    def __init__(self, sample_rate: int = ..., bit_depth: int = ...) -> None: ...
    def to_audio_segment(
        self, duration: float = ..., volume: float = ...
    ) -> AudioSegment: ...
    @abstractmethod
    def generate(self) -> Iterator[float]: ...

class Sine(SignalGenerator):
    freq: float
    def __init__(
        self, freq: float, *, sample_rate: int = ..., bit_depth: int = ...
    ) -> None: ...
    def generate(self) -> Iterator[float]: ...

class Pulse(SignalGenerator):
    duty_cycle: float
    def __init__(
        self,
        freq: float,
        duty_cycle: float = ...,
        *,
        sample_rate: int = ...,
        bit_depth: int = ...,
    ) -> None: ...
    def generate(self) -> Iterator[float]: ...

class Square(Pulse):
    def __init__(
        self, freq: float, *, sample_rate: int = ..., bit_depth: int = ...
    ) -> None: ...

class Sawtooth(SignalGenerator):
    def __init__(
        self,
        freq: float,
        duty_cycle: float = ...,
        *,
        sample_rate: int = ...,
        bit_depth: int = ...,
    ) -> None: ...
    def generate(self) -> Iterator[float]: ...

class Triangle(Sawtooth):
    def __init__(
        self, freq: float, *, sample_rate: int = ..., bit_depth: int = ...
    ) -> None: ...

class WhiteNoise(SignalGenerator):
    def generate(self) -> Iterator[float]: ...
