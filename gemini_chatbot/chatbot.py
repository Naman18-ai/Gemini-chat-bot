import google.generativeai as genai

genai.configure(api_key="AIzaSyBIaX8H4PmSt8IyeDy61fseDJD89mRCDd4")

def get_user_input():
    generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
        }

    safety_settings = [
    {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config=generation_config,
                              safety_settings=safety_settings)
    while True:
        user_input = input("You: ")
        if not user_input:
            print("Please provide some input")
        convo = model.start_chat(history=[
        { 
        "role": "user",
        "parts": [user_input]
        },
        {
        "role": "model",
        "parts": ["Hello there, you kid I am Gemini and I will mess up your future haha"]
         },
        ])

        convo.send_message(user_input)
        print(convo.last.text)


get_user_input()