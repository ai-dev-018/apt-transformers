from typing import TYPE_CHECKING

from ...utils import (
    OptionalDependencyNotAvailable,
    _LazyModule,
    is_torch_available,
)


_import_structure = {
    "configuration_lumina": ["LUMINA_PRETRAINED_CONFIG_ARCHIVE_MAP", "LuminaConfig"],
}


try:
    if not is_torch_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["modeling_lumina"] = [
        "LuminaForCausalLM",
        "LuminaModel",
        "LuminaPreTrainedModel",
        "LuminaForSequenceClassification",
    ]


if TYPE_CHECKING:
    from .configuration_lumina import LUMINA_PRETRAINED_CONFIG_ARCHIVE_MAP, LuminaConfig

    try:
        if not is_torch_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        pass
    else:
        from .modeling_lumina import (
            LuminaForCausalLM,
            LuminaForSequenceClassification,
            LuminaModel,
            LuminaPreTrainedModel,
        )


else:
    import sys

    sys.modules[__name__] = _LazyModule(__name__, globals()["__file__"], _import_structure, module_spec=__spec__)
