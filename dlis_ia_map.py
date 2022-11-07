import logging

import dateparser
from manatus import SourceResource

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
logger.debug(f'Loaded {__name__} map')


def dlis_ia_map(rec):
    sr = SourceResource()

    # contributor
    try:
        if isinstance(rec.contributor, list):
            sr.contributor = [{'name': name.strip('.')} for name in rec.contributor]
        else:
            sr.contributor = [{'name': rec.contributor.strip('.')}]
    except KeyError:
        pass

    # creator
    try:
        if isinstance(rec.creator, list):
            sr.creator = [{'name': name.strip('.')} for name in rec.creator]
        else:
            sr.creator = [{'name': rec.creator.strip('.')}]
    except KeyError:
        logger.info(f"No creator - {rec.harvest_id}")

    # date
    try:
        if rec.date:
            d = dateparser.parse(rec.date, languages=['en']).date().isoformat()
            sr.date = {"begin": d, "end": d, "displayDate": d}
    except (TypeError, KeyError):
        logger.info(f"No date - {rec.harvest_id}")

    # description
    try:
        if rec.description:
            sr.description = rec.description.strip(' ')
    except KeyError:
        pass

    # identifier
    sr.identifier = 'https://archive.org/details/{}'.format(rec.identifier)

    # language
    try:
        if rec.language:
            sr.language = rec.language
    except KeyError:
        pass

    # rights
    sr.rights = {'@id': 'http://rightsstatements.org/vocab/NoC-US/1.0/'}

    # subject
    try:
        if isinstance(rec.subject, list):
            sr.subject = [{'name': sub.strip('.')} for sub in rec.subject]
        else:
            sr.subject = [{'name': rec.subject.strip('.')}]
    except KeyError:
        logger.info(f"No subject - {rec.harvest_id}")

    # title
    if rec.title:
        sr.title = rec.title
    else:
        logger.error(f"No title - {rec.harvest_id}")
        return None

    # thumbnail
    tn = 'https://archive.org/services/img/{}'.format(rec.identifier)

    yield sr, tn
