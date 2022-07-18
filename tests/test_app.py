import unittest
import os
from urllib import request, response
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Ivanna's Portfolio</title>" in html

        #Add more tests relating to the home page
        assert '<img src="static/img/me.jpeg" alt="Image"/>' in html
        assert '<a class="nav-link smooth-scroll" href="/">Home</a>' in html
        assert '<a class="nav-link smooth-scroll" href="/#portfolio">Portfolio</a>' in html
        assert '<a class="nav-link smooth-scroll" href="/hobbies">Hobbies</a>' in html
        assert '<div class="h4 text-center mb-4 title">Work Experience</div>' in html
        assert '<div class="h4 text-center mb-4 title">Education</div>' in html

    def test_timeline_api(self):
        #GET the timeline_post page, test the initial length
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        #Add more tests relating to /api/timeline_post GET and POST APIs

        #POST some timeline posts, test the posting values
        post = self.client.post("/api/timeline_post", data={"name":"Placid", "email":"cidakat@outlook.com", "content":"Testing POST api in SQLite with Placid"})
        assert post.status_code == 200
        assert post.is_json
        json = post.get_json()
        assert json["name"] == "Placid"

        post = self.client.post("/api/timeline_post", data={"name":"Yulia", "email":"yuliaz@gmail.com", "content":"Testing POST api in SQLite with Yulia"})
        assert post.status_code == 200
        assert post.is_json
        json = post.get_json()
        assert json["email"] == "yuliaz@gmail.com"

        post = self.client.post("/api/timeline_post", data={"name":"Dannie", "email":"iamdannie@yahoo.ca", "content":"Testing POST api in SQLite with Dannie"})
        assert post.status_code == 200
        assert post.is_json
        json = post.get_json()
        assert json["content"] == "Testing POST api in SQLite with Dannie"

        #GET the timeline_post page, test the length after post
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert json["timeline_posts"][1]["id"] == 2
        assert json["timeline_posts"][2]["id"] == 1
        assert len(json["timeline_posts"]) == 3

    def test_timeline(self):
        #Add tests relating to the timeline page
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)

        assert '<form id="post-form">' in html
        assert '<button class="mt-3" type="submit">Submit</button>' in html
        '''
        assert '<h5 class="card-title"> Placid </h5>' in html
        assert '<p class="card-text">Testing POST api in SQLite with Dannie</p>' in html
        '''

        