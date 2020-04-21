# InstituteappBackend

## API end points

### check registered
``` http://iitbhuapp.tk/checkreg ```

#### Expected POST req

```
{
	"email":"asdjabda@akf.com",
	"password": "retrieved from login"
}
```


#### Expected POST res

- Response if anything goes wrong
``` {"status": 0}```

- Response if registered
``` 
{
    "status": 1,
    "name": "Ayush Saxena",
    "roll": 18095016,
    "phone": "8440007759",
    "department": "BioMedical Engineering",
    "yearOfAdmission": 2018,
    "course": "B.Tech",
    "fatherName": "Kishan Saxena",
    "address": "243,London Complex,China Street,Jabalpur",
    "gender": "Male",
    "bloodGroup": "O+",
    "dob": "07/07/2000"
}
```

- Response if new reg
``` {"status": 2}```

_______

### Login/register
``` http://iitbhuapp.tk/login ```

#### Expected POST req

``` {"email":"asdjabda@akf.com"}```

#### Expected POST res

- Response if registered 
``` 
{
	"status": 2,
    	"password": "ljdkzenidt"
}
```

- Response if new reg
``` 
{
	"status": 1,
   	"password": "xevnsemtag"
}
```

_________

### Feed stories and clubs
```http://iitbhuapp.tk/feedandclubs```

#### Expected POST req

``` 
{
	"email":"abscvdsfk@itbhu.ac.in",
	"password": "eiptxcqupu"
}
```

#### Expected POST res

- Response if anything goes wrong
``` 
{
    "status": 0,
    "councils": [
        {
            "name": "Cultural Council",
            "image": "/media/abc.jpeg",
            "clubs": [
                {
                    "name": "Indian Music Club",
                    "image": "/media/download.png"
                },
                {
                    "name": "Western Music Club"
                },
                {
                    "name": "Dance Club"
                }
            ]
        },
        {
            "name": "Games and Sports Council",
            "image": "/media/3.jpeg",
            "clubs": [
                {
                    "name": "Cricket Club",
                    "image": "/media/posters.jpg"
                }
            ]
        }
    ]
}
```

- Response if everything is fine

```
{
    "status": 1,
    "councils": [
        {
            "name": "Cultural Council",
            "image": "/media/abc.jpeg",
            "clubs": [
                {
                    "name": "Indian Music Club",
                    "image": "/media/download.png"
                },
                {
                    "name": "Western Music Club"
                },
                {
                    "name": "Dance Club"
                }
            ]
        },
        {
            "name": "Games and Sports Council",
            "image": "/media/3.jpeg",
            "clubs": [
                {
                    "name": "Cricket Club",
                    "image": "/media/posters.jpg"
                }
            ]
        }
    ],
    "notif": [
        {
            "club": "Indian Music Club",
            "clubimage": "/media/IMC.jpg",
            "council": "Cultural Council",
            "councilimage": "/media/00_Cult.jpg",
            "title": "Indian Music Club, IIT BHU",
            "description": "The musical journey began with Cultural Council's Fresher's Orientation on 1st and 4th August. The club mesmerised the audience with a number of soulful and rocking performances. The club's musical prowess was staged in front of the fresher's through songs covering a number of genres like Qawwali, Semi-Classical and Rock.",
            "image": "/media/45235975_2329093817165660_5482301324122914816_o.jpg",
            "datetime": "2020-07-08T06:00:00Z",
            "location": "G11",
            "map_location": "G11",
            "viewedcount": 1,
            "interestedcount": 0,
            "interested_names": [],
            "interested": 0,
            "notifid": 13
        },
        {
            "club": "Robotics Club",
            "clubimage": "/media/ROBO.jpg",
            "council": "SNTC",
            "councilimage": "/media/00_SNTC.jpg",
            "title": "Selection for Aagman",
            "description": "RocketLaunch",
            "image": "/media/robotics_Thv5kj6.jpg",
            "datetime": "2020-04-30T18:00:00Z",
            "location": "LT3",
            "map_location": "SWATANTRATA_BHAVAN",
            "viewedcount": 1,
            "interestedcount": 3,
            "interested_names": [
                "Martin",
                "Monu Kumar",
                "Bhoomik Bhamawat"
            ],
            "interested": 1,
            "notifid": 23
        }
    ]
}
```
___________
### Interested
```http://iitbhuapp.tk/interested```

#### Expected POST req

``` 
{
	"email":"abdfgbdfg.min18@itbhu.ac.in",
        "notifid": 23
}
```

#### Expected POST res

- Response if anything goes wrong
``` {"status": 0}```

- Response if everything is fine
``` 
{    
	"status": 1,
	"intrested_names": ["Martin"]
}
```

- Response if already intersted
``` 
{  
	"status": 2,
	"intrested_names": ["Bhoomik Bhamawat", "Martin", "Monu Kumar"]
}
```

___________
### Complain
```http://iitbhuapp.tk/postcomplain```

#### Expected POST req

``` 
{
	"roll":213,
	"complain":"test complain",
	"anonymous":1 #0 if you dont want to be anonymous,
	"header":"complain header",
	"type":"hostel complain",
	"hostel":"sc dey"#optional field
}
```

#### Expected POST res

- Response if anything goes wrong
``` {"status": 0}```

- Response if everything is fine
``` {"status": 1}```

___________________
### important contacts
```http://iitbhuapp.tk/importantcontacts```

#### Expected POST req

Empty
``` 
{}
```
#### Expected POST res

- Response if anything goes wrong
``` {"status": 0}```

- Response if no error
``` 
{
    "status": 1,
    "data": [
        {
            "name": "Yogesh",
            "email": "sample@sample.com",
            "phone": "123",
            "role" : "student",
        },
        {
            "name": "xyz",
            "email": "xyz@xyz.com",
            "phone": "1",
            "role" : "head",
        }
    ]
}
```
___________________
### timetable 
```http://iitbhuapp.tk/timetable```

#### Expected POST req

``` 
{"email":"sample@sample.com","password":"asdadddd"}
```
#### Expected POST res

- Response if anything goes wrong
``` Error in request {"status": 0}```
``` Invalid credentials {"status": 2}```

- Response if no error
``` 
{
    "status": 1,"image":"/media/mechanical.png"
}
```
___________________
### notification 
```http://iitbhuapp.tk/notification```

#### Expected POST req

``` 
{
 {'email': 'ksnabielmartin.mec18@gmail.com', 
 'password': 'fmacjdorpn', 
 'club': 'DFZ', 'year': 2020, 
 'month': 5, 'day': 2, 
 'hour': 17, 'minutes': 30, 
 'header': 'TECHNEX2020', 
 'description': 'the event is postponed', 
 'image': 'base64encoded image string'
 }
```
#### Expected POST res

- Response if anything goes wrong
``` Error in request {"status":1 }```
``` Invalid credentials {"status": 3}```

- Response if no error
``` 
{
    "status": 1,
}
```
___________________

### Contributors
[![](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/images/0)](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/links/0)[![](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/images/1)](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/links/1)[![](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/images/2)](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/links/2)[![](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/images/3)](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/links/3)[![](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/images/4)](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/links/4)[![](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/images/5)](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/links/5)[![](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/images/6)](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/links/6)[![](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/images/7)](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/links/7)
