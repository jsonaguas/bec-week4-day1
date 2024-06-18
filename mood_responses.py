def mood_response(mood):
    if mood.lower() == "happy":
        return "Awesome to hear you're doing well!"
    elif mood.lower() == "sad":
        return "I'm sorry to hear that, let me know if I can help."
    elif mood.lower() == "angry":
        return "Let's take a moment to breathe. What's going on?"
    elif mood.lower() == "excited":
        return "That's great! Why are you so excited?"
    else:
        return "Interesting, tell me more."
    
