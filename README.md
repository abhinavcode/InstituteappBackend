# InstituteappBackend

## API end points

### check registered
``` http://iitbhuapp.tk/checkreg ```

#### Expected POST req

``` {"email":"asdjabda@akf.com",
	"password": "retrieved from login"}```

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
``` {"status": 2,
    "password": "ljdkzenidt"}```

- Response if new reg
``` {"status": 1,
    "password": "xevnsemtag"}```

_________

### Feed stories and clubs
```http://iitbhuapp.tk/feedandclubs```

#### Expected POST req

``` {"email":"abscvdsfk@itbhu.ac.in",
	"password": "eiptxcqupu"}```

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
            "clubimage": "/media/download.png",
            "council": "Cultural Council",
            "councilimage": "/media/abc.jpeg",
            "title": "asd",
            "description": "ad",
            "datetime": "2019-05-31T10:53:10Z",
            "location": "ds",
            "viewedcount": 1,
            "interestedcount": 1,
            "interested": 1,
            "notifid": 1
        },
        {
            "club": "Western Music Club",
            "council": "Cultural Council",
            "councilimage": "/media/abc.jpeg",
            "title": "test1",
            "description": "test",
            "image": "/media/back.jpg",
            "datetime": "2019-05-31T17:55:29Z",
            "location": "testloc",
            "viewedcount": 1,
            "interestedcount": 0,
            "interested": 0,
            "notifid": 2
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
``` {    "status": 2,
	"intrested_names": ["Martin"]
	}```

- Response if already intersted
``` {   "status": 2,
	"intrested_names": ["Bhoomik Bhamawat", "Martin", "Monu Kumar"]
	}```


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

### Contributors
[![](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/images/0)](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/links/0)[![](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/images/1)](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/links/1)[![](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/images/2)](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/links/2)[![](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/images/3)](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/links/3)[![](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/images/4)](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/links/4)[![](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/images/5)](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/links/5)[![](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/images/6)](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/links/6)[![](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/images/7)](https://sourcerer.io/fame/abhinavcode/abhinavcode/InstituteappBackend/links/7)
