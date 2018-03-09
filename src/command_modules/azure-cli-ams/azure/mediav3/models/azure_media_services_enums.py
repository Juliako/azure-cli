# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class AacAudioProfile(Enum):

    aac_lc = "AacLc"
    he_aac_v1 = "HeAacV1"
    he_aac_v2 = "HeAacV2"


class StretchMode(Enum):

    none = "None"
    auto_size = "AutoSize"
    auto_fit = "AutoFit"


class VideoSyncMode(Enum):

    auto = "Auto"
    passthrough = "Passthrough"
    cfr = "Cfr"
    vfr = "Vfr"
    drop = "Drop"


class ClosedCaptionType(Enum):

    side_car = "SideCar"
    stream = "Stream"
    embedded = "Embedded"


class ClosedCaptionFormat(Enum):

    ttml = "Ttml"
    web_vtt = "WebVtt"


class DDPlusACMode(Enum):

    acmod20 = "ACMOD20"
    acmod32 = "ACMOD32"


class DeinterlaceParity(Enum):

    auto = "Auto"
    top_field_first = "TopFieldFirst"
    bottom_field_first = "BottomFieldFirst"


class DeinterlaceMode(Enum):

    off = "Off"
    auto_pixel_adaptive = "AutoPixelAdaptive"


class Rotation(Enum):

    auto = "Auto"
    none = "None"
    rotate0 = "Rotate0"
    rotate90 = "Rotate90"
    rotate180 = "Rotate180"
    rotate270 = "Rotate270"


class LoudnessAdjustment(Enum):

    none = "None"
    auto = "Auto"
    manual = "Manual"


class Flip(Enum):

    none = "None"
    horizontal = "Horizontal"
    vertical = "Vertical"


class H264VideoProfile(Enum):

    auto = "Auto"
    baseline = "Baseline"
    main = "Main"
    high = "High"
    high10 = "High10"
    high422 = "High422"
    high444 = "High444"


class EntropyMode(Enum):

    cabac = "Cabac"
    cavlc = "Cavlc"


class H264RateControlMode(Enum):

    abr = "ABR"
    cbr = "CBR"


class H264Complexity(Enum):

    speed = "Speed"
    balanced = "Balanced"
    quality = "Quality"


class EncoderNamedPreset(Enum):

    adaptive_streaming = "AdaptiveStreaming"
    content_adaptive_multiple_bitrate_mp4 = "ContentAdaptiveMultipleBitrateMP4"
    aac_good_quality_audio = "AACGoodQualityAudio"
    h264_multiple_bitrate1080p = "H264MultipleBitrate1080p"
    h264_multiple_bitrate720p = "H264MultipleBitrate720p"


class StreamSelectionMode(Enum):

    selection_not_set = "SelectionNotSet"
    select_highest_bitrate_stream = "SelectHighestBitrateStream"
    select_lowest_bitrate_stream = "SelectLowestBitrateStream"
    select_all_streams = "SelectAllStreams"


class OnErrorType(Enum):

    stop_processing_job = "StopProcessingJob"
    continue_job = "ContinueJob"


class Priority(Enum):

    low = "Low"
    normal = "Normal"
    high = "High"


class JobErrorCode(Enum):

    service_error = "ServiceError"
    service_transient_error = "ServiceTransientError"
    download_not_accessible = "DownloadNotAccessible"
    download_transient_error = "DownloadTransientError"
    upload_not_accessible = "UploadNotAccessible"
    upload_transient_error = "UploadTransientError"
    configuration_unsupported = "ConfigurationUnsupported"
    content_malformed = "ContentMalformed"
    content_unsupported = "ContentUnsupported"


class JobErrorCategory(Enum):

    service = "Service"
    download = "Download"
    upload = "Upload"
    configuration = "Configuration"
    content = "Content"


class JobRetry(Enum):

    do_not_retry = "DoNotRetry"
    may_retry = "MayRetry"


class JobState(Enum):

    canceled = "Canceled"
    canceling = "Canceling"
    error = "Error"
    finished = "Finished"
    processing = "Processing"
    queued = "Queued"
    scheduled = "Scheduled"


class StorageAccountType(Enum):

    primary = "Primary"
    secondary = "Secondary"