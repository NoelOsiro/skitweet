def tweet_thread_from_json_entry(entry):
        """
        Post a tweet thread based on data from a JSON entry.

        Args:
            entry (dict): A dictionary containing information for the tweet thread.

        Returns:
            None
        """
        # Create the first tweet in the thread
        first_tweet = f"📢 Project Name: {entry['title']}"
        location_info = f"🌍 Location: This project serves a global audience, spanning across various regions and countries, making it a worldwide initiative."
        sdgs_info = f"🌱 Sustainable Development Goals (SDGs): {', '.join(entry['sdg'])}. This project aligns with key global development goals, contributing to a sustainable future."
        description = f"📋 Project Description: {entry['description']}. This initiative is a humanitarian risk intelligence platform designed to provide early warning and decision support to the public, governments, and NGOs worldwide."
        source_link = f"🔗 Source: Learn more about this project on the official website: {entry['source']}. Stay informed and support this vital humanitarian effort!"
        print(first_tweet)
        print(location_info)
        print(sdgs_info)
        print(description)
        print(source_link)

def generate_first_tweet(entry):
        first_tweet = f"📢 Project Name: {entry['title']}"
        
entry = {
        "title": "MobileAid",
        "description": "Using geo-targeting and machine learning to deliver relief to society's most vulnerable groups",
        "theme": [
            "Disaster Mitigation"
        ],
        "use_case": "Disaster Relief logistic/resource allocation ",
        "status": "production",
        "disaster_cycle": "response",
        "technology": [
            "Machine Learning",
            "Geographical Information Systems"
        ],
        "disaster_type": "Various",
        "region": [
            "Africa"
        ],
        "subregion": [
            "Eastern Africa"
        ],
        "country": [
            "Malawi"
        ],
        "partner": [
            "UNDP",
            "UNDP Bangladesh /a2i",
            "World Bank",
            "Center for Effective Global Action (CEGA)",
            "USAID",
            "Google.org",
            "Government of Togo",
            "Fonds Social de la Republique Democratique du Congo (Social Fund of the Democratic Republic of Cong"
        ],
        "un_host": [
            "UNDP"
        ],
        "data": [
            "Mobile Network Data"
        ],
        "sdg": [
            "SDG 1"
        ],
        "date_of_implementation": "2022",
        "source": "https://www.givedirectly.org/",
        "img_url": "https://www.givedirectly.org/wp-content/uploads/2021/07/Transfer-Withdrawal-scaled-1-705x469.jpeg",
        "id": 173,
        "uuid": "dfbcba81-22a3-4a31-91df-16a8df85f2b1",
        "created_at": "2023-07-11T09:14:28.714411+00:00",
        "updated_at": 'null',
        "tr_projects_id": 109
    }
tweet_thread_from_json_entry(entry) 