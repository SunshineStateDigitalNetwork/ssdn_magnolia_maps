import logging

from manatus import SourceResource, SourceResourceRequiredElementException

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
logger.debug(f'Loaded {__name__} map')


def ssdn_mods_map(rec):
    sr = SourceResource()

    # alternative title
    sr.alternative = rec.alternative

    # Archival collection info
    if rec.collection:
        coll_info = dict()
        if rec.collection.url:
            coll_info['_:id'] = rec.collection.url
        if rec.collection.location:
            coll_info['host'] = rec.collection.location
        if rec.collection.title:
            coll_info['name'] = rec.collection.title
        sr.collection = coll_info

    sr.contributor = rec.contributor
    sr.creator = rec.creator

    # date
    try:
        sr.date = rec.date
    except TypeError:
        logger.info(f"No date - {rec.harvest_id}")
        pass
    
    sr.description = rec.description
    sr.extent = rec.extent
    sr.genre = rec.format

    # identifier
    try:
        sr.identifier = rec.identifier
    except IndexError:
        logger.error(f"No identifier - {rec.harvest_id}")
        return None

    sr.language = rec.language
    sr.spatial = rec.place
    sr.publisher = rec.publisher

    # rights
    try:
        if rec.rights.startswith('http:'):
            sr.rights = [{'@id': rec.rights}]
        else:
            logger.warning(f"No rights URI - {rec.harvest_id}")
            sr.rights = [{'text': rec.rights}]
    except (SourceResourceRequiredElementException, AttributeError):
        logger.error(f"No rights - {rec.harvest_id}")
        return None

    sr.subject = rec.subject
    sr.title = [rec.title]
    sr.type = rec.type

    # thumbnail
    tn = f'https://{rec.harvest_id.split(":")[1]}/islandora/object/{rec.pid}/datastream/TN/view'

    yield sr, tn
