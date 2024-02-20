from http.server import BaseHTTPRequestHandler
import json 
import socketserver
from db import get_database_connection

class HttpRequestHandler(BaseHTTPRequestHandler):

    #GET METHOD
    def do_GET(self):

        """
        This is the get method for the crud operation which gets all the notes from the database
        """
        #Connect to the database
        connection = get_database_connection()

        cursor = connection.cursor()

        #query to get all notes
        cursor.execute("SELECT * FROM notes")

        #turn rows into tuples
        notes = cursor.fetchall()

        #Close connection
        cursor.close()
        connection.close()

        #turn tuples into a list of dictionaries
        notes = [{'id': id, 'title': title, 'content': content} for (id, title, content) in notes]

        #Response
        self.send_response(200) #send 200 response code -> successfully got data
        self.send_header('Content-type', 'application/json') #turn data into json
        self.end_headers()
        self.wfile.write(json.dumps(notes).encode())


    #POST METHOD
    def do_POST(self):
        
        """
        This is the post method for the crud operation which creates a new note in the database
        """

        #Request
        length = int(self.headers.get('Content-length'))
        body = self.rfile.read(length)
        note = json.loads(body)

        #Connect to the database
        connection = get_database_connection()
        cursor = connection.cursor()

        #Query to insert a new note
        cursor.execute("INSERT INTO notes (title, content) VALUES (%s, %s)", (note['title'], note['content']))

        #Commit
        connection.commit()

        #Close connection
        cursor.close()
        connection.close()

        #Response 201 -> Creation of a resource 
        self.send_response(201)
        self.end_headers()
    
    #PUT METHOD
    def do_PUT(self):
        
        """
        This is the put method for the crud operation which updates a note from the database
        """

        #Request
        length = int(self.headers.get('Content-length'))
        body = self.rfile.read(length)
        note = json.loads(body)

        #Connect to the database
        connection = get_database_connection()
        cursor = connection.cursor()

        #Query to update a note
        cursor.execute("UPDATE notes SET title = %s, content = %s WHERE id = %s", (note['title'], note['content'], note['id']))

        #commit
        connection.commit()

        #Close connection
        cursor.close()
        connection.close()

        #Response 200 -> Success
        self.send_response(200)
        self.end_headers()

    #DELETE METHOD
    def do_DELETE(self):
        
        """
        This is the delete method for the crud operation which deletes a note from the database
        """

        #Request
        length = int(self.headers.get('Content-length'))
        body = self.rfile.read(length)
        note = json.loads(body)

        #Connect to the database
        connection = get_database_connection()
        cursor = connection.cursor()

        #Query to delete a note
        cursor.execute("DELETE FROM notes WHERE id = %s", (note['id'],))

        #Commit
        connection.commit()

        #Close connection
        cursor.close()
        connection.close()

        #Response 200 -> Success
        self.send_response(200)
        self.end_headers()

#Connect on port 8000
PORT = 8000
Handler = HttpRequestHandler

#Check if successfully connected
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Listening on port:", PORT)
    httpd.serve_forever()
