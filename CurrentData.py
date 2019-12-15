from DraftMode import DraftMode
from ModeCollection import ModeCollection


class CurrentData:
    initialParameters = []
    modeCollection = None
    filteredModes = []
    orderedModes = []

    @staticmethod
    def display(details: bool=False, size: int=50):
        if not details:
            ModeCollection.displaySimple(CurrentData.orderedModes)
        else:
            classic = DraftMode.getClassic()
            for i, dM in enumerate(CurrentData.orderedModes):
                if i <= size - 1:
                    dM.display(classic)

