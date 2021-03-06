from eth_utils import (
    is_bytes,
)

from ssz.exceptions import (
    DecodingError,
    InvalidSedesError,
)
from ssz.sedes import (
    sedes_by_name,
)
from ssz.utils import (
    infer_sedes,
    is_sedes,
)


def encode(obj, sedes=None):
    """
    Encode object in SSZ format.
    `sedes` needs to be explicitly mentioned for encode/decode
    of integers(as of now).
    `sedes` parameter could be given as a string or as the
    actual sedes object itself.
    """
    if sedes:
        if sedes in sedes_by_name:
            # Get the actual sedes object from string representation
            sedes_obj = sedes_by_name[sedes]
        else:
            sedes_obj = sedes

        if not is_sedes(sedes_obj):
            raise InvalidSedesError("Invalid sedes object", sedes)

    else:
        sedes_obj = infer_sedes(obj)

    serialized_obj = sedes_obj.serialize(obj)
    return serialized_obj


def decode(ssz, sedes):
    """
    Decode a SSZ encoded object.
    """
    if not is_bytes(ssz):
        raise DecodingError('Can only decode SSZ bytes, got type %s' % type(ssz).__name__, ssz)

    obj = sedes.deserialize(ssz)
    return obj
