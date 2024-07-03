from brainscore_vision import model_registry
from brainscore_vision.model_helpers.brain_transformation import ModelCommitment
from .model import get_model, get_layers

model_registry['effnetb1_cutmixpatch_SAM_robust32_avge6e8e9e10_manylayers_324x288'] = lambda: ModelCommitment(identifier='effnetb1_cutmixpatch_SAM_robust32_avge6e8e9e10_manylayers_324x288', activations_model=get_model('effnetb1_cutmixpatch_SAM_robust32_avge6e8e9e10_manylayers_324x288'), layers=get_layers('effnetb1_cutmixpatch_SAM_robust32_avge6e8e9e10_manylayers_324x288'))
