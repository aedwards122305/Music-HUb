from Flask import FLask, render_template, request, jsonify, redirect
import sqlite3

app = Flask(__name__)

# Initializes the Sqlite database
def init_db():
    conn = sqlite3.connect(database.db)
    conn.execute("""Create TABLE IF NOT EXITSTs projects
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    project_name TEXT NOT NULL);""")
    conn.close()


# Route to insert a new name and project
@app.route('add', methods=['POST'])
def add_project():
    name = request.form['name']
    conn =sqlite3.connect('databse.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO projects (name, projects_name) VALUES (?, ?)",(name, project_name))
    conn.commit()
    conn.close()
    return redirect('/')


# Route to retrieve all name and projects
@app.route(
    /projects', methods=['GET']
def get_projects():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM projects")
    projects = cur.fetchall()
    conn.close()
    return jsonify(projects)

#Route to update a project
@app.route('/update', methods=['post'])
def update_project():
    projects_id = request.form['id']
    name = request.form['name']
    project_name = request.form['project']
    conn. = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("UPDATE projects SET name?, projects_name =? WHERE id=?", (name, project_name, project_id))
    conn.commit()
    conn.close()
    return redirect("/")


# Route to delete a project
@app.route('/delete', methods=['POST'])
def delect_project():
    project_id = request.form['id']
    conn.sqlit3.connect('database.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM projects WHERE id?", (project_id,))
    conn.commit()
    conn.close()

# Render main page
    @app.route('/')
    def index()
        return render_template('index.html')

    if __name__ == '__main__':
        init_db()   #Initializes the database and table
        app.run(debug=True)