from flask import Flask, request, render_template, redirect, url_for
import psycopg2

app = Flask(__name__)

# Database connection details
DB_HOST = "localhost"
DB_NAME = "bookings"
DB_USER = "postgres"
DB_PASSWORD = "deepanmpcbaby"

# Route for home
@app.route("/")
def home():
    return render_template("index.html")

# Route to insert sample data
@app.route("/insert-sample-data")
def insert_sample_data():
    # Sample data to insert
    name = "John Doe"
    uid = 12345
    bdate = "2024-12-12"
    btime = "10:00"

    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cur = conn.cursor()

        # Insert sample data into the table
        cur.execute(
            "INSERT INTO bookings (name, uid, bdate, btime) VALUES (%s, %s, %s, %s)",
            (name, uid, bdate, btime)
        )

        # Commit the transaction
        conn.commit()

        # Verify insertion
        cur.execute("SELECT * FROM bookings WHERE name = %s AND uid = %s", (name, uid))
        inserted_data = cur.fetchone()
        if inserted_data:
            print(f"Sample data inserted successfully: {inserted_data}")
        else:
            print("Sample data insertion failed.")

        # Close the cursor and connection
        cur.close()
        conn.close()

        return "Sample data inserted successfully!"

    except Exception as e:
        print(f"An error occurred: {e}")
        return f"An error occurred: {e}"

if __name__ == "__main__":
    app.run(debug=True)