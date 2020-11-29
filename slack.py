from slacker import Slacker

token = "xoxb-135797385811-933250460480-Yl5z76aaCNNiSRP4x2rnWJXq" # 종봇
#token = "xoxb-135797385811-935194805424-sld7lHzgzmnEawz0nV4mmj2T" # 데참이

slack = Slacker(token)
slack.chat.post_message('mkt_naver_sa_auto_alert', ':wowwwwww:', as_user=True)
#slack.chat.post_message('mkt_signup_alert', 'test', as_user=True)
