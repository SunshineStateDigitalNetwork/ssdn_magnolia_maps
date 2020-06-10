import logging

from citrus import SourceResource

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
logger.debug(f'Loaded {__name__} map')


def ssdn_dc_bepress_map(rec):
    sr = SourceResource()
    if rec.contributor:
        sr.contributor = [{'name': contributor} for contributor in
                          rec.contributor]
    if rec.creator:
        sr.creator = [{'name': creator} for creator in
                      rec.creator]
    try:
        sr.date = {'begin': rec.date,
                   'end': rec.date,
                   'displayDate': rec.date}
    except TypeError:
        logger.info(f"No date - {rec.harvest_id}")
        pass
    sr.description = rec.description
    sr.format = rec.format
    for identifier in rec.identifier:
        if identifier.startswith('http'):
            sr.identifier = identifier
    try:
        sr.language = [{'name': lang} for lang in rec.language]
    except TypeError:
        logger.info(f"No language - {rec.harvest_id}")
        pass
    if rec.place:
        sr.spatial = [{'name': place} for place in rec.place]
    sr.publisher = rec.publisher
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
    if rec.subject:
        sr.subject = [{'name': subject} for subject in rec.subject]
    sr.title = rec.title
    sr.type = rec.type

    # thumbnail
    tn = None

    yield sr, tn
