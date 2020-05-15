from citrus import SourceResource, SourceResourceRequiredElementException


def fiu_dc_map(rec):
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
    sr.format = rec.format
    for identifier in rec.identifier:
        if 'dpanther.fiu.edu' in identifier:
            sr.identifier = identifier
    try:
        sr.language = [{'name': lang} for lang in rec.language]
    except TypeError:
        pass
    sr.spatial = rec.place
    sr.publisher = rec.publisher
    #print(rec.rights)
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
    
    if rec.thumbnail:
        tn = rec.thumbnail
    
    return sr, tn
