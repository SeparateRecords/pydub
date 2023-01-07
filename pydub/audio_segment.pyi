from __future__ import annotations

import os
from array import array
from typing import (
    Any,
    ClassVar,
    Iterator,
    Literal,
    Sequence,
    TypedDict,
    BinaryIO,
    overload,
)

_PathLike = str | bytes | os.PathLike[Any]
_AudioDataSource = str | bytes | array[int] | BinaryIO

class Metadata(TypedDict):
    channels: int
    frame_rate: int
    frame_width: int
    sample_width: int

class PartialMetadata(TypedDict, total=False):
    channels: int
    frame_rate: int
    frame_width: int
    sample_width: int

class AudioSegment:
    converter: ClassVar[str]
    DEFAULT_CODECS: ClassVar[dict[str, str]]
    @overload
    def __init__(self, data: _AudioDataSource) -> None: ...
    @overload
    def __init__(
        self,
        data: _AudioDataSource,
        *,
        sample_width: int,
        frame_rate: int,
        channels: int,
    ) -> None: ...
    @overload
    def __init__(self, data: _AudioDataSource, *, metadata: Metadata) -> None: ...
    def __add__(self, arg: float | AudioSegment) -> AudioSegment: ...
    def __radd__(self, rarg: AudioSegment) -> AudioSegment: ...
    def __sub__(self, arg: float) -> AudioSegment: ...
    def __mul__(self, arg: int | AudioSegment) -> AudioSegment: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[AudioSegment]: ...
    def __getitem__(self, ms: int | slice) -> AudioSegment: ...
    def __getattr__(self, attr: str) -> Any: ...
    @property
    def channels(self) -> int: ...
    @property
    def sample_width(self) -> int: ...
    @property
    def frame_rate(self) -> int: ...
    @property
    def frame_width(self) -> int: ...
    @property
    def rms(self) -> float: ...
    @property
    def max(self) -> float: ...
    @property
    def dBFS(self) -> float: ...
    @property
    def max_dBFS(self) -> float: ...
    @property
    def max_possible_amplitude(self) -> float: ...
    @property
    def duration_seconds(self) -> int: ...
    @property
    def raw_data(self) -> bytes: ...
    @property
    def array_type(self) -> Literal["b", "B", "h", "H", "i", "I"]: ...
    def _spawn(
        self,
        data: _AudioDataSource | list[bytes],
        overrides: PartialMetadata = ...,
    ) -> AudioSegment: ...
    @overload
    def export(
        self,
        out_f: _PathLike | None = ...,
        *,
        format: str = ...,
        codec: str | None = ...,
        bitrate: str | None = ...,
        tags: dict[str, str | None] = ...,
        parameters: Sequence[str | None] = ...,
        id3v2_version: Literal["3", "4"] = ...,
        cover: str | None = ...,
    ) -> BinaryIO: ...
    @overload  # fallback
    def export(
        self,
        out_f: _PathLike | None = ...,
        *,
        format: str = ...,
        codec: str | None = ...,
        bitrate: str | None = ...,
        tags: dict[str, str | None] = ...,
        parameters: Sequence[str | None] = ...,
        id3v2_version: str = ...,
        cover: str | None = ...,
    ) -> BinaryIO: ...
    def frame_count(self, ms: int = ...) -> float: ...
    def get_frame(self, index: int) -> bytes: ...
    def get_sample_slice(
        self, start_sample: int | None = ..., end_sample: int | None = ...
    ) -> AudioSegment: ...
    def append(self, seg: AudioSegment, *, crossfade: int = ...) -> AudioSegment: ...
    def overlay(
        self,
        seg: AudioSegment,
        *,
        position: int = ...,
        loop: bool = ...,
        times: int | None = ...,
        gain_during_overlay: int | None = ...,
    ) -> AudioSegment: ...
    def apply_gain(self, volume_change: float) -> AudioSegment: ...
    @overload
    def fade(
        self, *, start: int, end: int, to_gain: float = ..., from_gain: float = ...
    ) -> AudioSegment: ...
    @overload
    def fade(
        self, *, start: int, duration: int, to_gain: float = ..., from_gain: float = ...
    ) -> AudioSegment: ...
    @overload
    def fade(
        self, *, end: int, duration: int, to_gain: float = ..., from_gain: float = ...
    ) -> AudioSegment: ...
    def fade_out(self, duration: int) -> AudioSegment: ...
    def fade_in(self, duration: int) -> AudioSegment: ...
    def reverse(self) -> AudioSegment: ...
    def set_sample_width(self, sample_width: int) -> AudioSegment: ...
    def set_frame_rate(self, frame_rate: int) -> AudioSegment: ...
    def set_channels(self, channels: int) -> AudioSegment: ...
    def split_to_mono(self) -> list[AudioSegment]: ...
    @overload
    def get_array_of_samples(
        self,
        array_type_override: Literal["b", "B", "h", "H", "i", "I", "l", "L", "q", "Q"]
        | None = ...,
    ) -> array[int]: ...
    @overload  # fallback
    def get_array_of_samples(
        self,
        array_type_override: str | None = ...,
    ) -> array[int]: ...
    @overload
    def get_dc_offset(self, channel: Literal[1, 2]) -> int: ...
    @overload  # fallback
    def get_dc_offset(self, channel: int) -> int: ...
    @overload
    def remove_dc_offset(
        self, channel: Literal[1, 2] | None = ..., offset: float | None = ...
    ) -> AudioSegment: ...
    @overload  # fallback
    def remove_dc_offset(
        self, channel: int | None = ..., offset: float | None = ...
    ) -> AudioSegment: ...
    @overload
    @classmethod
    def from_file(
        cls,
        file: _PathLike,
        *,
        format: str | None = ...,
        codec: str | None = ...,
        read_ahead_limit: int = ...,
        parameters: Sequence[str | None] = ...,
        start_second: float | None = ...,
        duration: float | None = ...,
    ) -> AudioSegment: ...
    @overload
    @classmethod
    def from_file(
        cls,
        file: _PathLike,
        *,
        channels: int,
        frame_rate: int,
        sample_width: int,
        format: str | None = ...,
        codec: str | None = ...,
        read_ahead_limit: int = ...,
        parameters: Sequence[str | None] = ...,
        start_second: float | None = ...,
        duration: float | None = ...,
    ) -> AudioSegment: ...
    @overload
    @classmethod
    def from_file_using_temporary_files(
        cls,
        file: _PathLike,
        *,
        format: str | None = ...,
        codec: str | None = ...,
        parameters: Sequence[str | None] = ...,
        start_second: float | None = ...,
        duration: float | None = ...,
    ) -> AudioSegment: ...
    @overload
    @classmethod
    def from_file_using_temporary_files(
        cls,
        file: _PathLike,
        *,
        channels: int,
        frame_rate: int,
        sample_width: int,
        format: str | None = ...,
        codec: str | None = ...,
        parameters: Sequence[str | None] = ...,
        start_second: float | None = ...,
        duration: float | None = ...,
    ) -> AudioSegment: ...
    @classmethod
    def from_mp3(
        cls, file: _PathLike, parameters: Sequence[str | None] = ...
    ) -> AudioSegment: ...
    @classmethod
    def from_flv(
        cls, file: _PathLike, parameters: Sequence[str | None] = ...
    ) -> AudioSegment: ...
    @classmethod
    def from_ogg(
        cls, file: _PathLike, parameters: Sequence[str | None] = ...
    ) -> AudioSegment: ...
    @classmethod
    def from_wav(
        cls, file: _PathLike, parameters: Sequence[str | None] = ...
    ) -> AudioSegment: ...
    @classmethod
    def from_raw(
        cls, file: _PathLike, *, frame_rate: int, channels: int, sample_width: int
    ) -> AudioSegment: ...
    @classmethod
    def empty(cls) -> AudioSegment: ...
    @classmethod
    def silent(cls, duration: int = ..., frame_rate: int = ...) -> AudioSegment: ...
    @classmethod
    def from_mono_audiosegments(
        cls, __seg: AudioSegment, /, *mono_segments: AudioSegment
    ) -> AudioSegment: ...
