from citrus import SourceResource, SourceResourceRequiredElementException
from assets import tgn_cache


def fsu_mods_map(rec):
    sr = SourceResource()
    sr.alternative = rec.alternative
    try:
        sr.collection = {'_:id': rec.collection.url, 
                        'host': rec.collection.location,
                        'name': rec.collection.title}
    except AttributeError:
        pass
    sr.contributor = rec.contributor
    sr.creator = rec.creator
    sr.date = rec.date
    sr.description = rec.description
    sr.extent = rec.extent
    sr.genre = rec.format
    try:
        sr.identifier = rec.identifier
    except IndexError:
        pass
    sr.language = rec.language
    sr.place = rec.place
    sr.publisher = rec.publisher
    try:
        if rec.rights.startswith('http:'):
            sr.rights = [{'@id': rec.rights}]
        else:
            sr.rights = [{'text': rec.rights}]
    except SourceResourceRequiredElementException:
        pass
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
    sr.title = [rec.title]
    sr.type = rec.type
    tn = f'http://fsu.digital.flvc.org/islandora/object/{rec.pid}/datastream/TN/view'
    return sr, tn
