from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

# Load environment variables
load_dotenv()

# Correct GROQ API key setup
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Define LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# ---------------- BLOG RESEARCHER ----------------

blog_researcher = Agent(
    role="Blog Researcher from YouTube Videos",
    goal="Get the relevant video content for the topic {topic} from the YouTube channel",
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos related to AI, Data Science, "
        "Machine Learning, and GenAI, providing insightful suggestions."
    ),
    tools=[yt_tool],
    allow_delegation=True,
)

# ---------------- BLOG WRITER ----------------

blog_writer = Agent(
    role="Writer",
    goal="Narrate compelling tech stories about the video {topic} from the YouTube channel",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft engaging "
        "narratives that captivate and educate, bringing new discoveries "
        "to light in an accessible manner."
    ),
    llm=llm,
    tools=[yt_tool],
    allow_delegation=True,
)
print("crew.py is running")
