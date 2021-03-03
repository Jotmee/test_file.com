
# Create DB

$ python

>> from app import db

>> db.create_all()

>> exit()

# Run Server

python app.py 

(http://localhost:5000)


## API points test on postman

* GET (all)   

        - /Song
            e.g http://localhost:5000/Song

        - /Podcast

        - /Audiobook

* GET (specific id and pass json data according to fields available)

        - /Song/id
            e.g http://localhost:5000/Song/1
                    {
                    "duration": 55,
                    "name_of_song": "Heal the World",
                    "uploaded_time": "2021-03-02 12:16:53"
                    }

        - /Audiobook/id

        - /Podcast/id

* POST  (pass json data according to fields available)

        - /Song
            e.g {
                    "duration": 44,
                    "name_of_song": "Heal the World",
                    "uploaded_time": "2021-03-02 12:16:53"
                }

        - /Podcast

        - /Audiobook

* PUT   (specify id)

        - /Song/id
            e.g http://localhost:5000/Song/1

        - /Podcast/id

        - /Audiobook/id

* DELETE (specify id)

         - /Song/id
                e.g http://localhost:5000/Song/1

         - /Podcast/id

         - /Audiobook/id