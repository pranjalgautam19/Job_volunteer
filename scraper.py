import psycopg2
import datetime

# Database Connection Parameters from your Supabase Connection String
DB_HOST = "db.rvibgvtogqjobjstpmty.supabase.co"
DB_PORT = "5432"
DB_NAME = "postgres"
DB_USER = "postgres.rvibgvtogqjobjstpmty"
DB_PASSWORD = "jobvoluntary195#%z" # <-- Type your real database password inside these quotes

def insert_local_jobs():
    print("Generating job database records locally...")
    
    # 1. High-quality mock job listings to populate your platform
    jobs_data = [
        {
            "title": "Remote Python Developer",
            "company": "TechSol Labs",
            "location": "Remote (Asia)",
            "salary": "₹12,00,000 - ₹18,00,000",
            "url": "https://example.com"
        },
        {
            "title": "Junior Data Engineer (SQL & Python)",
            "company": "DataMetrics Inc",
            "location": "Bangalore / Hybrid",
            "salary": "₹8,00,000 - ₹11,00,000",
            "url": "https://example.com"
        },
        {
            "title": "AI Prompt Engineer & Backend Specialist",
            "company": "NeuralFlow AI",
            "location": "Remote (Global)",
            "salary": "$60,000 - $80,000",
            "url": "https://example.com"
        },
        {
            "title": "Senior Django Web Framework Engineer",
            "company": "SaaSFactory",
            "location": "Mumbai / Remote",
            "salary": "₹20,00,000 - ₹26,00,000",
            "url": "https://example.com"
        }
    ]
    
    try:
        print("Connecting to your Supabase Server in Mumbai...")
        # 2. Connect directly to your Supabase SQL Database
        conn = psycopg2.connect(
            host=DB_HOST, 
            database=DB_NAME, 
            user=DB_USER, 
            password=DB_PASSWORD, 
            port=DB_PORT
        )
        cursor = conn.cursor()
        
        # 3. Safely insert each record into your database
        inserted_count = 0
        for job in jobs_data:
            try:
                cursor.execute(
                    """
                    INSERT INTO niche_jobs (title, company, location, salary_range, apply_link)
                    VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT (apply_link) DO NOTHING;
                    """,
                    (
                        job["title"], 
                        job["company"], 
                        job["location"], 
                        job["salary"], 
                        job["url"]
                    )
                )
                inserted_count += 1
            except Exception as row_error:
                print(f"Skipping individual row error: {row_error}")
                continue
                
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Database updated successfully! Inserted {inserted_count} jobs.")
        
    except Exception as e:
        print(f"Database connection error occurred: {e}")
        print("Please double check that your DB_PASSWORD is correct and you are connected to the internet.")

if __name__ == "__main__":
    insert_local_jobs()
