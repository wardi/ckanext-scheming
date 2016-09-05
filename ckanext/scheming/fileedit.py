from ckanext.scheming import loader

def validate_schema_from_file_edit(f, contents):
    try:
        loader.loads(contents, f['path'])
    except Exception, e:
        return unicode(e)

