from math import floor

albums = [{
            "discogs_id":13,
            "artist": 'Matt Damon',
            "album": 'Stars',
            "year": 1989,
            "decade": floor(1989/ 10) * 10,
            "country": "Turkey",
            "genres": "Turkish pop",
            "styles": "Turkish popular music",
            "label": "La Fontaine",
            "url": "www.google.com/p",
            "image": "www.google.com/988?par=id"
        },
       {
            "discogs_id":12,
            "artist": 'Matt Damon',
            "album": 'Planetary Citizen',
            "year": 1982,
            "decade": floor(1982/ 10) * 10,
            "country": "Azerbaijan",
            "genres": "Turkish pop",
            "styles": "Polka",
            "label": "Belle",
            "url": "www.google.com/pssa",
            "image": "www.google.com/988?par=idsdas"
        },
       {
            "discogs_id":15,
            "artist": 'Leopoldo Siqueira',
            "album": 'A viagem',
            "year": 1972,
            "decade": floor(1972 / 10) * 10,
            "country": "Brazil",
            "genres": "Brazilian song",
            "styles": "MPB",
            "label": "Belle",
            "url": "www.google.com/pssssa",
            "image": "www.google.com/988?par=idsdasaas"
        }
]

# keys = ['album', 'genres', 'label', 'country', 'decade', 'year']
#
# advanced_filter = {key:value for key, value in albums[0].items() if key in keys}
# advanced_filter['style'] = albums[0]['styles']
#
# complex_filter = {key:"" for key in albums[0].keys() if key in keys}
# complex_filter['decade'] = albums[1]['decade']
# complex_filter['year'] = albums[2]['year']
# complex_filter['style'] = ""

