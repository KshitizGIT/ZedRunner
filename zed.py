import requests
from zedrunner_store import ZedRunnerStore

class ZedRun:

    def __init__(self):
        self.store = ZedRunnerStore()

    def clean_horses_data(self, horse_datas):
        return_datas = []
        for d in horse_datas:
            bloodline = d['bloodline']
            breed_type = d['breed_type']
            breeding_counter = d['breeding_counter']
            career_first = d['career']['first']
            career_second = d['career']['second']
            career_third  = d['career']['third']
            c=d['class']
            genotype = d['genotype']
            hashinfo_color = d['hash_info']['color']
            hashinfo_hexcode = d['hash_info']['hex_code']
            hashinfo_name=d['hash_info']['name']
            horse_id=d['horse_id']
            horse_type= d['horse_type']
            img_url=d['img_url']
            is_approved_for_racing= d['is_approved_for_racing']
            is_in_stud= d['is_in_stud']
            is_on_racing_contract=d['is_on_racing_contract']
            last_stud_duration= d['last_stud_duration']
            last_stud_timestamp= d['last_stud_timestamp']
            mating_price =d['mating_price']
            next_breeding_date= d['next_breeding_date']
            number_of_races= d['number_of_races']
            owner= d['owner']
            parents_father= d['parents']['father']
            parents_mother= d['parents']['mother']
            rating =d['rating']
            super_coat= d['super_coat']
            tx= d['tx']
            tx_date =d['tx_date']
            win_rate=d['win_rate']

            return_datas.append((bloodline , breed_type , breeding_counter ,
                career_first , career_second , career_third  , c, genotype ,
                hashinfo_color , hashinfo_hexcode , hashinfo_name, horse_id,
                horse_type, img_url, is_approved_for_racing, is_in_stud,
                is_on_racing_contract, last_stud_duration, last_stud_timestamp, mating_price ,
                next_breeding_date, number_of_races, owner, parents_father, parents_mother,
                rating , super_coat, tx, tx_date , win_rate
                ))

        return return_datas


    def fetch_horse_data(self):
        url = 'https://api.zed.run/api/v1/horses/roster?offset={0}&gen\[\]=1&gen\[\]=268&sort_by=created_by_desc&page=2'
        offset = 0
        while True:
            current_url = url.format(offset)
            response = requests.get(current_url)
            print(response.status_code)
            jsondata =response.json()
            count = len(jsondata)
            offset = offset + count
            print(jsondata)
            print(len(jsondata))
            horse_datas = self.clean_horses_data(jsondata)
            self.store.store_horses(horse_datas)
            if count == 10:
                break



if __name__ == '__main__':
    run = ZedRun()
    run.fetch_horse_data()
