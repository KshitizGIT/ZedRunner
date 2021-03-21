from mysql.connector import connect, Error
from config import Database


class ZedRunnerStore:
    def __get_connection(self):
        connection = connect(
                host = Database.get("host"),
                user= Database.get('user'),
                database = Database.get('database'),
                password =Database.get('password')
                )
        return connection

    def store_horses(self, horse_datas):
        insert_horses_query = """
        INSERT INTO horses(bloodline, breed_type , breeding_counter , career_first ,
                        career_second , career_third , class , genotype, hashinfo_color ,
                        hashinfo_hexcode , hashinfo_name , horse_id , horse_type , img_url,
                        is_approved_for_racing, is_in_stud, is_on_racing_contract , last_stud_duration,
                        last_stud_timestamp , mating_price , next_breeding_date , number_of_races , 
                        owner , parents_father  , parents_mother  , rating  , super_coat  ,
                        tx , tx_date ,win_rate  )
        VALUES(%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        with self.__get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.executemany(insert_horses_query, horse_datas)
                connection.commit()
