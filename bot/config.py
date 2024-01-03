#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = ("25164506")
    API_HASH = ("2771620a92dd0d044e51a787f18565c0")
    BOT_TOKEN = ("6926658380:AAFa1LrCf-yHGuJ9-dPnUw4Ywx8-gu8sswY")
    DEV = 5467555331
    OWNER = ("5098097249")
    ffmpegcode = ["-preset faster -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By AnshuSharma (https://github.com/Anshusharma75/TG-videoCompress)' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1"]
    THUMB = ("https://graph.org/file/2d09921cab4461e27d286.png")
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit(1)
