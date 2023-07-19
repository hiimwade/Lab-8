"""
Description:
 Generates a CSV reports containing all married couples in
 the Social Network database.

Usage:
 python marriage_report.py
"""
import os
import sqlite3
from create_relationships import db_path, script_dir

def main():
    # Query DB for list of married couples
    married_couples = get_married_couples()

    # Save all married couples to CSV file
    csv_path = os.path.join(script_dir, 'married_couples.csv')
    save_married_couples_csv(married_couples, csv_path)

def get_married_couples():
    """Queries the Social Network database for all married couples.

    Returns:
        list: (name1, name2, start_date) of married couples 
    """
    # TODO: Function body
    con = sqlite3.connect('social_network.db')
    cur = con.cursor()
    married_couple_query= """
        SELECT person1.name, person2.name, start_date, type FROM relationships
        JOIN people person1 ON person1_id = person1.id
        JOIN people person2 ON person2_id = person2.id;
        WHERE r.type = 'spouse'
    """
    cur.execute(married_couple_query)
    married_couple = cur.fetchall()
    con.close
    for person1, person2, start_date, type in married_couple:
        print(f'{person1} has been a {type} of {person2} since {start_date}.')    
    con = sqlite3.connect(db_path)
    return

def save_married_couples_csv(married_couples, csv_path):
    """Saves list of married couples to a CSV file, including both people's 
    names and their wedding anniversary date  

    Args:
        married_couples (list): (name1, name2, start_date) of married couples
        csv_path (str): Path of CSV file
    """
    # TODO: Function body
    df = pd.Dataframe (married_couples, columns=['Person1', 'Person 2', 'Start Date'])
    df.to_cs(csv_path, index=False)
    print(f'Couples report saved to {csv_path}')
    # Hint: We did this in Lab 7.
    return

if __name__ == '__main__':
   main()