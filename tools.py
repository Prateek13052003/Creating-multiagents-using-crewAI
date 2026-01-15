from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

from crewai_tools import YoutubeChannelSearchTool

yt_tool = YoutubeChannelSearchTool(
    youtube_channel_handle="https://www.youtube.com/channel/UCNU_lfiiWBdtULKOw6X0Dig"
)
