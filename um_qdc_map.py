import logging

import requests
from bs4 import BeautifulSoup
from citrus import SourceResource

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
logger.debug(f'Loaded {__name__} map')

IANA_type_list = []

IANA_XML = requests.get('http://www.iana.org/assignments/media-types/media-types.xml')
IANA_parsed = BeautifulSoup(IANA_XML.text, "lxml")
for type in IANA_parsed.find_all('file'):
    IANA_type_list.append(type.text)


def um_qdc_map(rec):
    # handling for how UM marks records to skip
    if rec.requires:
        if 'noharvest' in rec.requires:
            logger.info(f"Marked `noharvest` {rec.harvest_id}")
            return None

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
                    for genre in rec.format
                    if genre.lower() not in IANA_type_list]
    except TypeError:
        logger.info(f"No genre - {rec.harvest_id}")

    # identifier
    for identifier in rec.identifier:
        if 'cdm17191.contentdm.oclc.org' in identifier:
            sr.identifier = identifier
    if not sr.identifier:
        logger.error(f"No identifier - {rec.harvest_id}")
        return None

    # language
    sr.language = rec.language

    # place
    if rec.place:
        sr.spatial = [{'name': place} for place in rec.place]
    sr.publisher = rec.publisher

    # rights
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

    # collection
    sr.collection = {'host': rec.is_part_of[0], 'name': rec.is_part_of[1]}

    # extent
    sr.extent = rec.extent

    # thumbnail
    prefix = 'http://cdm17191.contentdm.oclc.org'
    collection_list = identifier.split('/')[-4:]
    cdm_tn_path = f'/utils/getthumbnail/collection/{collection_list[1]}/id/{collection_list[3]}'
    tn = prefix + cdm_tn_path

    yield sr, tn
