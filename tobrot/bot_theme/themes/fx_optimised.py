class TXStyle:
    TOGGLEDOC_MSG = '''โโโ ๐   ๐ง๐ผ๐ด๐ด๐น๐ฒ ๐ฆ๐ฒ๐๐๐ถ๐ป๐ด๐ :
โ
โฃ ๐ค ๐๐ฌ๐๐ซ : {u_men} ( #ID{u_id} )
โ
โฃ๐ท ๐๐จ๐ ๐ ๐ฅ๐ : ๐<code>Document ๐</code>
โ
โโโฆ๏ธโ๐ ๐จ๐๐ฃ๐๐ ๐น๐ช {UPDATES_CHANNEL}โฆ๏ธโโน'''
    TOGGLEVID_MSG = '''โโโ ๐   ๐ง๐ผ๐ด๐ด๐น๐ฒ ๐ฆ๐ฒ๐๐๐ถ๐ป๐ด๐ :
โ
โฃ ๐ค ๐๐ฌ๐๐ซ : {u_men} ( #ID{u_id}
โ
โฃ๐ท๐๐จ๐ ๐ ๐ฅ๐ : <code>๐ Video ๐</code>
โ
โโโฆ๏ธโ๐ ๐จ๐๐ฃ๐๐ ๐น๐ช {UPDATES_CHANNEL}โฆ๏ธโโน'''
    THUMB_REPLY = "<code>Processing . . . ๐</code>"
    SAVE_THUMB_MSG = "<b>โก<i>Custom Thumbnail ๐ผ Saved for Next Uploads</i>โก</b>\n\n <b><i>โYour Photo is Set, Ready to Go ...๐จโ๐ฆฏ</i></b>."
    SAVE_THUMB_FAIL_MSG = "<b><i>โSorryโ</i></b>\n\n<b>โ Reply with Image to Save Your Custom Thumbnail.โ</b>"
    CLEAR_THUMB_SUCC_MSG = "<b><i>โSuccessโ</i></b>\n\n <b>๐ผCustom Thumbnail Cleared Successfully As Per Your Request.</b>"
    CLEAR_THUMB_FAIL_MSG = "<b><i>โSorryโ</i></b>\n\n <b>โNothing to Clear For Youโ</b>"
    PREFIX_MSG = "โก๏ธ<i><b>Custom Prefix Set Successfully</b></i> โก๏ธ \n\n๐ค <b>User :</b> {u_men}\n๐ <b>User ID :</b> <code>{uid}</code>\n๐ <b>Prefix :</b> <code>{t}</code>"
    CAPTION_MSG = "โก๏ธ<i><b>Custom Caption Set Successfully</b></i> โก๏ธ \n\n๐ค <b>User :</b> {u_men}\n๐ <b>User ID :</b> <code>{uid}</code>\n๐ <b>Caption :</b>\n<code>{t}</code>"
    IMDB_MSG = "โก๏ธ<i><b>Custom Template Set Successfully</b></i> โก๏ธ \n\n๐ค <b>User :</b> {u_men}\n๐ <b>User ID :</b> <code>{uid}</code>\n๐ <b>IMDB Template :</b> \n<code>{t}</code>"
    THEME_MSG = "โก๏ธ <i><b>Available Custom Themes</b></i> โก๏ธ\n\n๐ค <b>User :</b> {u_men}\n๐ <b>User ID :</b> <code>{uid}</code>\n\n๐ <b>Choose Available Theme from Below:</b>"
    STATS_MSG_1 = 'โโโโโ ๐ ๐๐ผ๐ ๐ฆ๐๐ฎ๐๐ ๐ โโโโโโป\nโ\n'
    STATS_MSG_2 = 'โฃ ๐ <b>Commit Date:</b> {lc}\nโ\n'
    STATS_MSG_3 = '''โฃ ๐ค <b>Bot Uptime:</b> {currentTime}
โฃ ๐ถ <b>OS Uptime:</b> {osUptime}
โ
โฃ ๐ฆ<b>CPU:</b>
โ  โ <code>{cpu_prog} {cpuUsage}%</code>
โ
โฃ ๐งฌ <b>RAM:</b>
โ  โ <code>{mem_prog} {mem_p}%</code>
โฃย  โข <i><b>Total:</b> {mem_t}</i> โ โข <i><b>Used:</b> {mem_u}</i>
โย ย ย ย ย ย ย ย ย ย ย ย ย ย ย  โข <i><b>Free:</b> {mem_a}</i>
โ
โฃ ๐ <b>DISK:</b>
โ  โ <code>{disk_prog} {disk}%</code>
โฃย  โข <i><b>Total:</b> {total}</i> โ โข <i><b>Used:</b> {used}</i>
โย ย ย ย ย ย ย ย ย ย ย ย ย ย ย  โข <i><b>Free:</b> {free}</i>
โ
โฃ ๐ <b>SWAP:</b>
โ  โ <code>{swap_prog} {swap_p}%</code>
โฃ  โข <i><b>Total:</b> {swap_t}</i> โ โข <i><b>Used:</b> {swap_u}</i>
โ                โข <i><b>Free:</b> {swap_f}</i>
โ
โฃ ๐ <b>CORES:</b>
โ  โ <code>{core_prog} {core_per}%</code>
โฃ ๐ <i><b>Physical Cores:</b> {p_core}</i> โ ๐ <i><b>Total Cores:</b> {t_core}</i>
โ
โฃ ๐ค <b>Total Upload Data :</b> {sent}
โฃ ๐ฅ <b>Total Download Data :</b> {recv}
โ
โโโฆ๏ธโ๐ ๐จ๐๐ฃ๐๐ ๐น๐ช {UP_CHANNEL}โฆ๏ธโโน'''
    HELP_MSG = '''โโ ๐ <b>HELP MODULE</b> ๐ โโโโป
โ
โโข <i>Open Help to Get Tips and Help</i>
โโข <i>Use the Bot Like a Pro User</i>
โโข <i>Access Every Feature That Bot Offers in Better Way </i>
โโข <i>Go through Commands to Get Help</i>
โ
โโโฆ๏ธโ๐ ๐จ๐๐ฃ๐๐ ๐น๐ช {UPDATES_CHANNEL}โฆ๏ธโโน'''
    INDEX_SCRAPE_MSG = """
โโ๐ฎ  ๐๐ป๐ฑ๐ฒ๐ ๐ฆ๐ฐ๐ฟ๐ฎ๐ฝ๐ฒ ๐ฅ๐ฒ๐๐๐น๐ :
โ
โฃ๐ค ๐๐ฌ๐๐ซ : {u_men} ( #ID{uid} )
โ
โฃ๐ ๐จ๐ฅ๐ : <code> {url} </code>
โ
โโโฆ๏ธโ๐ ๐จ๐๐ฃ๐๐ ๐น๐ช {UPDATES_CHANNEL}โฆ๏ธโโน
"""
    MEDIAINFO_MEDIA_MSG = '''
โน๏ธ <code>MEDIA INFO</code> โน
โ
โโข <b>File Name :</b> <code>{filename}</code>
โโข <b>Mime Type :</b> <code>{mimetype}</code>
โโข <b>File Size :</b> <code>{filesize}</code>
โโข <b>Date :</b> <code>{date}</code>
โโข <b>File ID :</b> <code>{fileid}</code>
โโข <b>Media Type :</b> <code>{txt}</code>
โ
โโโฆ๏ธโ๐ ๐จ๐๐ฃ๐๐ ๐น๐ช {UPDATES_CHANNEL}โฆ๏ธโโน
'''
    MEDIAINFO_DIRECT_MSG = """
โน๏ธ <code>DIRECT LINK INFO</code> โน
โ
โโข <b>File Name :</b> <code>{tit}</code>
โโข <b>Direct Link :</b> <code>{link}</code>
โ
โโโฆ๏ธโ๐ ๐จ๐๐ฃ๐๐ ๐น๐ช {UPDATES_CHANNEL}โฆ๏ธโโน
"""
    SPEEDTEST_MSG = '''
โโโโโโโโโโโโโโโโโโโโป
โฃโโ๐ ๐๐ฉ๐๐๐๐ญ๐๐ฌ๐ญ ๐๐ง๐๐จ:
โฃ <b>Upload:</b> <code>{upload}/s</code>
โฃ <b>Download:</b>  <code>{download}/s</code>
โฃ <b>Ping:</b> <code>{ping} ms</code>
โฃ <b>Time:</b> <code>{timestamp}</code>
โฃ <b>Data Sent:</b> <code>{bytes_sent}</code>
โฃ <b>Data Received:</b> <code>{bytes_received}</code>
โ
โฃโโ๐ ๐๐ฉ๐๐๐๐ญ๐๐ฌ๐ญ ๐๐๐ซ๐ฏ๐๐ซ:
โฃ <b>Name:</b> <code>{name}</code>
โฃ <b>Country:</b> <code>{country}, {cc}</code>
โฃ <b>Sponsor:</b> <code>{sponsor}</code>
โฃ <b>Latency:</b> <code>{latency}</code>
โฃ <b>Latitude:</b> <code>{serverlat}</code>
โฃ <b>Longitude:</b> <code>{serverlon}</code>
โ
โฃโโ๐ค ๐๐ฅ๐ข๐๐ง๐ญ ๐๐๐ญ๐๐ข๐ฅ๐ฌ:
โฃ <b>IP Address:</b> <code>{ip}</code>
โฃ <b>Latitude:</b> <code>{clientlat}</code>
โฃ <b>Longitude:</b> <code>{clientlon}</code>
โฃ <b>Country:</b> <code>{clicountry}</code>
โฃ <b>ISP:</b> <code>{isp}</code>
โฃ <b>ISP Rating:</b> <code>{isprating}</code>
โ
โโโโโโโโโโโโโโโโโโโโน
'''
    TSHELP_MSG = '''
โโ ๐ง๐ผ๐ฟ๐ฟ๐ฒ๐ป๐ ๐ฆ๐ฒ๐ฎ๐ฟ๐ฐ๐ต ๐ ๐ผ๐ฑ๐๐น๐ฒ โโโป
โ
โโข /nyaasi <i>[search query]</i>
โโข /sukebei <i>[search query]</i>
โโข /1337x <i>[search query]</i>
โโข /piratebay <i>[search query]</i>
โโข /tgx <i>[search query]</i>
โโข /yts <i>[search query]</i>
โโข /eztv <i>[search query]</i>
โโข /torlock <i>[search query]</i>
โโข /rarbg <i>[search query]</i>
โโข /ts <i>[search query]</i>
โ
โโโฆ๏ธโ๐ ๐จ๐๐ฃ๐๐ ๐น๐ช {UPDATES_CHANNEL}โฆ๏ธโโน
'''
    STATUS_MSG_1 = '''
โโโโโโโโโโโโโโโโโโโโป
โฃ๐ ๐๐๐ฆ๐: <a href='{mess_link}'>{file_name}</a>
โฃ๐ ๐๐ญ๐๐ญ๐ฎ๐ฌ: <i>Downloading...๐ฅ</i>
โ<code>{progress}</code>
โฃโก๏ธ ๐๐จ๐ฐ๐ง๐ฅ๐จ๐๐๐๐: <code>{prog_string}</code> <b>of</b> <code>{total_string}</code>
โฃ๐ก ๐๐ฉ๐๐๐: <code>{speed_string}</code>, โณ๏ธ ๐๐๐: <code>{eta_string}</code>'''
    STATUS_MSG_2 = "\nโฃโฐ๏ธ ๐๐ฅ๐๐ฉ๐ฌ๐๐: <code>{etime}</code>"
    STATUS_MSG_3 = '''
โฃ<b>๐ค ๐๐ฌ๐๐ซ:</b> {u_men} ( #ID{uid} )
โฃ<b>โ ๏ธ ๐๐๐ซ๐ง:</b> <code>/warn {uid}</code>'''
    STATUS_MSG_4 = "\nโฃ๐ ๐๐จ๐ง๐ง๐๐๐ญ๐ข๐จ๐ง๐ฌ: <code>{connections}</code>"
    STATUS_MSG_5 = "\nโฃ๐ ๐๐๐๐๐๐ซ๐ฌ: <code>{num_seeders}</code> โ๐ ๐๐๐๐๐ก๐๐ซ๐ฌ: <code>{connections}</code>"
    STATUS_MSG_6 = '''
โฃ๐ซ ๐๐จ ๐๐๐ง๐๐๐ฅ: /cancel_{gid}
โโโโโโโโโโโโโโโโโโโโน
'''
    TOP_STATUS_MSG = '''
โฃ ๐ฝ๐ฎ : {umen} (<code>{uid}</code>)
โโโโโโโโโ โ โโโโโโโโโ'''
    BOTTOM_STATUS_MSG = "โโโโโโโโโ โ โโโโโโโโโ"
    DEF_STATUS_MSG = '''
โโโโโโโโโโโโโโโโโโโโป
โ
โ โ ๏ธ <b>No Active, Queued or Paused 
โ Torrents / Direct Links โ ๏ธ</b>
โ
โโโโโโโโโโโโโโโโโโโโน
'''
    WRONG_COMMAND = "<i> Hey {u_men}, \n\n โ ๏ธ Check and Send a Valid Download Source to Start Me Up !! โ ๏ธ</i>"
    WRONG_DEF_COMMAND = "<b>โ ๏ธ Opps โ ๏ธ</b>\n\n <b><i>โ  Reply with Direct/Torrent Link or Fileโ๏ธ</i></b>"
    DOWNLOAD_ADDED_MSG = "โโโโโโโโโโโโโโโโโโป\nโฃ๐ค ๐๐ฌ๐๐ซ : {u_men}({u_id}) \nโ\nโ <code>โก๏ธ Your Request Has Been Added To The Status List โก๏ธ</code> \nโ\nโฃ <b><u>Send</u> /{status_cmd} <u>To Check Your Progress</u></b>\nโ\nโโโฆ๏ธโ๐ ๐จ๐๐ฃ๐๐ ๐น๐ช {UPDATES_CHANNEL}โฆ๏ธโโน"
    EXCEP_DEF_MSG = "<b> ๐Maybe You Didn't Know I am Being Used !!</b> \n\n<b>๐ API Error</b>: {cf_name}"
    WRONG_RENAME_MSG = "<b>โ ๏ธ Oops โ ๏ธ</b>\n\nโกProvide Name with extension.\n\nโฉ<b>Example</b>: <code> /rename Sample.mkv</code>"
    TOP_LIST_FILES_MSG = '''โ ๐ ๐๐๐๐๐ ๐พ๐ค๐ข๐ฅ๐ก๐๐ฉ๐ !! ๐
โ
โฃ ๐ค ๐๐ฌ๐๐ซ : {u_men} ( #ID{user_id} )
โฃ โฐ๏ธ ๐๐ฅ๐๐ฉ๐ฌ๐๐ : {timeuti}
โ
'''
    BOTTOM_LIST_FILES_MSG = '''โ
โ #Uploads
โ
โโโฆ๏ธโ๐ ๐จ๐๐ฃ๐๐ ๐น๐ช {UPDATES_CHANNEL}โฆ๏ธ'''
    SINGLE_LIST_FILES_MSG = "โฃ โ <a href='{private_link}'>{local_file_name}</a>\n"
    EXTRACT_MSG = "<b><i>๐  Extracting : </i></b> <code>{no_of_con}</code> <b>File(s)</b>"
    START_UPLOAD_MSG = '''โ๐ ๐๐๐ฆ๐: <code>{filename}</code>
โ
โ๐ ๐๐ญ๐๐ญ๐ฎ๐ฌ: <b><i>Uploading...๐ค</i></b>'''
    START_DOWM_MSG = '''โโก๏ธ <i>Telegram Download Initiated</i> โก๏ธ
โ
โ๐ ๐๐ญ๐๐ญ๐ฎ๐ฌ: <b><i>Downloading...๐ฅ</i></b>'''

    DOWN_COM_MSG = '''โ๐ ๐๐๐ฆ๐: `{filename}`
โ
โฃ๐ ๐๐ญ๐๐ญ๐ฎ๐ฌ: <b><i>Downloaded ๐ฅ</i></b>
โฃ๐ฆ ๐๐ข๐ณ๐: `{size}`
โ
โ #Downloaded'''
    DOWN_RE_COM_MSG = '''โ๐ ๐๐๐ฆ๐: `{base_file_name}`
โ
โฃ๐ ๐๐ญ๐๐ญ๐ฎ๐ฌ: <b><i>Downloaded ๐ฅ</i></b>
โฃ๐ฆ ๐๐ข๐ณ๐: `{file_size}`
โฃโฐ๏ธ ๐๐ข๐ฆ๐ ๐๐๐ค๐๐ง: `{tt}`
โ
โ #Downloaded'''
    TOP_PROG_MSG = '''โโโโโโโโ โ โโโโโโโโ

โโโโโโโโโโโโโโโโโโป
โฃ๐ ๐๐๐ฆ๐: `{base_file_name}`'''
    PROG_MSG = '''โ
โ<code>[{0}{1}{2}] {3}%</code>
โ
'''
    DOWN_PROG_MSG = '''โฃ๐ฆ ๐๐จ๐ญ๐๐ฅ : `ใ{t}ใ`
โฃโก๏ธ ๐๐จ๐ฐ๐ง๐ฅ๐จ๐๐๐๐  :`ใ{d}ใ`
โฃ๐ก ๐๐ฉ๐๐๐ : ` ใ{s}ใ`
โฃโณ๏ธ ๐๐๐ : `ใ{eta}ใ`
โโโฆ๏ธโ๐ ๐จ๐๐ฃ๐๐ ๐น๐ช {UPDATES_CHANNEL}โฆ๏ธโโน

โโโโโโโโ โ โโโโโโโโ'''

    CANCEL_PROG_BT = "โ ๐๐๐ก๐๐๐ โ"
