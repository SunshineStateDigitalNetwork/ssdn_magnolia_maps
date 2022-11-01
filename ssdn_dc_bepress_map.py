import logging

from manatus import SourceResource

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
logger.debug(f'Loaded {__name__} map')


def ssdn_dc_bepress_map(rec):
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
        sr.date = {'begin': rec.date,
                   'end': rec.date,
                   'displayDate': rec.date}
    except TypeError:
        logger.info(f"No date - {rec.harvest_id}")

    # description
    sr.description = rec.description

    # format
    sr.format = rec.format

    # identifier
    for identifier in rec.identifier:
        if identifier.startswith('http'):
            sr.identifier = identifier

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
    tn = None

    yield sr, tn
