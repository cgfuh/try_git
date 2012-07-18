dic = {
        'director': {
            'text': 'Director',
            'required': True
        },
        'production_company': {
            'text': 'Production Company',
            'required': True
        },
        'agency': {
            'text': 'Agency',
            'required': True
        }
    }

print dic

for fields, data in dic.items():
    print "field: ", fields
    print "data: ", data
    print type(data)
