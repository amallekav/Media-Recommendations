def get_user_preferences():
    preferences = []
    questions = [
        "What topics are you interested in?",
        "Do you prefer short or long articles?",
        "Do you enjoy reading news from multiple perspectives?",
        "Do you prefer factual or opinion-based articles?",
        "Are you interested in scientific news?",
        "Do you like reading in-depth analysis?",
        "Are you interested in current affairs and politics?",
        "Do you enjoy reading personal stories and narratives?",
        "Do you like reading book reviews and literary articles?",
        "Are you interested in lifestyle and entertainment news?"
    ]

    print("Please answer the following questions about your reading preferences (Y/N):")
    for question in questions:
        answer = input(question + " ")
        preferences.append(answer.lower() == "y")

    return preferences


def recommend_reading(preferences):
    recommendations = []

    if preferences[0]:
        recommendations.append("News articles related to your topics of interest.")
    if preferences[1]:
        recommendations.append("Short articles that can be read quickly.")
    if preferences[2]:
        recommendations.append("News sources that provide different perspectives.")
    if preferences[3]:
        recommendations.append("Articles that align with your preferred style (factual or opinion-based).")
    if preferences[4]:
        recommendations.append("Scientific news and discoveries.")
    if preferences[5]:
        recommendations.append("In-depth analysis and feature articles.")
    if preferences[6]:
        recommendations.append("Current affairs and political news.")
    if preferences[7]:
        recommendations.append("Personal stories and narratives.")
    if preferences[8]:
        recommendations.append("Book reviews and literary articles.")
    if preferences[9]:
        recommendations.append("Lifestyle and entertainment news.")

    return recommendations


def main():
    print("Welcome to the Reading Recommendation Program!")
    print("We'll ask you a series of questions to understand your reading preferences.")
    print("Based on your responses, we'll recommend different types of news, media, and reading materials.")

    preferences = get_user_preferences()
    recommendations = recommend_reading(preferences)

    print("\nBased on your preferences, we recommend the following:")
    for recommendation in recommendations:
        print("- " + recommendation)


if __name__ == "__main__":
    main()
