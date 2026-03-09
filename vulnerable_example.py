"""
Example vulnerable application for testing the AVR prototype
This file contains intentional security vulnerabilities for demonstration purposes
DO NOT use this code in production!
"""

import os
import sys


def command_injection_example():
    """
    Vulnerable to command injection
    """
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
        # VULNERABLE: Direct use of user input in os.system
        os.system(f"echo {user_input}")


def sql_injection_example():
    """
    Vulnerable to SQL injection
    """
    import sqlite3
    
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER, username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users VALUES (1, 'admin', 'secret123')")
    
    username = input("Enter username: ") if sys.stdin.isatty() else "admin"
    
    # VULNERABLE: SQL injection via f-string
    query = f"SELECT * FROM users WHERE username='{username}'"
    cursor.execute(query)
    
    results = cursor.fetchall()
    print(f"Found {len(results)} users")


def path_traversal_example():
    """
    Vulnerable to path traversal
    """
    base_dir = "/tmp/uploads"
    filename = input("Enter filename: ") if sys.stdin.isatty() else "test.txt"
    
    # VULNERABLE: No path sanitization
    filepath = os.path.join(base_dir, filename)
    
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        print(f"File content: {content[:100]}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("Vulnerable Application - For Testing Only")
    print("=" * 50)
    
    # Run command injection example
    command_injection_example()
