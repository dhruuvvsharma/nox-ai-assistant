from client import client
def ask(prompt):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system",
                "content": "You are Advance-Nox, you are an AI assistant. First you'll introduce yourself then give response, Give short voice assistant responses."}
                ,{"role": "user",
                "content": prompt}
                ]
        )

        return response.choices[0].message.content

    except Exception as e:
        print("AI Error:", e)
        return "Sorry, I am unable to connect to the AI service right now."