import requests

class DB_MOVIES:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor(buffered=True)

    def get_documents(self):
        self.cursor.execute("SELECT title, plot FROM wiki_movie_plots_deduped")
        return self.cursor.fetchall()
    
    def get_documentsRandom(self, amount):
        self.cursor.execute("SELECT title, plot FROM wiki_movie_plots_deduped ORDER BY rand() limit {:d}".format(amount))
        return self.cursor.fetchall()
    
    def get_topic(self, id):
        self.cursor.execute("SELECT topic_text, topic_name FROM movie_topics WHERE id = {:d}".format(id))
        return self.cursor.fetchall()