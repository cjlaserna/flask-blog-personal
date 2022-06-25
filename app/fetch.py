from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import os
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

result = client.execute(query)
test = result["hobbies"]
