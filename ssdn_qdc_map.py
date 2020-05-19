from citrus import SourceResource


def ssdn_qdc_map(rec):
    sr = SourceResource()
    if rec.contributor:
        sr.contributor = [{'name': contributor} for contributor in
                          rec.contributor]
    if rec.creator:
        sr.creator = [{'name': creator} for creator in
                      rec.creator]
    try:
        sr.date = {'begin': rec.date[0],
                   'end': rec.date[0],
                   'displayDate': rec.date[0]}
    except TypeError:
        pass
    sr.description = rec.description
    try:
        sr.genre = [{'name': genre}
                    for genre in rec.medium if genre]
    except TypeError:
        pass
    for identifier in rec.identifier:
        if identifier.startswith('http'):
            sr.identifier = identifier
    sr.language = rec.language
    if rec.place:
        sr.spatial = [{'name': place} for place in rec.place]
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
    if rec.subject:
        sr.subject = [{'name': subject} for subject in rec.subject]
    sr.title = rec.title
    sr.type = rec.type
    sr.alternative = rec.alternative
    sr.abstract = rec.abstract
    sr.extent = rec.extent
    if rec.is_part_of:
        sr.collection = [{'host': collection} for collection in rec.is_part_of]

    # thumbnail
    prefix = f'http://{rec.harvest_id.split(":")[1]}'
    collection_list = sr.identifier.split('/')[-4:]
    cdm_tn_path = f'/utils/getthumbnail/collection/{collection_list[1]}/id/{collection_list[3]}'
    tn = prefix + cdm_tn_path

    yield sr, tn
