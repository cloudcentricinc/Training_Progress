albums = [("welcome to my nightmare", "alice cooper", 1975),
          ("bad company", "bad company", 1974),
          ("nightflight", "budgie", 1981),
          ("more mayhem", "emila may", 20111),
          ("ride of lightning", "metallica", 1984),
          ]

print(len(albums))

for name,artist,year in albums:
    print("album:{},artist:{},year:{}"
          .format(name, artist, year))
