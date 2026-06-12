import generativeai as genai


genai.configure(api_key="AIzaSyBVAgpHBzWJhqQjoA2TzujY2aJBZfwq45M")
[print(m.name) for m in genai.list_models()]
model = genai.GenerativeModel("models/gemini-2.0-flash")  

def generate_reply(clean_chat, persona_name="Cartoonbhai.art"):
      
    prompt = f"""You are Cartoonbhai.art, an Indian artist and coder who speaks Hindi and English.
Analyze this chat and reply naturally as Cartoonbhai.art.
Output only the next message, what is coding.

Chat:
{clean_chat}"""

    response = model.generate_content(prompt)
    return response.text.strip()
if __name__ == "__main__":
    reply = generate_reply("Hey bro how are you?")
    print("Test reply:", reply)