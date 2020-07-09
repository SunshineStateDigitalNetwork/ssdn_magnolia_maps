import logging

from citrus import SourceResource

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
logger.debug(f'Loaded {__name__} map')


def fiu_dc_map(rec):
    sr = SourceResource()

    # contributor
    if rec.contributor:
        sr.contributor = [{'name': contributor} for contributor in
                          rec.contributor]

    # creator
    if rec.creator:
        sr.creator = [{'name': creator} for creator in
                      rec.creator]

    # date
    try:
        sr.date = {'begin': rec.date[0],
                   'end': rec.date[0],
                   'displayDate': rec.date[0]}
    except TypeError:
        logger.info(f"No date - {rec.harvest_id}")

    # description
    sr.description = rec.description

    # format
    sr.format = rec.format

    # identifier
    try:
        for identifier in rec.identifier:
            if 'dpanther.fiu.edu' in identifier:
                sr.identifier = identifier
    except (TypeError, AttributeError):
        logger.error(f"No identifier - {rec.harvest_id}")
        return None

    # language
    try:
        sr.language = [{'name': lang} for lang in rec.language]
    except TypeError:
        logger.info(f"No language - {rec.harvest_id}")

    # place
    if rec.place:
        sr.spatial = [{'name': place} for place in rec.place]

    # publisher
    sr.publisher = rec.publisher

    # rights
    try:
        if len(rec.rights) > 1:
            for r in rec.rights:
                if r.startswith('http'):
                    sr.rights = [{'@id': r}]
        else:
            if rec.rights[0].startswith('http'):
                sr.rights = [{'@id': rec.rights[0]}]
            else:
                logger.warning(f"No rights URI - {rec.harvest_id}")
                sr.rights = [{'text': rec.rights[0]}]
    except TypeError:
        logger.error(f"No rights - {rec.harvest_id}")
        return None

    # subject
    if rec.subject:
        sr.subject = [{'name': subject} for subject in rec.subject]

    # title
    sr.title = rec.title

    # type
    sr.type = rec.type

    # thumbnail
    if rec.thumbnail:
        tn = rec.thumbnail
    else:
        tn = None

    yield sr, tn
