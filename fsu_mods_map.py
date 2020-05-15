import re

from citrus import SourceResource, SourceResourceRequiredElementException
from assets import tgn_cache

first_baptist = re.compile('^FSU_FBCTLH')
leon_high = re.compile('^FSU_LeonHigh')
godby_high = re.compile('^FSU_Godby')
havana_hhs = re.compile('^FSU_HHHS')


def fsu_mods_map(rec):
    sr = SourceResource()
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
    sr.date = rec.date
    sr.description = rec.description
    sr.extent = rec.extent
    sr.genre = rec.format
    try:
        sr.identifier = rec.identifier
    except IndexError:
        pass
    sr.language = rec.language
    sr.spatial = rec.place
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
    tn = f'https://fsu.digital.flvc.org/islandora/object/{rec.pid}/datastream/TN/view'
    
    # check if not in default data_provider scope
    first_baptist_iid = first_baptist.search(rec.iid)
    leon_high_iid = leon_high.search(rec.iid)
    godby_high_iid = godby_high.search(rec.iid)
    havana_hhs_iid = havana_hhs.search(rec.iid)
    if first_baptist_iid:
        data_provider = 'First Baptist Church of Tallahassee'
        intermediate_provider = 'Florida State University Libraries'
    elif leon_high_iid:
        data_provider = 'Leon High School, Tallahassee, Florida'
        intermediate_provider = 'Florida State University Libraries'   
    elif godby_high_iid:
        data_provider = 'Godby High School, Tallahassee, Florida'
        intermediate_provider = 'Florida State University Libraries'
    elif havana_hhs_iid:
        data_provider = 'Havana History & Heritage Society, Havana, Florida'
        intermediate_provider = 'Florida State University Libraries'
    else:
        data_provider = 'Florida State University Libraries'
        intermediate_provider = None
    
    return sr, tn, data_provider, intermediate_provider
