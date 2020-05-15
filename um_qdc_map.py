import requests
from bs4 import BeautifulSoup

from citrus import SourceResource, SourceResourceRequiredElementException


IANA_type_list = []

IANA_XML = requests.get('http://www.iana.org/assignments/media-types/media-types.xml')
IANA_parsed = BeautifulSoup(IANA_XML.text, "lxml")
for type in IANA_parsed.find_all('file'):
    IANA_type_list.append(type.text)


def um_qdc_map(rec):
    sr = SourceResource()
    sr.contributor = rec.contributor
    sr.creator = rec.creator
    try:
        sr.date = {'begin': rec.date[0], 
                   'end': rec.date[0], 
                   'displayDate': rec.date[0]}
    except TypeError:
        pass
    sr.description = rec.description
    sr.genre = [{'name': genre}                 
                for genre in rec.format
                if genre.lower() not in IANA_type_list]
    for identifier in rec.identifier:
        if 'merrick.library.miami.edu' in identifier:
            sr.identifier = identifier
    sr.language = rec.language
    sr.spatial = rec.place
    sr.publisher = rec.publisher
    if len(rec.rights) > 1:
        for r in rec.rights:
            if r.startswith('http'):
                sr.rights = [{'@id': r}]
    else:
        if rec.rights[0].startswith('http'):
                sr.rights = [{'@id': rec.rights[0]}]
        else:        
            sr.rights = [{'text': rec.rights[0]}]
    sr.subject = rec.subject
    sr.title = rec.title
    sr.type = rec.type
    sr.alternative = rec.alternative
    sr.abstract = rec.abstract
    sr.collection = {'host': rec.is_part_of[0], 'name': rec.is_part_of[1]}
    sr.extent = rec.extent
    
    # thumbnail
    prefix = 'http://merrick.library.miami.edu'
    collection_list = identifier.split('/')[-4:]
    cdm_tn_path = f'/utils/getthumbnail/collection/{collection_list[1]}/id/{collection_list[3]}'
    tn = prefix + cdm_tn_path
    
    return sr, tn
    