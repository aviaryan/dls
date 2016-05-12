from models import Data


def getType(strId):
    data = Data.query.filter_by(strId=strId).first()
    return 0 if data is None else 1


def getText(strId):
    data = Data.query.filter_by(strId=strId).first()
    return '' if data is None else data.text
