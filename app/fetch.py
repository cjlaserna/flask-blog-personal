from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import os
import json
import sys
import json

token = os.getenv("DATOCMS_READONLY_TOKEN")

url = "https://graphql.datocms.com/"
auth = "Bearer " + str(token)
query = gql("""{
			aboutMe {
				greeting
				shortIntroduction
				about
				profilePicture {
					url
					alt
					title
				}
			}
			experiences: allExperiences(orderBy: startDate_DESC) {
				job
				jobDescription
				jobEndDate
				startDate
				stillEmployedHere
				company
			}
			hobbies: allHobbies {
				name
				image {
				alt
				url
				}
				description
			}
			education: allEducations(orderBy: start_DESC) {
				school
                gpa
                start
                end
                additional
			}
			socials: allSocialLinks {
				faIcon
				link
			}
		}""")

headers = {
    'Authorization': auth
}

transport = AIOHTTPTransport(url=url, headers=headers)
client = Client(transport=transport, fetch_schema_from_transport=True)

backup_result="""{
    "aboutMe": {
      "greeting": "Hello,",
      "shortIntroduction": "I’m Catherine Laserna, an 18-year-old computer science major and self-taught programmer on the web. ",
      "about": "My passion for all things tech and games started at an early age. My family immigrated to the US when I was eight and I had a hard time making friends for a while because of cultural/language differences. Instead, I immersed myself in online spaces and games on my dad’s work laptop as a kid. Before I knew it, I was delving into a coding and web rabbit-hole.",
      "profilePicture": {
        "url": "https://www.datocms-assets.com/74353/1654746341-catherine.jpg",
        "alt": "Catherine's Face",
        "title": "Catherine's Profile Picture"
      }
    },
    "experiences": [
      {
        "job": "Production Engineering Fellow",
        "jobDescription": "The MLH Fellowship is a 12-week internship alternative for aspiring technologists. Fellows on the Production Engineering powered by Meta track experience what it's like to work in Production / Site Reliability Engineering and DevOps while having access to Meta mentors.",
        "jobEndDate": null,
        "startDate": "2022-05-10",
        "stillEmployedHere": true,
        "company": "Major League Hacking"
      },
      {
        "job": "Paid Student Intern",
        "jobDescription": "I contribute through both research for outreach and contact building, as well as well as match, pair, and facilitate MentorHER mentorship sessions.",
        "jobEndDate": null,
        "startDate": "2022-04-25",
        "stillEmployedHere": true,
        "company": "1000 Dreams Fund"
      },
      {
        "job": "Paid Cashier",
        "jobDescription": "I managed and handled money on shift. I helped stock and carry snacks, cold refreshments, hot food, and cold desserts. I sold goods and counted change.",
        "jobEndDate": "2022-06-01",
        "startDate": "2021-08-19",
        "stillEmployedHere": false,
        "company": "Sierra Pacific Snack Bar"
      },
      {
        "job": "Paid Summer Intern",
        "jobDescription": "I completed a 6-week survey course focused on introducing the professional culture of global business and topics, skills, and issues that are defining the future of work. We collaborated with 7 other interns to create a group project which included a final presentation for Accenture and Non-profit guests. Finally we apply the skills learned throughout L2L to create and present my own passion pitch",
        "jobEndDate": "2021-08-10",
        "startDate": "2021-06-28",
        "stillEmployedHere": false,
        "company": "Accenture"
      },
      {
        "job": "Facilitator",
        "jobDescription": "I taught a 10-week introduction to Python and AI to 4 high school peers at the Hanford Longfield center, providing pizza and laptops funded through stipends by the Hall STEM Initiative. I curated a 10-week course, complementing slides, and presented the lessons. ",
        "jobEndDate": "2020-06-01",
        "startDate": "2019-08-19",
        "stillEmployedHere": false,
        "company": "Hall STEM Initiative"
      }
    ],
    "hobbies": [
      {
        "name": "Gaming",
        "image": {
          "alt": "rgb keyboard",
          "url": "https://www.datocms-assets.com/74353/1655113789-pexels-tima-miroshnichenko-5380602.jpg"
        },
        "description": "My favorite games of all time are Zelda: Breath of The Wild and Hypnospace Outlaw"
      },
      {
        "name": "Singing",
        "image": {
          "alt": "music sheet",
          "url": "https://www.datocms-assets.com/74353/1655113247-pexels-pixabay-164821.jpg"
        },
        "description": "I've been heavily involved in choir and theatre for most of my academic career."
      },
      {
        "name": "Design",
        "image": {
          "alt": "One of my designs",
          "url": "https://www.datocms-assets.com/74353/1654751030-machinehealing.png"
        },
        "description": "I like mocking up apps, websites, and prototyping on Figma and other tools."
      }
    ],
    "education": [
      {
        "school": "Fresno State University",
        "gpa": null,
        "start": "2022-08-17",
        "end": "2026-06-01",
        "additional": "I'm apart of the Smittcamp Honors Program w/ a full scholarship :)"
      },
      {
        "school": "Sierra Pacific Highschool",
        "gpa": 4,
        "start": "2018-08-17",
        "end": "2022-06-01",
        "additional": "AP World, AP US Hist, AP Lang, AP Lit, AP Calc, and Physics Honors"
      }
    ],
    "socials": [
      {
        "faIcon": "instagram",
        "link": "https://www.instagram.com/clasernaj/"
      },
      {
        "faIcon": "share-square",
        "link": "http://tiktok.com/@bubbaguppylive"
      },
      {
        "faIcon": "youtube",
        "link": "https://www.youtube.com/channel/UCCncUabhB43dAZ7ZMAiwIbA"
      },
      {
        "faIcon": "Twitter",
        "link": "https://twitter.com/bubbaguppylive"
      },
      {
        "faIcon": "Twitch",
        "link": "http://twitch.tv/bubbaguppylive"
      },
      {
        "faIcon": "LinkedIn",
        "link": "https://www.linkedin.com/in/catherinelaserna/"
      },
      {
        "faIcon": "Github",
        "link": "https://github.com/cjlaserna/"
      }
    ]
}"""

try:
    result = client.execute(query)
except:
    result = json.loads(backup_result)

# result = json.loads(backup_result)
# print(result["aboutMe"])
