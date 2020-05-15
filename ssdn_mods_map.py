from citrus import SourceResource, SourceResourceRequiredElementException


def ssdn_mods_map(rec):
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
    sr.subject = rec.subject
    sr.title = [rec.title]
    sr.type = rec.type
    tn = f'https://{rec.harvest_id.split(":")[1]}/islandora/object/{rec.pid}/datastream/TN/view'
    
    return sr, tn
