import logging

from manatus import SourceResource, SourceResourceRequiredElementException

from assets import tgn_cache

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
logger.debug(f'Loaded {__name__} map')


def fsu_mods_map(rec):
    sr = SourceResource()

    try:
        sr.alternative = rec.alternative
    except AttributeError:
        return None

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
    sr.date = rec.date
    sr.description = rec.description
    sr.extent = rec.extent
    sr.genre = rec.format

    # identifier
    try:
        sr.identifier = rec.identifier
    except IndexError:
        logger.error(f"No identifier - {rec.harvest_id}")
        return None

    # language
    try:
        sr.language = rec.language
    except AttributeError:
        return None

    # place
    try:
        sr.spatial = rec.place
    except (AttributeError, TypeError):
        return None

    sr.publisher = rec.publisher

    # rights
    try:
        if rec.rights.startswith('http:'):
            sr.rights = [{'@id': rec.rights}]
        else:
            logger.warning(f"No rights URI - {rec.harvest_id}")
            sr.rights = [{'text': rec.rights}]
    except (AttributeError, SourceResourceRequiredElementException):
        logger.error(f"No rights - {rec.harvest_id}")
        return None

    # place
    try:
        attribution = "This record contains information from Thesaurus of Geographic Names (TGN) which is made available under the ODC Attribution License."
        geo_data_list = [tgn_cache(geo_code) for geo_code in rec.geographic_code]
        sr.spatial = [{'lat': lat,
                       'long': long,
                       'name': label,
                       '_:attribution': attribution}
                      for _, lat, long, label in geo_data_list]
    except TypeError:
        pass

    sr.subject = rec.subject

    # title
    try:
        sr.title = [rec.title]
    except (AttributeError, SourceResourceRequiredElementException):
        logger.error(f"No title - {rec.harvest_id}")
        return None

    sr.type = rec.type

    # thumbnail
    tn = f'https://diginole.lib.fsu.edu/islandora/object/{rec.pid}/datastream/TN/view'

    yield sr, tn
