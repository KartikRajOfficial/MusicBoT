from Kartik.core.dir import dirr
from Kartik.core.git import git
from Kartik.core.userbot import Userbot
from Kartik.misc import dbb, heroku
from Kartik.core.bot import Kartikraj

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Kartikraj()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
