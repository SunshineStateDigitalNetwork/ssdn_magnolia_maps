import logging

from manatus import SourceResource

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
logger.debug(f'Loaded {__name__} map')


def ssdn_qdc_map(rec):
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

    # genre
    try:
        sr.genre = [{'name': genre}
                    for genre in rec.medium if genre]
    except TypeError:
        logger.info(f"No genre - {rec.harvest_id}")

    # identifier
    for identifier in rec.identifier:
        if identifier.startswith('http'):
            sr.identifier = identifier

    # language
    sr.language = rec.language

    # place
    if rec.place:
        sr.spatial = [{'name': place} for place in rec.place]
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

    # subject
    if rec.subject:
        sr.subject = [{'name': subject} for subject in rec.subject]

    # title
    sr.title = rec.title

    # type
    sr.type = rec.type

    # alternative title
    sr.alternative = rec.alternative

    # abstract
    sr.abstract = rec.abstract

    # extent
    sr.extent = rec.extent

    # collection
    if rec.is_part_of:
        sr.collection = [{'host': collection} for collection in rec.is_part_of]

    # thumbnail
    prefix = f'http://{rec.harvest_id.split(":")[1]}'
    collection_list = sr.identifier.split('/')[-4:]
    cdm_tn_path = f'/utils/getthumbnail/collection/{collection_list[1]}/id/{collection_list[3]}'
    tn = prefix + cdm_tn_path

    yield sr, tn
