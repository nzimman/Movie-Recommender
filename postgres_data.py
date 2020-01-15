from sqlalchemy import create_engine
import pandas as pd
import re



#Query all movies

def connect_to_db():
    #Connect to postgres
    USERNAME = '...' #<-- add credentials
    PASSWORD = '...' #<- add credentials
    HOST = 'localhost' #127.0.0.1 --> IP address loop back
    PORT = '5432'
    DBNAME = '...' #<- add name of the database in postgresd

    conn_string = f'postgres://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}'
    db = create_engine(conn_string)
    return db

def get_movie_list(conn):
  query = """select r.movieid, m.title, count(r.rating) as myc, avg(r.rating) as mya
            from ratings r, movies m
            where r.movieid = m.movieid
            group by r.movieid, m.title
            order by myc desc, mya desc
            limit 100;
            """
  result = conn.execute(query)

  df=pd.DataFrame(result,columns=result.keys())
  df2=df['title'].apply(clean_title)
  movie_list = df2.values.tolist()
  return movie_list


def clean_title(x):
    result = re.sub("[\(\[].*?[\)\]]", "", x).strip()
    return result



def create_movie_matrix_clean(db):
    query = """select r.movieid, r.userid, m.title,  r.rating
          from ratings r, movies m
          where r.movieid = m.movieid
          """
    result = db.execute(query)

    df = pd.DataFrame(result,columns=result.keys())
    df['clean_title'] = df['title'].apply(clean_title)
    return df


def create_movie_matrix(conn):
  query = """select r.movieid, r.userid, m.title,  r.rating
        from ratings r, movies m
        where r.movieid = m.movieid
        """
  result = db.execute(query)

  df = pd.DataFrame(result,columns=result.keys())
  df['clean_title'] = df['title'].apply(clean_title)

  R = df[['userid','movieid','rating']]
  R.set_index(['movieid', 'userid'])['rating']
  R = R.pivot_table(values='rating',index='userid',columns='movieid')

  return R
