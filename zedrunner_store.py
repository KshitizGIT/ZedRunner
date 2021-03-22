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

    def horse_exists(self, horse_info):
        query_horse = "SELECT 1 from horses where horse_id = %s"%(horse_info['horse_id'])

        with self.__get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query_horse)
                data = cursor.fetchall()
                if data:
                    print('Horse exists')
                    return True
                else:
                    return False

    def store_horses(self, horse_datas):
        list_of_ids = [d[11] for d in horse_datas]
        format_strings = ','.join(['%s'] * len(list_of_ids))
        delete_horses_query = """
        DELETE FROM horses where horse_id in (%s)
        """%format_strings
        insert_horses_query = """
        INSERT INTO horses(bloodline, breed_type , breeding_counter , career_first ,
                        career_second , career_third , class , genotype, hashinfo_color ,
                        hashinfo_hexcode , hashinfo_name , horse_id , horse_type , img_url,
                        is_approved_for_racing, is_in_stud, is_on_racing_contract , last_stud_duration,
                        last_stud_timestamp , mating_price , next_breeding_date , number_of_races , 
                        owner , parents_father  , parents_mother  , rating  , super_coat  ,
                        tx , tx_date ,win_rate  )
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        with self.__get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(delete_horses_query,tuple(list_of_ids))
                cursor.executemany(insert_horses_query, horse_datas)
                connection.commit()

    def store_races(self, races_data):
        list_of_ids = [d[10] for d in races_data]

        format_strings = ','.join(['%s'] * len(list_of_ids))
        delete_races_query = "DELETE From races where race_id in (%s)"%format_strings

        insert_races_query = """INSERT INTO races(city, class, country_code, fee,
                          length, name, prizepool_first,
                          prizepool_second, prizepool_third,
                          prizepool_total , race_id, start_time,
                          status, weather)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        with self.__get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(delete_races_query, tuple(list_of_ids) )
                cursor.executemany(insert_races_query, races_data)
                connection.commit()

    def store_races_result(self, races_data):
        list_of_race_ids = set([d[0] for d in races_data])
        import pdb
        pdb.set_trace()
        format_strings = ','.join(['%s'] * len(list_of_race_ids))
        delete_races_query = "DELETE From races_results where race_id in (%s)"%format_strings

        insert_races_query = """ 
        INSERT INTO races_results( race_id, horse_id ,
                                   finish_time , final_position ,
                                   name , gate , owner_address ,
                                   bloodline , gender , breed_type ,
                                   gen , races , coat , win_rate ,
                                   career , hex_color , img_url ,
                                   class , stable_name )
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        with self.__get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(delete_races_query, tuple(list_of_race_ids))
                cursor.executemany(insert_races_query, races_data)
                connection.commit()
    def race_exists(self, race_info):
        query_race = "SELECT 1 from races where race_id = '%s'"%(race_info['node']['race_id'])
        print(query_race)

        with self.__get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query_race)
                data = cursor.fetchall()
                if data:
                    print('Race exists')
                    return True
                else:
                    return False

