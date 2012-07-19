
CONTEXT = {
    'sections': {
        'A. LIVE ACTION': {
            'total_categories': '3',
            'total_entries': '4',
            'categories': {
                'best direction': {
                    'total_entries': '2',
                    'entries': {
                        'id_1': {
                            'title': 'transformers',
                            'director': 'jeff lowe',
                            'agency': 'kamaamram',
                            'file': 'transformers_1.mov',
                            'size': '45mb',
                            'status': 'finalizada',
                        },
                        'id_2': {
                            'title': 'Naturaleza',
                            'director': 'Jeff Lowe',
                            'agency': 'kamaamram',
                            'file': '01.mov',
                            'size': '30MB',
                            'status': 'completa',
                        }
                    }
                }
            }
        },
        'C. SOUND': {
            'total_categories': '2',
            'total_entries': '2',
            'categories': {
                'best direction': {
                    'total_entries': '2',
                    'entries': {
                        'id_1': {
                            'title': 'ice age',
                            'director': 'jeff lowe',
                            'agency': 'kamaamram',
                            'file': 'ice.mov',
                            'size': '50mb',
                            'status': 'completa',
                        },
                    }
                }
            }
        }
    }
}

print CONTEXT['sections']

for sec_name, sec_detail in CONTEXT['sections'].items():
    print sec_name
    print sec_detail['total_categories']
    print sec_detail['total_entries']

    for cat_name, cat_detail in sec_detail['categories'].items():
        print cat_name
        print cat_detail['total_entries']

        for e_name, e_detail in cat_detail['entries'].items():
            print e_name
            print e_detail
