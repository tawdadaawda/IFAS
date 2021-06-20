from components.setImage import SetImage


class ScreenTransitHandler(object):
    def __init__(self):

        None

    def transit(frame, flag):
        if flag == "topToChoosing":
            frame.createChooseScreen()

        elif flag == "choosingToChoosing2":
            frame.createChoose2Screen()

        elif flag == "choosing2ToShutter":
            frame.createShutterScreen()

        elif flag == "shutterToFitting":
            frame.createFittingScreen()

        elif flag == "fittingToSimilarOrSame":
            frame.createSimilarOrSameScreen()

        elif flag == "similarOrSameToProperty":
            frame.createPropertyScreen()

        elif flag == "propertyToFitting2":
            frame.createFitting2Screen()

        elif flag == "fitting2ToPurchase":
            frame.createPurchaseScreen()

        elif flag == "purchaseToComplete":
            frame.createCompleteScreen()

        elif flag == "completeToTop":
            frame.createTopScreen()
