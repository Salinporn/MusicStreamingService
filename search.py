import os.path
from whoosh import index, analysis
from whoosh.fields import Schema, STORED, ID, KEYWORD, TEXT
from whoosh.qparser import MultifieldParser

from server import music_manager

def index_data():
    schema = Schema(
        title=TEXT(stored=True, analyzer=analysis.NgramWordAnalyzer(minsize=2)),
        artists=KEYWORD(stored=True, analyzer=analysis.NgramWordAnalyzer(minsize=2)),
        album=TEXT(stored=True),
        genres=KEYWORD,
        uuid=ID(stored=True)
    )

    if not os.path.exists("index"):
        os.mkdir("index")
        
    ix = index.create_in("index", schema)

    writer = ix.writer()

    for song in music_manager.get_songs():
        song_data = song.get_json()
        
        writer.add_document(
            title=song_data["title"],
            artists=" ".join(song_data["artists"]),
            album=song_data["album"],
            genres=song_data["genres"],
            uuid=song_data["uuid"]
        )
        
    writer.commit()

def search(query_string):
    ix = index.open_dir("index")
    with ix.searcher() as searcher:
        query_parser = MultifieldParser(fieldnames=["title", "artists", "album"], schema=ix.schema)
        query = query_parser.parse(query_string)
        results = searcher.search(query)
        
        return [dict(hit) for hit in results]
