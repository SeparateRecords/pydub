from __future__ import annotations
from .audio_segment import AudioSegment

def detect_silence(
    audio_segment: AudioSegment,
    *,
    min_silence_len: int = ...,
    silence_thresh: float = ...,
    seek_step: int = ...,
) -> list[list[int]]: ...
def detect_nonsilent(
    audio_segment: AudioSegment,
    *,
    min_silence_len: int = ...,
    silence_thresh: float = ...,
    seek_step: int = ...,
) -> list[AudioSegment]: ...
def split_on_silence(
    audio_segment: AudioSegment,
    *,
    min_silence_len: int = ...,
    silence_thresh: float = ...,
    keep_silence: float | bool = ...,
    seek_step: int = ...,
) -> list[AudioSegment]: ...
def detect_leading_silence(
    sound: AudioSegment, *, silence_threshold: float = ..., chunk_size: int = ...
) -> int: ...
